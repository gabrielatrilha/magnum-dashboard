#!/usr/bin/env python3
"""
fetch_bi_data.py — Coleta dados do BI Emultec e atualiza bi_data.json
Executa automaticamente via Windows Task Scheduler.

Fontes (endpoints analise — dados exatos do BI):
  /analise/40  → faturamento     (campo SUBTOTAL)
  /analise/41  → cirurgias       (campo CONT_CIRURGIA)
  /analise/43  → despesas        (campo VALOR)
  /analise/44  → inadimplência   (campo VALOR, acumulado histórico)
"""

import os, sys, json, re, subprocess
from datetime import datetime, date
from pathlib import Path
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).parent
BI_URL        = "https://bi.emultec.com.br"
BI_USER       = "gabriela@magnumimport.com.br"
BI_PASS       = "847597"
GITHUB_REPO   = "gabrielatrilha/magnum-dashboard"
GITHUB_BRANCH = "main"

# Lê .env para sobrescrever defaults
_env_file = SCRIPT_DIR / ".env"
if _env_file.exists():
    for _line in _env_file.read_text(encoding="utf-8").splitlines():
        if "=" in _line and not _line.startswith("#"):
            _k, _v = _line.split("=", 1)
            _k = _k.strip(); _v = _v.strip().strip('"').strip("'")
            if _k == "BI_USER"      and _v: BI_USER  = _v
            if _k == "BI_PASS"      and _v: BI_PASS  = _v
            if _k == "GITHUB_TOKEN" and _v: os.environ["GITHUB_TOKEN"] = _v

def br_float(s):
    try:
        return float(str(s).strip().replace(".", "").replace(",", "."))
    except:
        return 0.0

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def mes_atual():
    """Retorna (inicio_mes, hoje) como strings YYYY-MM-DD"""
    hoje = date.today()
    inicio = hoje.replace(day=1)
    return inicio.strftime("%Y-%m-%d"), hoje.strftime("%Y-%m-%d")

# ── 1. Login ──────────────────────────────────────────────────────────────────
def make_session():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0"
    resp = s.post(f"{BI_URL}/login",
                  data={"email": BI_USER, "password": BI_PASS},
                  allow_redirects=True, timeout=30)
    if "login" in resp.url.lower():
        raise RuntimeError(f"Login falhou. URL final: {resp.url}")
    log(f"Login OK → {resp.url}")
    return s

# ── 2. Função genérica: busca o total de um endpoint analise ─────────────────
def get_analise_total(s, analise_id, filters, campo):
    """
    Busca o valor total de um relatório /analise/{id}.

    filters : lista de strings no formato 'CAMPO;operador;valor'
              ex: ['UNIDADE_EMPRESA;!=;C62', 'DATA_NOTA;entre;2026-06-01;2026-06-09']
    campo   : coluna a retornar (ex: 'SUBTOTAL', 'VALOR', 'CONT_CIRURGIA')

    Retorna float do total (linha totalizadora marcada com '-').
    """
    f = "|".join(filters)
    url = f"{BI_URL}/analise/{analise_id}?f={quote(f)}&campos={campo}"
    log(f"  GET /analise/{analise_id} ...")
    resp = s.get(url, timeout=60)
    soup = BeautifulSoup(resp.text, "html.parser")

    # Linha totalizadora: primeira célula contém exatamente '-'
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if cells and cells[0].get_text(strip=True) == "-":
            return br_float(cells[-1].get_text(strip=True))

    # Fallback: tenta a última linha com dados numéricos
    for row in reversed(soup.find_all("tr")):
        cells = row.find_all("td")
        if len(cells) >= 2:
            try:
                val = br_float(cells[-1].get_text(strip=True))
                if val > 0:
                    return val
            except:
                pass
    log(f"  AVISO: total não encontrado em analise/{analise_id} — retornando 0")
    return 0.0

# ── 3. Faturamento — /analise/40, campo SUBTOTAL ──────────────────────────────
def get_faturamento(s):
    inicio, hoje = mes_atual()
    filters = [
        "UNIDADE_EMPRESA;!=;C62",
        f"DATA_NOTA;entre;{inicio};{hoje}",
    ]
    val = get_analise_total(s, 40, filters, "SUBTOTAL")
    log(f"Faturamento: R$ {val:,.2f}")
    return val

def get_nf_count(s):
    """Conta NFs emitidas no mês atual via CONT_NOTA (analise/40)."""
    inicio, hoje = mes_atual()
    filters = [
        "UNIDADE_EMPRESA;!=;C62",
        f"DATA_NOTA;entre;{inicio};{hoje}",
    ]
    val = get_analise_total(s, 40, filters, "CONT_NOTA")
    count = int(val)
    log(f"NF count: {count}")
    return count

def get_faturamento_por_un(s):
    """Retorna dict {nome_un: subtotal} para o mês atual (analise/40 por unidade)."""
    from urllib.parse import quote as _q
    inicio, hoje = mes_atual()
    UNIT_MAP = {"C61":"RS","C63":"SP","C64":"PR","C65":"Holep","C66":"Traumato","C67":"SC","C68":"BA"}
    f = f"UNIDADE_EMPRESA;!=;C62|DATA_NOTA;entre;{inicio};{hoje}"
    url = f"{BI_URL}/analise/40?f={_q(f)}&campos=UNIDADE_EMPRESA,SUBTOTAL"
    resp = s.get(url, timeout=60)
    from bs4 import BeautifulSoup as _BS
    soup = _BS(resp.text, "html.parser")
    result = {}
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:
            un_raw = cells[1].get_text(strip=True)  # primeira coluna = #, segunda = UNIDADE
            val_raw = cells[-1].get_text(strip=True)
            if un_raw and un_raw != "-" and un_raw != "Unidade_Empresa":
                un_name = UNIT_MAP.get(un_raw, un_raw)
                try:
                    result[un_name] = float(val_raw.replace(".","").replace(",","."))
                except:
                    pass
    log(f"Faturamento por UN: {result}")
    return result

# ── 4. Despesas — /analise/43, campo VALOR ────────────────────────────────────
def get_despesas(s):
    inicio, hoje = mes_atual()
    filters = [
        "QUITADO;=;SIM",
        "UNIDADE_EMPRESA;!=;C62",
        f"DATA_PAGTO;entre;{inicio};{hoje}",
    ]
    val = get_analise_total(s, 43, filters, "VALOR")
    log(f"Despesas: R$ {val:,.2f}")
    return val

# ── 5. Cirurgias — /analise/41, campo CONT_CIRURGIA ──────────────────────────
def get_cirurgias(s):
    inicio, hoje = mes_atual()
    # Exclui materiais/procedimentos que não são cirurgias
    tipos_excluir = "AGULHA BONEE,AGULHA-BONEE,SPEED-TERCEIROS,SONDAS,SPEEDICATH"
    filters = [
        f"TIPO_CIRURGIA;nin;{tipos_excluir}",
        "UNIDADE_EMPRESA;!=;C62",
        f"DATA_CIRURGIA;entre;{inicio};{hoje}",
    ]
    val = get_analise_total(s, 41, filters, "CONT_CIRURGIA")
    cir = int(val)
    log(f"Cirurgias: {cir}")
    return cir

# ── 6b. Receita × Despesa por mês — /analise/45 (pagar_receber_agrupado) ────
def get_a45_por_mes(s):
    """
    Retorna dict {'AAAA-MM': {'rec': float, 'desp': float}} via analise/45.
    Filtro: UNIDADE_EMPRESA!=C62, DATA_PG entre 2025-06-01 e hoje.
    Campos: REF_BAIXA, DESPESA, RECEITA
    """
    hoje = date.today().strftime("%Y-%m-%d")
    f = f"UNIDADE_EMPRESA;!=;C62|DATA_PG;entre;2025-06-01;{hoje}"
    url = f"{BI_URL}/analise/45?f={quote(f)}&campos=REF_BAIXA,DESPESA,RECEITA&sort=REF_BAIXA&dir=ASC"
    log("  GET /analise/45 (receita×despesa por mês) ...")
    resp = s.get(url, timeout=60)
    soup = BeautifulSoup(resp.text, "html.parser")
    result = {}
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 4:
            ref  = cells[1].get_text(strip=True)   # ex: "2026-03"
            desp = cells[2].get_text(strip=True)
            rec  = cells[3].get_text(strip=True)
            if ref and ref != "-" and len(ref) == 7:  # formato AAAA-MM
                result[ref] = {
                    "rec":  br_float(rec),
                    "desp": br_float(desp),
                }
    log(f"  analise/45: {len(result)} meses coletados")
    return result

# ── 6. Inadimplência — /analise/44, campo VALOR (acumulado histórico) ─────────
def get_inadimplencia(s):
    # Sem filtro de data: captura tudo vencido e não pago até hoje
    filters = [
        "FUTURO;=;NAO",
        "DATA_PG;=;",          # DATA_PG vazio = não pago
        "UNIDADE_EMPRESA;!=;C62",
    ]
    val = get_analise_total(s, 44, filters, "VALOR")
    log(f"Inadimplência: R$ {val:,.2f}")
    return val

# ── 7. Salvar bi_data.json ────────────────────────────────────────────────────
def salvar_bi_data(fat, desp, cir, inad, nf_count=0, fat_por_un=None, a45=None):
    inicio, hoje = mes_atual()
    data = {
        "coleta_em":           datetime.now().strftime("%Y-%m-%d"),
        "periodo":             {"ini": inicio, "fim": hoje},
        "faturamento":         round(fat,  2),
        "nf_count":            nf_count,
        "faturamento_por_un":  fat_por_un or {},
        "despesas":            round(desp, 2),
        "cirurgias":           cir,
        "inadimplencia_total": round(inad, 2),
        "a45_por_mes":          a45 or {},
    }
    out = SCRIPT_DIR / "bi_data.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"bi_data.json salvo: Fat={fat:,.2f} NFs={nf_count} Desp={desp:,.2f} Cir={cir} Inad={inad:,.2f}")
    return data

# ── 8. Gerar dashboard HTML ───────────────────────────────────────────────────
def gerar_dashboard():
    r = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "gen_dashboard.py")],
        capture_output=True, text=True, cwd=str(SCRIPT_DIR)
    )
    if r.returncode != 0:
        raise RuntimeError(f"gen_dashboard.py falhou:\n{r.stderr}")
    log("Dashboard gerado")

# ── 9. Publicar no GitHub Pages via API ──────────────────────────────────────
def publicar_github():
    import base64, urllib.request, urllib.error
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        log("GITHUB_TOKEN ausente no .env — publicação automática desativada")
        return False

    html_path = SCRIPT_DIR / "index.html"
    html_path.write_bytes((SCRIPT_DIR / "dashboard_magnum.html").read_bytes())
    content_b64 = base64.b64encode(html_path.read_bytes()).decode()

    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/index.html"
    headers = {
        "Authorization":        f"Bearer {token}",
        "Accept":               "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    sha = ""
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            sha = json.loads(r.read())["sha"]
    except Exception:
        pass

    payload = json.dumps({
        "message": f"Auto-update {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "content": content_b64,
        "branch":  GITHUB_BRANCH,
        **({"sha": sha} if sha else {}),
    }).encode()

    req = urllib.request.Request(
        api_url, data=payload, method="PUT",
        headers={**headers, "Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            log("GitHub: publicado OK")
            return True
    except urllib.error.HTTPError as e:
        log(f"GitHub erro {e.code}: {e.read().decode()[:200]}")
        return False

# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    log("=== Coleta BI Magnum ===")
    try:
        sess       = make_session()
        fat        = get_faturamento(sess)
        nf_count   = get_nf_count(sess)
        fat_por_un = get_faturamento_por_un(sess)
        desp       = get_despesas(sess)
        cir        = get_cirurgias(sess)
        inad       = get_inadimplencia(sess)
        a45        = get_a45_por_mes(sess)
        salvar_bi_data(fat, desp, cir, inad, nf_count=nf_count, fat_por_un=fat_por_un, a45=a45)
        gerar_dashboard()
        publicar_github()
        log("=== Concluído ===")
    except Exception as e:
        log(f"ERRO: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)
