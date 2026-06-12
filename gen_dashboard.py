import json

UNIT_MAP = {"C61":"RS","C63":"SP","C64":"PR","C65":"Holep","C66":"Traumato","C67":"SC","C68":"BA"}
import os as _os, datetime as _dt

# ═══════════════════════════════════════════════════════════════
# AUTO-UPDATE: Lê bi_data.json gerado pelo fetch_bi_data.py
# Atualiza INAD, faturamento do mês atual e despesas automaticamente
# ═══════════════════════════════════════════════════════════════
_BI_DATA_FILE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "bi_data.json")
_bi = {}
if _os.path.exists(_BI_DATA_FILE):
    try:
        with open(_BI_DATA_FILE, "r", encoding="utf-8") as _f:
            _bi = json.load(_f)
        print(f"[AUTO] bi_data.json carregado: {_bi.get('coleta_em','?')}")
    except Exception as _e:
        print(f"[AUTO] Aviso: bi_data.json inválido — {_e}")

def u(code): return UNIT_MAP.get(str(code).upper(), code)

INADIMPLENTES_RAW = [
# --- RS (C61) 61.756,55 ---
["ANDROLOGIA MOINHOS",           "C61","7.000,00","20/05/2026","PARTICULAR"],
["MOINHOS DE VENTO",             "C61","6.099,05","23/05/2026","SAUDE MOINHOS"],
["MOINHOS DE VENTO",             "C61","5.567,00","24/05/2026","BRADESCO SAUDE"],
["CENTRO CLINICO GAUCHO",        "C61","3.957,00","22/05/2026","MEDSENIOR"],
["MOINHOS DE VENTO",             "C61","3.706,00","23/05/2026","SAS UNIDASUL"],
["CENTRO CLINICO GAUCHO",        "C61","3.701,50","17/05/2026","CENTRO CLINICO GAUCHO"],
["HOSPITAL UNIMED PASL",         "C61","3.600,00","24/05/2026","IPASEM"],
["UNIMED VTRP",                  "C61","3.475,00","24/05/2026","UNIMED VTRP"],
["SOC. SULINA DIVINA PROV.",     "C61","3.050,00","05/03/2026","RBS"],
["UNIMED VTRP",                  "C61","3.045,00","17/05/2026","UNIMED VTRP"],
["HOSPITAL ESTRELA",             "C61","2.700,00","25/03/2026","PARTICULAR"],
["CENTRO CLINICO GAUCHO",        "C61","2.615,00","14/05/2026","CENTRO CLINICO GAUCHO"],
["UNIMED POA",                   "C61","2.100,00","23/05/2026","UNIMED POA"],
["SANTA CASA - POA",             "C61","2.000,00","11/05/2026","PARTICULAR"],
["MAE DE DEUS - AESC",           "C61","1.812,00","23/05/2026","UNIMED POA"],
["MAE DE DEUS - AESC",           "C61","1.347,00","24/05/2026","UNIMED POA"],
["SANTA CASA - POA",             "C61","1.200,00","10/05/2026","GEAP"],
["MOINHOS DE VENTO",             "C61","750,00","08/05/2026","UNIMED POA"],
["HOSPITAL BLANC",               "C61","750,00","20/05/2026","UNIMED POA"],
["MOINHOS DE VENTO",             "C61","750,00","24/04/2026","UNIMED POA"],
["MOINHOS DE VENTO",             "C61","720,00","23/05/2026","PARTICULAR"],
["HOSPITAL HUMANIZA",            "C61","600,00","11/05/2026","HAPVIDA NOTREDAME"],
["MOINHOS DE VENTO",             "C61","376,00","11/05/2026","UNIMED POA"],
["HOSPITAL BLANC",               "C61","241,00","23/05/2026","UNIMED POA"],
["SANTA CASA - POA",             "C61","240,00","10/05/2026","DOCTOR CLIN"],
["MOINHOS DE VENTO",             "C61","160,00","23/05/2026","UNIMED VTRP"],
["FATIMA SUELI T. OLIVEIRA",     "C61","130,00","24/05/2026","PARTICULAR"],
["UNIMED TORRE II",              "C61","65,00","24/05/2026","UNIMED VALE DO SINOS"],
# --- SP (C63) 104.333,34 ---
["HOSPITAL E MATERNIDADE BRASIL","C63","93.900,00","30/03/2026","SULAMERICA"],
["HOSPITAL VILA NOVA STAR",      "C63","7.333,34","22/05/2026","PARTICULAR"],
["AC CAMARGO CANCER CENTER",     "C63","2.500,00","24/05/2026","UNIMED CNU SP"],
["BP PAULISTA",                  "C63","600,00","22/05/2026","MEDISERVICE"],
# --- BA (C65) 29.000,00 ---
["MARILI NOVELLO",               "C65","7.500,00","26/09/2025","PARTICULAR"],
["ADAO BORGES BOEIRA",           "C65","7.500,00","02/05/2026","PARTICULAR"],
["SANTA CASA - POA",             "C65","7.000,00","25/03/2026","PARTICULAR"],
["UNIMED TORRE II",              "C65","7.000,00","24/05/2026","PARTICULAR"],
# --- Traumato (C66) 725.977,82 ---
["SOC. SULINA DIVINA PROV.",     "C66","53.112,38","24/10/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","43.800,00","10/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","29.000,00","27/08/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","29.000,00","10/10/2025","PETROBRAS"],
["POSTAL SAUDE",                 "C66","27.400,00","08/03/2026","POSTAL SAUDE"],
["HOSPITAL LIFEPLUS",            "C66","26.774,92","29/06/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","26.774,92","23/10/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","26.337,46","28/10/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","25.900,00","10/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","25.900,00","19/09/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","25.200,00","12/11/2025","IPE ADM"],
["SOC. SULINA DIVINA PROV.",     "C66","25.200,00","26/11/2025","IPE ADM"],
["SOC. SULINA DIVINA PROV.",     "C66","24.921,20","25/11/2025","ISSEG"],
["SOC. SULINA DIVINA PROV.",     "C66","24.700,00","25/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","22.900,00","25/12/2025","IPE ADM"],
["SOC. SULINA DIVINA PROV.",     "C66","22.900,00","22/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","22.900,00","16/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","22.900,00","28/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","21.900,00","05/02/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","21.900,00","26/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","21.900,00","27/02/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","21.900,00","28/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","12.791,20","16/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","12.791,20","09/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","12.791,20","16/12/2025","IPERGS"],
["HOSPITAL LIFEPLUS",            "C66","12.091,20","29/06/2025","IPERGS"],
["HOSPITAL LIFEPLUS",            "C66","10.873,70","14/06/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","10.873,70","12/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","8.956,20","23/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","8.956,20","28/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","8.956,20","26/11/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","8.652,64","03/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","7.038,70","14/01/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","4.371,20","06/02/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","3.671,20","07/02/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","3.671,20","19/02/2026","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","3.271,20","27/12/2025","IPERGS"],
["SOC. SULINA DIVINA PROV.",     "C66","3.000,00","13/11/2025","IPERGS"],
# --- SC (C67) 79.150,00 ---
["HOSPITAL REGIONAL DO OESTE",   "C67","64.900,00","19/04/2026","FAS"],
["HOSP. CARIDADE FLORIANOPOLIS", "C67","10.000,00","15/05/2026","PARTICULAR"],
["UROSAS CLINICA SANTANNA",      "C67","3.120,00","24/05/2026","PARTICULAR"],
["SOS CARDIO - UNIMED",          "C67","1.130,00","28/02/2026","UNIMED"],
# --- SCP (C68) 33.900,00 ---
["VIPMEDIC",                     "C68","33.900,00","20/04/2026","PARTICULAR"],
]

INADIMPLENTES = [[r[0], u(r[1]), r[2], r[3], r[4]] for r in INADIMPLENTES_RAW]

INAD_UNIDADE = {
    "Traumato": {"total": 761092.72, "count": 55},
    "RS":       {"total": 152676.50,  "count": 10},
    "SP":       {"total": 124527.00,  "count": 8},
    "SC":       {"total": 23540.00,  "count": 5},
    "PR":       {"total": 87400,   "count": 3},
    "BA":       {"total": 33900.00,   "count": 2},
    "Holep":    {"total": 7500.00,   "count": 1}
}

# Override com dados frescos do bi_data.json
if _bi.get("inadimplentes"):
    for _un, _val in _bi["inadimplentes"].items():
        _key = UNIT_MAP.get(str(_un).upper(), _un)
        if _key in INAD_UNIDADE:
            INAD_UNIDADE[_key]["total"] = round(_val, 2)
        else:
            INAD_UNIDADE[_key] = {"total": round(_val, 2), "count": 1}
    _inad_total_new = sum(v['total'] for v in INAD_UNIDADE.values())
    print(f"[AUTO] INAD atualizado do bi_data.json — total: R${_inad_total_new:,.2f}")

INAD_GRAND_TOTAL = sum(v["total"] for v in INAD_UNIDADE.values())

# Override direto com total do BI se disponível
if _bi.get("inadimplencia_total"):
    INAD_GRAND_TOTAL = round(_bi["inadimplencia_total"], 2)
    print(f"[AUTO] INAD_GRAND_TOTAL via bi_data.json: R${INAD_GRAND_TOTAL:,.2f}")

# Ciclo financeiro — cirurgia → nota e cirurgia → recebimento
_ciclo        = _bi.get("ciclo_financeiro", {})
_ciclo_nota   = _ciclo.get("cir_nota",        {"media": 24.5, "n": 15840})
_ciclo_receb  = _ciclo.get("cir_recebimento", {"media": 68.4, "n": 15840})
_ciclo_por_un = _ciclo.get("por_un", {})
_ciclo_ref    = _ciclo.get("ref", "2026 Jan-Jun")
# Último dia do mês anterior (corte do ciclo financeiro)
import calendar as _cal
_hoje_dt  = __import__("datetime").date.today()
_mes_ant  = (_hoje_dt.replace(day=1) - __import__("datetime").timedelta(days=1))
_ciclo_ate = _mes_ant.strftime("%d/%m/%Y")  # ex: "31/05/2026"

# Reference despesas (proportional base)
DESP_AD_REF = [
{"ad":"COMPRAS REVENDA","val":681315.91,"top":[
    ["COLOPLAST",446677.96,"MATERIAL P/ REVENDA"],
    ["COLOPLAST NAVEGANTES",107354.8,"MATERIAL P/ REVENDA"],
    ["LEVMEDICAL",22624.67,"MATERIAL P/ REVENDA"],
    ["SYMATESE",20073.64,"MATERIAL P/ REVENDA"],
    ["NEXTIMPLANTES RIO DE JANEIRO",13244.83,"MATERIAL P/ REVENDA"],
    ["RAZEK LTDA",12196.62,"MATERIAL P/ REVENDA"],
    ["LABCOR",12191.0,"MATERIAL P/ REVENDA"],
    ["MG OSTEO PHARMA",9949.34,"MATERIAL P/ REVENDA"],
    ["MSB BRASIL",6512.03,"MATERIAL P/ REVENDA"],
    ["STEEL SURGICAL",4829.28,"MATERIAL P/ REVENDA"],
    ["NEXXMED EQUIPAMENTOS",4633.33,"MATERIAL P/ REVENDA"],
    ["VICTORIA PRODUTOS HOSPITALARES",3580.0,"MATERIAL P/ REVENDA"],
    ["EIC BRASIL",3425.0,"MATERIAL P/ REVENDA"],
    ["BRAMSYS",3075.17,"MATERIAL P/ REVENDA"],
    ["OPERANDI",2666.72,"MATERIAL P/ REVENDA"],
    ["R3A MEDICAL",2141.4,"MATERIAL P/ REVENDA"],
    ["ENDOTECH COMERCIO",2040.0,"MATERIAL P/ REVENDA"],
    ["VOLMED ATACADO",1479.12,"MATERIAL P/ REVENDA"],
    ["ENDO INDUSTRIA",1411.0,"MATERIAL P/ REVENDA"],
    ["MEDHCIR",1210.0,"MATERIAL P/ REVENDA"],
]},
{"ad":"OPERACIONAL","val":624126.35,"top":[
    ["LUCAS PRAETORIUS",247400.0,"PRESTADORES DE SERVIÇO"],
    ["SANDRO DE OLIVEIRA VIANA",14000.0,"PRESTADORES DE SERVIÇO"],
    ["SQUADRA TRANSPORTE",12882.68,"PRESTADORES DE SERVIÇO"],
    ["ATM SERVICOS CONTABEIS S.S.",6748.45,"PRESTADORES DE SERVIÇO"],
    ["HR CONSULTORIA EMPRESARIAL",5920.0,"PRESTADORES DE SERVIÇO"],
    ["MANOEL",5000.0,"PRESTADORES DE SERVIÇO"],
    ["DUTRA ADVOGADOS",4931.44,"PRESTADORES DE SERVIÇO"],
    ["EMULTEC",4930.0,"PRESTADORES DE SERVIÇO"],
    ["SINERGYMED",4900.0,"PRESTADORES DE SERVIÇO"],
    ["LANES LEVY",2720.97,"PRESTADORES DE SERVIÇO"],
    ["BIONEXO S A",2629.33,"PRESTADORES DE SERVIÇO"],
    ["ML BIDDING",2500.0,"PRESTADORES DE SERVIÇO"],
    ["ENDOLOG",2500.0,"PRESTADORES DE SERVIÇO"],
    ["TANARA SCHEIN",2200.0,"PRESTADORES DE SERVIÇO"],
    ["ELLEVAR PLATAFORMA FURGAO",2137.5,"PRESTADORES DE SERVIÇO"],
    ["PRO RAD C E R S S",1835.71,"PRESTADORES DE SERVIÇO"],
    ["NLS GRAFICA LTDA",1800.0,"PRESTADORES DE SERVIÇO"],
    ["QUBO - KLEOS",1735.49,"PRESTADORES DE SERVIÇO"],
    ["CHECK 4 DATA",1532.23,"PRESTADORES DE SERVIÇO"],
    ["SND DISTRIBUICAO",1525.98,"PRESTADORES DE SERVIÇO"],
    ["CHECKMOB DIGITAL",1139.9,"PRESTADORES DE SERVIÇO"],
    ["LINX SISTEMAS",1071.56,"PRESTADORES DE SERVIÇO"],
    ["ESTERILIZARE",1013.5,"PRESTADORES DE SERVIÇO"],
    ["MARCELO CIOATO COSTA",1000.0,"PRESTADORES DE SERVIÇO"],
    ["OXISUL ACTION PLANE",930.0,"PRESTADORES DE SERVIÇO"],
    ["ESPRESSO APP CARTAO",624.0,"PRESTADORES DE SERVIÇO"],
    ["LPCLE INFORMATICA",612.91,"PRESTADORES DE SERVIÇO"],
    ["CENTRO CLINICO GAUCHO",576.84,"PRESTADORES DE SERVIÇO"],
    ["B.I. INPART SERVICOS",508.93,"PRESTADORES DE SERVIÇO"],
    ["LILIANE (SEC. LIVIA)",500.0,"PRESTADORES DE SERVIÇO"],
    ["CENTRAL STORAGE SELF STOR",401.44,"PRESTADORES DE SERVIÇO"],
    ["GPS 77",270.0,"PRESTADORES DE SERVIÇO"],
    ["MEDICAL VIRTUAL MARKET",208.69,"PRESTADORES DE SERVIÇO"],
    ["ATM SERVICOS CONTABEIS",200.0,"PRESTADORES DE SERVIÇO"],
    ["J. F. MARTINS DA SILVA",150.0,"PRESTADORES DE SERVIÇO"],
    ["AHGORA SISTEMAS",119.7,"PRESTADORES DE SERVIÇO"],
    ["ECO AMBIENTALIS",110.0,"PRESTADORES DE SERVIÇO"],
    ["JAQUELINE WITT DA SILVA",66.0,"PRESTADORES DE SERVIÇO"],
    ["GOL LINHAS AEREAS S.A.",30447.7,"FRETE"],
    ["STRATEGICA EM TRANSPORTES",5523.02,"FRETE"],
    ["EXPRESSO SAO MIGUEL LTDA",3289.0,"FRETE"],
    ["FULL EXPRESS TRANSPORTES",1797.94,"FRETE"],
    ["FREE FRETE - GUILHERME MICOS",1055.0,"FRETE"],
    ["CORREIOS",338.13,"FRETE"],
    ["LOGMED RIO ARMAZENAGEM",322.53,"FRETE"],
    ["EXPRESSO SAO MIGUEL SA",239.0,"FRETE"],
    ["TRANSMED",183.91,"FRETE"],
    ["EXPRESSA LOGISTICA",94.07,"FRETE"],
    ["INACIO MONCKS",66.0,"FRETE"],
    ["KAMILA DE CASTILHO",47.96,"FRETE"],
    ["FINANCIAMENTO FINAME",33799.36,"FINANCIAMENTO"],
    ["STELLANTIS FINANCIAMENTO SC",7014.14,"FINANCIAMENTO"],
    ["DR VITA - RLVN",9201.0,"EVENTO"],
    ["SOCIEDADE BRASILEIRA DE UROLOGIA",5880.0,"EVENTO"],
    ["INACIO MONCKS",5613.85,"EVENTO"],
    ["PALESTRA DR FABIO SANTANNA",5000.0,"EVENTO"],
    ["LUCAS PRAETORIUS",4494.1,"EVENTO"],
    ["PROGRAMA BOCA NO TRAMBONE",3500.0,"EVENTO"],
    ["ALIDA CONFEITARIA",1650.0,"EVENTO"],
    ["LUCAS LAMPERT",1480.0,"EVENTO"],
    ["DR PEDRO VICTOR",844.7,"EVENTO"],
    ["DR GABRIEL HELUANY",332.47,"EVENTO"],
    ["DR AUREO DUARTE",332.47,"EVENTO"],
    ["DR SANDER",226.54,"EVENTO"],
    ["DR PEDRO",226.54,"EVENTO"],
    ["COLOPLAST",6434.85,"MKT"],
    ["AGENCIA HEFESTO",5000.0,"MKT"],
    ["RG PULSE",4000.0,"MKT"],
    ["V4 COMPANY",3900.0,"MKT"],
    ["LARISSA DA MOTTA BROSE",2900.0,"MKT"],
    ["FACEBOOK",2149.52,"MKT"],
    ["PULSEBRAND",947.0,"MKT"],
    ["WEB IN SIDE",623.33,"MKT"],
    ["MATEUS MACHADO OSORIO",350.0,"MKT"],
    ["GOOGLE BRASIL",300.0,"MKT"],
    ["ENDO INDUSTRIA",12000.0,"ALUGUEL DE EQUIPAMEN"],
    ["ADILSON CORTINES LAXE - MEDLASER",4500.0,"ALUGUEL DE EQUIPAMEN"],
    ["GLOBAL LASER",3000.0,"ALUGUEL DE EQUIPAMEN"],
    ["LASERMED",3000.0,"ALUGUEL DE EQUIPAMEN"],
    ["NOVELTY",3000.0,"ALUGUEL DE EQUIPAMEN"],
    ["FREE - PRECISION SURGICAL",2200.0,"FREELANCER CIRURGIA"],
    ["FREE - VITORIA BREMM BACK",2100.0,"FREELANCER CIRURGIA"],
    ["LARISSA MACIEL MONKS",2099.03,"FREELANCER CIRURGIA"],
    ["TATIANA NUNES ROSA",1854.0,"FREELANCER CIRURGIA"],
    ["MIGUEL",1800.0,"FREELANCER CIRURGIA"],
    ["MARIA FABIANE MARTINI",1780.0,"FREELANCER CIRURGIA"],
    ["FREE - GABRIEL ALVES SORREICAO",1710.0,"FREELANCER CIRURGIA"],
    ["MARCELO CIOATO COSTA",1250.0,"FREELANCER CIRURGIA"],
    ["JEFERSON NEVES CANTO",850.0,"FREELANCER CIRURGIA"],
    ["EDUARDO MACHADO DA SILVEIRA",750.0,"FREELANCER CIRURGIA"],
    ["VERIDIANE BARCELOS MACHADO",600.0,"FREELANCER CIRURGIA"],
    ["SUANE PEREIRA SILVEIRA",300.0,"FREELANCER CIRURGIA"],
    ["VERIDIANE",300.0,"FREELANCER CIRURGIA"],
    ["ANDERSON ROGER CUSTODIO",290.0,"FREELANCER CIRURGIA"],
    ["VIVIANE DE MOURA DE OLIVEIRA",150.0,"FREELANCER CIRURGIA"],
    ["WF ADMINISTRADORA DE IMOVEIS",7044.83,"ALUGUEL"],
    ["LUCAS PRAETORIUS",3000.0,"ALUGUEL"],
    ["MIGUEL",1768.62,"COMBUSTIVEL"],
    ["RAFAEL - RFS FREITAS LTDA",1086.01,"COMBUSTIVEL"],
    ["KAMILA DE CASTILHO",1003.68,"COMBUSTIVEL"],
    ["RENATO",1000.0,"COMBUSTIVEL"],
    ["RODOLPHO FALCIANO FILHO",787.15,"COMBUSTIVEL"],
    ["GUILHERME CARVALHO",696.12,"COMBUSTIVEL"],
    ["LUCAS PRAETORIUS",428.4,"COMBUSTIVEL"],
    ["EDUARDO MACHADO DA SILVEIRA",400.0,"COMBUSTIVEL"],
    ["JEFERSON NEVES CANTO",394.7,"COMBUSTIVEL"],
    ["INACIO MONCKS",373.01,"COMBUSTIVEL"],
    ["NS ASSESSORIA TECNICA",356.72,"COMBUSTIVEL"],
    ["FVEGA REPRESENTACOES",311.42,"COMBUSTIVEL"],
    ["MATHEUS VIALE",236.76,"COMBUSTIVEL"],
    ["MONTEGGIA SOLUCOES",6277.5,"MANUTENÇÃO GERAL"],
    ["INACIO MONCKS",1178.0,"MANUTENÇÃO GERAL"],
    ["SCIENCETECH SISTEMAS",725.0,"MANUTENÇÃO GERAL"],
    ["EDUARDO MACHADO DA SILVEIRA",300.0,"MANUTENÇÃO GERAL"],
    ["WILSON PEREIRA",100.0,"MANUTENÇÃO GERAL"],
    ["CIMAFER",29.9,"MANUTENÇÃO GERAL"],
    ["INACIO MONCKS",7000.0,"ADVOGADO"],
    ["FVEGA REPRESENTACOES",937.5,"ESTACIONAMENTO"],
    ["JEFERSON NEVES CANTO",817.0,"ESTACIONAMENTO"],
    ["RODOLPHO FALCIANO FILHO",729.0,"ESTACIONAMENTO"],
    ["RAFAEL - RFS FREITAS LTDA",610.5,"ESTACIONAMENTO"],
    ["INACIO MONCKS",585.0,"ESTACIONAMENTO"],
    ["MIGUEL",568.9,"ESTACIONAMENTO"],
    ["WILSONEI PEREIRA DOS SANTOS",533.5,"ESTACIONAMENTO"],
    ["MARCELO CIOATO COSTA",424.0,"ESTACIONAMENTO"],
    ["NS ASSESSORIA TECNICA",408.96,"ESTACIONAMENTO"],
    ["TATA PARK MOINHOS",350.0,"ESTACIONAMENTO"],
    ["MARCOS ROGERIO VERDURA",210.5,"ESTACIONAMENTO"],
    ["VALE PARKING",210.0,"ESTACIONAMENTO"],
    ["KAMILA DE CASTILHO",106.5,"ESTACIONAMENTO"],
    ["GUILHERME CARVALHO",60.0,"ESTACIONAMENTO"],
    ["PEDRO BITENCOURT",60.0,"ESTACIONAMENTO"],
    ["MATHEUS VIALE",55.0,"ESTACIONAMENTO"],
    ["JEFERSON",15.0,"ESTACIONAMENTO"],
    ["SEFAZ SP",5391.42,"DIFAL"],
    ["GNRE - SEFAZ RJ",360.93,"DIFAL"],
    ["SEFAZ RO",147.02,"DIFAL"],
    ["SUANE PEREIRA SILVEIRA",1409.69,"UBER"],
    ["SANDRO DE OLIVEIRA VIANA",966.32,"UBER"],
    ["INACIO MONCKS",736.78,"UBER"],
    ["MIGUEL",519.06,"UBER"],
    ["LUCAS PRAETORIUS",435.75,"UBER"],
    ["RODOLPHO FALCIANO FILHO",413.94,"UBER"],
    ["WILSONEI PEREIRA DOS SANTOS",150.36,"UBER"],
    ["ARAMIS DA SILVA NOGUEIRA",15.95,"UBER"],
    ["GABRIELA TRILHA",9.96,"UBER"],
    ["EDUARDO MACHADO DA SILVEIRA",1590.9,"KM RODADO"],
    ["JEFERSON NEVES CANTO",1090.05,"KM RODADO"],
    ["VERIDIANE BARCELOS MACHADO",1036.95,"KM RODADO"],
    ["WILSONEI PEREIRA DOS SANTOS",364.65,"KM RODADO"],
    ["MATHEUS VIALE",115.35,"KM RODADO"],
    ["SANDRO DE OLIVEIRA VIANA",1498.0,"HOSPEDAGEM"],
    ["INACIO MONCKS",811.77,"HOSPEDAGEM"],
    ["KAMILA DE CASTILHO",594.23,"HOSPEDAGEM"],
    ["EDUARDO MACHADO DA SILVEIRA",400.0,"HOSPEDAGEM"],
    ["FVEGA REPRESENTACOES",382.8,"HOSPEDAGEM"],
    ["JEFERSON NEVES CANTO",266.77,"HOSPEDAGEM"],
    ["MARCOS ROGERIO VERDURA",240.79,"HOSPEDAGEM"],
    ["CRF",4131.69,"CONSELHO DE FARMACIA"],
    ["ITAU",2706.8,"TARIFA BANCARIAS"],
    ["SANTANDER",493.17,"TARIFA BANCARIAS"],
    ["BANCO DO BRASIL",188.8,"TARIFA BANCARIAS"],
    ["BB",171.93,"TARIFA BANCARIAS"],
    ["MIGUEL",1950.01,"TREINAMENTO"],
    ["LUCAS PRAETORIUS",465.68,"TREINAMENTO"],
    ["GABRIEL VEBER MOISES DA SILVA",465.68,"TREINAMENTO"],
    ["GABRIELA TRILHA",465.68,"TREINAMENTO"],
    ["MATHEUS VIALE",1416.0,"MATERIAL DE ESCRITOR"],
    ["LUIS INACIO",1056.54,"MATERIAL DE ESCRITOR"],
    ["WILSONEI PEREIRA DOS SANTOS",280.66,"MATERIAL DE ESCRITOR"],
    ["MARCELO CIOATO COSTA",138.25,"MATERIAL DE ESCRITOR"],
    ["GABRIELA TRILHA",122.44,"MATERIAL DE ESCRITOR"],
    ["GUILHERME CARVALHO",60.0,"MATERIAL DE ESCRITOR"],
    ["SUANE PEREIRA SILVEIRA",47.96,"MATERIAL DE ESCRITOR"],
    ["SABRINA DA SILVA HIRT",25.0,"MATERIAL DE ESCRITOR"],
    ["LUHEN CUNHA MACIEL",5.5,"MATERIAL DE ESCRITOR"],
    ["LUCAS PRAETORIUS",1900.0,"BRINDE"],
    ["FVEGA REPRESENTACOES",292.12,"BRINDE"],
    ["WILSONEI PEREIRA DOS SANTOS",228.5,"BRINDE"],
    ["RAFAEL - RFS FREITAS LTDA",27.0,"BRINDE"],
    ["LUCAS PRAETORIUS",1049.74,"PASSAGEM"],
    ["SANDRO DE OLIVEIRA VIANA",731.37,"PASSAGEM"],
    ["KAMILA DE CASTILHO",374.3,"PASSAGEM"],
    ["LARISSA MACIEL MONKS",278.92,"PASSAGEM"],
    ["LUCAS GRACA ARANHA DE OLIVEIRA",2249.81,"PRECEPTORIA"],
    ["VIVO - MOVEL",1712.59,"TELEFONIA MOVEL"],
    ["CLARO - NET",75.98,"TELEFONIA MOVEL"],
    ["GABRIELA TRILHA",60.0,"TELEFONIA MOVEL"],
    ["FAXINA - TERESINHA LIMA BRUTIS",1800.0,"FAXINA"],
    ["CEEE",1706.64,"ENERGIA"],
    ["LTZ PERFORMANCE",1320.9,"FURGAO-MANUTENCAO"],
    ["RAFAEL - RFS FREITAS LTDA",493.0,"SEM PARAR"],
    ["CAMINHOS DA SERRA GAUCHA",194.55,"SEM PARAR"],
    ["FVEGA REPRESENTACOES",65.0,"SEM PARAR"],
    ["MIGUEL",40.0,"SEM PARAR"],
    ["RODOLPHO FALCIANO FILHO",38.7,"SEM PARAR"],
    ["CONFIANCA SERVICOS",600.0,"DEDETIZAÇÃO"],
    ["BRADESCO SEGURO AUTO",568.23,"SEGURO"],
    ["PONTUAL TELECOM",289.0,"INTERNET"],
    ["UNIFIQUE",187.86,"INTERNET"],
    ["RAFAEL - RFS FREITAS LTDA",254.99,"REEMBOLSO"],
    ["RODOLPHO FALCIANO FILHO",135.79,"REEMBOLSO"],
    ["SUANE PEREIRA SILVEIRA",46.67,"REEMBOLSO"],
    ["WILSONEI PEREIRA DOS SANTOS",20.91,"REEMBOLSO"],
    ["ADAN AMBIENTAL",374.0,"AGUA"],
    ["GABRIELA TRILHA",93.31,"MATERIAL GERAL (LIMP)"],
    ["JUNTA COMERCIAL",65.65,"TAXAS E LICENÇAS"],
    ["LUCAS PRAETORIUS",30.0,"EVENTOS INTERNOS"],
    ["INACIO MONCKS",30.0,"EVENTOS INTERNOS"],
]},
{"ad":"IMPORTACAO","val":287725.33,"top":[
    ["TELEFLEX LLC",267372.0,"IMPORTAÇÃO"],
    ["ACK ACCESS",20248.16,"IMPORTAÇÃO"],
    ["BERKLEY INTERNATIONAL",105.17,"IMPORTAÇÃO"],
]},
{"ad":"SALARIO","val":192693.58,"top":[
    ["RODOLPHO FALCIANO FILHO",13000.0,"REPRESENTANTE (PJ)"],
    ["FVEGA REPRESENTACOES",11951.81,"REPRESENTANTE (PJ)"],
    ["KAMILA DE CASTILHO",9773.32,"REPRESENTANTE (PJ)"],
    ["NS ASSESSORIA TECNICA",8000.0,"REPRESENTANTE (PJ)"],
    ["RAFAEL - RFS FREITAS LTDA",6250.0,"REPRESENTANTE (PJ)"],
    ["JOSELI STELLA",5500.0,"REPRESENTANTE (PJ)"],
    ["MARCOS ROGERIO VERDURA",4480.1,"REPRESENTANTE (PJ)"],
    ["ALINE GAMA",3950.0,"REPRESENTANTE (PJ)"],
    ["EVANDRO BIOVITAL",2000.0,"REPRESENTANTE (PJ)"],
    ["ELISSANDRA",1500.0,"REPRESENTANTE (PJ)"],
    ["FABIANA FLECK",1500.0,"REPRESENTANTE (PJ)"],
    ["JS FARMA",1000.0,"REPRESENTANTE (PJ)"],
    ["GABRIELA TRILHA",5544.21,"SALARIO"],
    ["JEFERSON NEVES CANTO",4685.79,"SALARIO"],
    ["WILSONEI PEREIRA DOS SANTOS",4643.3,"SALARIO"],
    ["TANARA",4500.0,"SALARIO"],
    ["EDUARDO MACHADO DA SILVEIRA",4312.71,"SALARIO"],
    ["VERIDIANE BARCELOS MACHADO",4297.33,"SALARIO"],
    ["GUILHERME CARVALHO",3204.61,"SALARIO"],
    ["SUANE PEREIRA SILVEIRA",3143.44,"SALARIO"],
    ["MATHEUS VIALE",2973.07,"SALARIO"],
    ["PEDRO BITENCOURT",2798.49,"SALARIO"],
    ["SABRINA DA SILVA HIRT",2715.0,"SALARIO"],
    ["NADIA SANTANA TAROUCO",2614.57,"SALARIO"],
    ["CAROLINA BORBA",2324.93,"SALARIO"],
    ["MARIA MOTA CABELEIRA",2089.48,"SALARIO"],
    ["ARAMIS DA SILVA NOGUEIRA",1810.19,"SALARIO"],
    ["LUHEN CUNHA MACIEL",1761.41,"SALARIO"],
    ["ARTUR HATZEN",802.75,"SALARIO"],
    ["CIEE - APRENDIZ",381.14,"SALARIO"],
    ["FLASH APP",13946.0,"ALIMENTAÇÃO"],
    ["LUCAS PRAETORIUS",4417.82,"ALIMENTAÇÃO"],
    ["MIGUEL",2320.73,"ALIMENTAÇÃO"],
    ["INACIO MONCKS",2207.12,"ALIMENTAÇÃO"],
    ["PLUXEE BENEFICIOS",836.0,"ALIMENTAÇÃO"],
    ["FVEGA REPRESENTACOES",796.77,"ALIMENTAÇÃO"],
    ["RODOLPHO FALCIANO FILHO",607.19,"ALIMENTAÇÃO"],
    ["WILSONEI PEREIRA DOS SANTOS",555.85,"ALIMENTAÇÃO"],
    ["RAFAEL - RFS FREITAS LTDA",187.09,"ALIMENTAÇÃO"],
    ["SANDRO DE OLIVEIRA VIANA",164.3,"ALIMENTAÇÃO"],
    ["JEFERSON NEVES CANTO",84.0,"ALIMENTAÇÃO"],
    ["GABRIELA TRILHA",83.8,"ALIMENTAÇÃO"],
    ["NS ASSESSORIA TECNICA",60.0,"ALIMENTAÇÃO"],
    ["BRADESCO SAUDE",17145.48,"PLANO DE SAUDE"],
    ["BRADESCO SAUDE SA",4351.99,"PLANO DE SAUDE"],
    ["BRADESCO SAUDE - FERNANDO",2148.95,"PLANO DE SAUDE"],
    ["BRADESCO - ODONTO",544.5,"PLANO DE SAUDE"],
    ["BRADESCO ODONTO",54.45,"PLANO DE SAUDE"],
    ["BRADESCO ODONTO - FERNANDO",54.45,"PLANO DE SAUDE"],
    ["BRADESCO ODONTO - KAMILA",36.3,"PLANO DE SAUDE"],
    ["IMPOSTOS - FGTS",6311.7,"FGTS"],
    ["FLASH APP",5113.4,"VALE TRANSPORTE"],
    ["CTG PRESTADORES",1500.0,"C.S"],
    ["NSTM PRESTADORES",1500.0,"C.S"],
    ["SINERGYMED",1614.5,"COMISSÃO"],
    ["EDUARDO MACHADO DA SILVEIRA",320.0,"COMISSÃO"],
    ["SUANE PEREIRA SILVEIRA",300.0,"COMISSÃO"],
    ["VERIDIANE BARCELOS MACHADO",80.0,"COMISSÃO"],
    ["WILSONEI PEREIRA DOS SANTOS",1343.54,"SALARIO - JUDICIAIS"],
    ["VERIDIANE BARCELOS MACHADO",500.0,"IAE"],
]},
{"ad":"IMPOSTO","val":100139.48,"top":[
    ["IMPOSTOS - COFINS",53303.54,"COFINS"],
    ["IMPOSTOS - INSS",24907.67,"INSS"],
    ["IMPOSTOS - PIS",11549.09,"PIS"],
    ["PREFEITURA MUNICIPAL DE POA",7262.71,"IPTU"],
    ["RODOLPHO FALCIANO FILHO",2403.97,"IMPOSTO"],
    ["IMPOSTOS - ISS",712.5,"ISSQN"],
]},
{"ad":"PRO LABORE","val":78635.53,"top":[
    ["LUCAS PRAETORIUS",30000.0,"RETIRADA PL"],
    ["INACIO MONCKS",30000.0,"RETIRADA PL"],
    ["MIGUEL",17500.0,"RETIRADA PL"],
    ["LUCAS PRAETORIUS",620.9,"PRO LABORE"],
    ["INACIO MONCKS",514.63,"PRO LABORE"],
]},
{"ad":"USO/CONSUMO","val":45722.37,"top":[
    ["ENDOTECH COMERCIO",14490.79,"COMPRA EQUIPAMENTO"],
    ["SET DE VIDEO - AA STORE",8189.02,"COMPRA EQUIPAMENTO"],
    ["MEDHCIR",1833.15,"COMPRA EQUIPAMENTO"],
    ["WILSONEI PEREIRA DOS SANTOS",169.41,"COMPRA EQUIPAMENTO"],
    ["DEUTSCHLINE MEDICAL LTDA",21040.0,"COMPRA LASER"],
]},
{"ad":"NAO INDICADO","val":8487.6,"top":[
    ["CUSTOM SPINE",8487.6,"NAO INDICADO"],
]},
{"ad":"MANUTENÇÃO","val":7550.0,"top":[
    ["ENDO AMERICAS PRODUTOS",4550.0,"MAN. EQUIP_FLEX"],
    ["ENDO REPAROS",3000.0,"MAN. EQUIP_FLEX"],
]},
{"ad":"PREDIAL","val":7203.39,"top":[
    ["CORTE REALIMOVEIS",4293.49,"CONDOMINIO"],
    ["GARANTE BLU",2909.9,"CONDOMINIO"],
]},
{"ad":"COMPRAS ATIVO","val":4957.24,"top":[
    ["GABRIELA TRILHA",4957.24,"COMPRA ATIVO"],
]},
{"ad":"COMPRA DE INSTRUMENTAL","val":4064.0,"top":[
    ["COLOPLAST",2250.0,"COMPRA DE INSTRUMENTAL"],
    ["ENDOTECH COMERCIO",1814.0,"COMPRA DE INSTRUMENTAL"],
]},
{"ad":"SPEED ATIVA","val":1390.46,"top":[
    ["LARISSA MACIEL MONKS",1137.46,"SPEED ATIVA"],
    ["TATIANA NUNES ROSA",253.0,"SPEED ATIVA"],
]},
]
# Real per-period despesas by category (from BI dashboard/51 DRE table)
DESP_AD_VALS = {
    "mar26": {
        "COMPRAS REVENDA":681315.91,"OPERACIONAL":625522.75,"IMPORTACAO":287725.33,
        "SALARIO":192693.58,"IMPOSTO":100139.48,"PRO LABORE":78635.53,
        "USO/CONSUMO":46634.80,"NAO INDICADO":0.0,"MANUTENÇÃO":7550.00,
        "PREDIAL":8022.98,"COMPRAS ATIVO":5526.24,"COMPRA DE INSTRUMENTAL":4064.00,
        "SPEED ATIVA":1390.46,"RETIRADA":0.0,
    },
    "abr26": {
        "COMPRAS REVENDA":701092.74,"OPERACIONAL":671488.36,"IMPORTACAO":49960.00,
        "SALARIO":243842.63,"IMPOSTO":409975.77,"PRO LABORE":18333.01,
        "USO/CONSUMO":52740.27,"NAO INDICADO":8487.60,"MANUTENÇÃO":71666.23,
        "PREDIAL":6779.06,"COMPRAS ATIVO":9998.70,"COMPRA DE INSTRUMENTAL":10551.31,
        "SPEED ATIVA":0.0,"RETIRADA":150000.00,
    },
    "jun26": {
        "COMPRAS REVENDA":55959.0,
        "OPERACIONAL":75135.55,
        "IMPORTACAO":21.62,
        "SALARIO":11565.65,
        "IMPOSTO":5326.7,
        "PRO LABORE":14998.65,
        "USO/CONSUMO":5803.78,
        "NAO INDICADO":0.0,
        "MANUTENÇÃO":3636.45,
        "PREDIAL":740.65,
        "COMPRAS ATIVO":218.8,
        "COMPRA DE INSTRUMENTAL":1402.72,
        "SPEED ATIVA":89.45,
        "RETIRADA":0.0,
    },
    "mai26": {
        "COMPRAS REVENDA":513003.56,"OPERACIONAL":688804.38,"IMPORTACAO":198.17,
        "SALARIO":106027.95,"IMPOSTO":48832.50,"PRO LABORE":137500.00,
        "USO/CONSUMO":53206.06,"NAO INDICADO":0.0,"MANUTENÇÃO":33337.08,
        "PREDIAL":6789.88,"COMPRAS ATIVO":2005.83,"COMPRA DE INSTRUMENTAL":12859.40,
        "SPEED ATIVA":820.00,"RETIRADA":0.0,
    },
}
DESP_AD_VALS["1t26"] = {k: round(sum(DESP_AD_VALS[p].get(k,0) for p in ["mar26","abr26","mai26"]),2)
                        for k in DESP_AD_VALS["mar26"]}

REF_DESP_TOTAL = sum(d["val"] for d in DESP_AD_REF)

def scale_desp_ad(ref_list, target_total):
    """Kept for fallback; use get_desp_ad_period for real per-period values."""
    factor = target_total / REF_DESP_TOTAL
    result = []
    for d in ref_list:
        nd = {"ad": d["ad"], "val": round(d["val"] * factor, 2), "top": []}
        for t in d["top"]:
            nd["top"].append([t[0], round(t[1] * factor, 2), t[2]])
        result.append(nd)
    return result

def get_desp_ad_period(period):
    """Return DESP_AD_REF with real per-period vals from DESP_AD_VALS."""
    vals = DESP_AD_VALS.get(period, DESP_AD_VALS["mai26"])
    ref_total = sum(d["val"] for d in DESP_AD_REF)
    result = []
    for d in DESP_AD_REF:
        real_val = vals.get(d["ad"], 0.0)
        # Scale top suppliers proportionally to real_val vs ref val
        factor = (real_val / d["val"]) if d["val"] > 0 else 0.0
        nd = {"ad": d["ad"], "val": round(real_val, 2), "top": []}
        for t in d["top"]:
            nd["top"].append([t[0], round(t[1] * factor, 2), t[2]])
        result.append(nd)
    return result

# Per-period faturamento — real byUN and byGrupo from BI
FAT_PERIODS = {
    "mar26": {
        "label": "Mar/26", "ini": "2026-03-01", "fim": "2026-03-31",
        "total": 2311749, "nf_count": 530, "prazo": 29,
        "byUN": [["RS",762356],["Traumato",534394],["Holep",359800],
                 ["SP",323589],["SC",180410],["PR",116900],["BA",34300]],
        "byGrupo": [
            {"g":"SAUDE DO HOMEM","val":641931,"cnt":52,"prods":[
                ["TITAN ESCROTAL 18CM",160000],["GENESIS 13MM",120000],
                ["TITAN INFRAPUBIC 18CM",95000],["RESERVATORIO OTR 125CC",72000],
                ["PERICARDIO BOVINO",45000]]},
            {"g":"TRAUMATOLOGIA","val":495932,"cnt":55,"prods":[
                ["LEVLIFE MR-BC",160000],["BLOCK SAFE 21X100",100000],
                ["BLOCK SAFE 21X120",85000],["ACCURE G.BLOCK",60000],["CANULA DISCECTOMIA",42000]]},
            {"g":"SERVICO","val":387180,"cnt":70,"prods":[]},
            {"g":"ENDOUROLOGIA","val":266784,"cnt":300,"prods":[]},
            {"g":"SPEEDICATH","val":187632,"cnt":35,"prods":[]},
            {"g":"UROLOGIA GERAL","val":166254,"cnt":35,"prods":[]},
            {"g":"RTU","val":42178,"cnt":18,"prods":[]},
            {"g":"UROLIFT","val":39000,"cnt":2,"prods":[]},
            {"g":"FIBRAS LASER - CONSUMO","val":34496,"cnt":20,"prods":[]},
            {"g":"CRIOANALGESIA","val":17200,"cnt":3,"prods":[]},
            {"g":"ACETABULAR","val":14717,"cnt":2,"prods":[]},
            {"g":"HOLEP","val":11900,"cnt":1,"prods":[]},
            {"g":"HASTE FEMORAL (ATQ)","val":6545,"cnt":1,"prods":[]},
        ]
    },
    "abr26": {
        "label": "Abr/26", "ini": "2026-04-01", "fim": "2026-04-30",
        "total": 2601247, "nf_count": 495, "prazo": 30,
        "byUN": [["RS",1099605],["Traumato",533192],["SP",292140],
                 ["Holep",270250],["SC",176310],["PR",171850],["BA",57900]],
        "byGrupo": [
            {"g":"SAUDE DO HOMEM","val":785705,"cnt":37,"prods":[
                ["TITAN INFRAPUBIC 22CM",105000],["GENESIS 13MM",98000],
                ["TITAN ESCROTAL 16CM",85000],["GENESIS 11MM",82000],
                ["TITAN ESCROTAL 20CM",70000]]},
            {"g":"TRAUMATOLOGIA","val":550392,"cnt":31,"prods":[
                ["LEVLIFE MR-BC",210000],["BLOCK SAFE 21X100",90000],
                ["BLOCK SAFE 21X120",75000],["ACCURE G.BLOCK",50000],
                ["ELETRODO ABLACAO",30000]]},
            {"g":"ENDOUROLOGIA","val":374415,"cnt":310,"prods":[]},
            {"g":"SERVICO","val":325580,"cnt":61,"prods":[]},
            {"g":"SPEEDICATH","val":254700,"cnt":25,"prods":[
                ["MASC CH12",102000],["FEMI CH12",60000],["FEMI CH10",51500],
                ["NAVI MASC CH12",31700],["FEMI CH08",9500]]},
            {"g":"UROLOGIA GERAL","val":133804,"cnt":16,"prods":[]},
            {"g":"UROLIFT","val":90700,"cnt":3,"prods":[]},
            {"g":"RTU","val":49184,"cnt":16,"prods":[]},
            {"g":"FIBRAS LASER - CONSUMO","val":30466,"cnt":13,"prods":[]},
            {"g":"MATRIZ DERMICA","val":23500,"cnt":2,"prods":[]},
        ]
    },
    "mai26": {
        "label": "Mai/26", "ini": "2026-05-01", "fim": "2026-05-31",
        "total": 3087631.28, "nf_count": 512, "prazo": 31,
        "byUN": [["RS",1101756],["Traumato",757383],["PR",426056],
                 ["SP",308368],["Holep",262250],["SC",197180],["BA",34638]],
        "byGrupo": [
            {"g":"SAUDE DO HOMEM","val":632488,"cnt":58,"prods":[
                ["TITAN ESCROTAL 18CM",222801],["GENESIS 13MM",80000],
                ["RESERVATORIO OTR 125CC",55000],["GENESIS 11MM",48000],
                ["TITAN ESCROTAL 20CM",42000]]},
            {"g":"TRAUMATOLOGIA","val":483613,"cnt":46,"prods":[
                ["LEVLIFE MR-BC",150500],["BLOCK SAFE 21X100",144400],
                ["CANULA DISCECTOMIA",41800],["FASTFIT ANCHOR",28493],
                ["ACCURE G.BLOCK",23700]]},
            {"g":"ENDOUROLOGIA","val":156340,"cnt":260,"prods":[]},
            {"g":"SERVICO","val":143586,"cnt":56,"prods":[]},
            {"g":"UROLOGIA GERAL","val":118144,"cnt":29,"prods":[]},
            {"g":"UROLIFT","val":86400,"cnt":3,"prods":[["KIT UROLIFT SISTEMA",86400]]},
            {"g":"SPEEDICATH","val":84402,"cnt":30,"prods":[]},
            {"g":"MATRIZ DERMICA","val":36760,"cnt":2,"prods":[["MATRIX HD DERMICA",36760]]},
            {"g":"RTU","val":25600,"cnt":10,"prods":[]},
            {"g":"FIBRAS LASER - CONSUMO","val":6775,"cnt":12,"prods":[]},
        ]
    },
    "jun26": {
        "label": "Jun/26", "ini": "2026-06-01", "fim": "2026-06-03",
        "total": 842555.51, "nf_count": 19, "prazo": 30,
        "parcial": True,
        "byUN": [["RS",30168],["Traumato",85100]],
        "byGrupo": [
            {"g":"CRIOANALGESIA","val":28500,"cnt":1,"prods":[]},
            {"g":"TRAUMATOLOGIA","val":85100,"cnt":8,"prods":[]},
        ]
    },
    "1t26": {
        "label": "1T/26", "ini": "2026-03-01", "fim": "2026-05-22",
        "total": 7637221.12, "nf_count": 1537, "prazo": 30,
        "byUN": [["RS",2686792],["Traumato",1741889],["PR",676306],
                 ["SP",924097],["Holep",892300],["SC",549000],["BA",166838]],
        "byGrupo": [
            {"g":"SAUDE DO HOMEM","val":2060124,"cnt":147,"prods":[]},
            {"g":"TRAUMATOLOGIA","val":1529937,"cnt":132,"prods":[]},
            {"g":"SERVICO","val":856346,"cnt":187,"prods":[]},
            {"g":"ENDOUROLOGIA","val":797539,"cnt":870,"prods":[]},
            {"g":"SPEEDICATH","val":526734,"cnt":87,"prods":[]},
            {"g":"UROLOGIA GERAL","val":418202,"cnt":80,"prods":[]},
            {"g":"UROLIFT","val":216100,"cnt":8,"prods":[]},
            {"g":"RTU","val":116962,"cnt":44,"prods":[]},
            {"g":"FIBRAS LASER - CONSUMO","val":71737,"cnt":45,"prods":[]},
            {"g":"MATRIZ DERMICA","val":60260,"cnt":4,"prods":[]},
            {"g":"CRIOANALGESIA","val":17200,"cnt":3,"prods":[]},
            {"g":"ACETABULAR","val":14717,"cnt":2,"prods":[]},
            {"g":"HOLEP","val":11900,"cnt":1,"prods":[]},
            {"g":"HASTE FEMORAL (ATQ)","val":6545,"cnt":1,"prods":[]},
        ]
    }
}

# Per-period despesas — real byUN + proportionally scaled byAd
DESP_PERIODS_RAW = {
    "mar26": {
        "label": "Mar/26", "total": 2039221,
        "byUN": [["RS",1420963],["Traumato",444321],["Holep",57756],
                 ["SP",51540],["PR",21537],["SC",14646],["BA",11515]]
    },
    "abr26": {
        "label": "Abr/26", "total": 2404916,
        "byUN": [["RS",1365065],["Traumato",501898],["SP",210735],
                 ["Holep",158109],["BA",60797],["PR",48276],["SC",47723]]
    },
    "mai26": {
        "label": "Mai/26", "total": 1135374.99,
        "byUN": [["RS",782930],["Traumato",440907],["Holep",164190],
                 ["SP",62990],["PR",32524],["BA",16598],["SC",13011]]
    },
    "jun26": {
        "label": "Jun/26", "total": 445691.80,
        "byUN": [["RS",143976],["Traumato",16371],["Holep",14552]]
    },
    "1t26": {
        "label": "1T/26", "total": 6083437,
        "byUN": [["RS",3569199],["Traumato",1250309],["Holep",373761],
                 ["SP",326265],["PR",102793],["BA",88088],["SC",72080]]
    }
}
DESP_PERIODS = {}
for k, v in DESP_PERIODS_RAW.items():
    DESP_PERIODS[k] = dict(v)
    DESP_PERIODS[k]["byAd"] = get_desp_ad_period(k)

# Faturamento clientes (mai26 - dados reais BI)
FAT_CLIENTES = [
{"c":"UNIMED POA","val":3558157,"items":[
    {"conv":"UNIMED POA","med":"LIVIA SILVA SMIDT","prod":"MATRIZ DERMICA 20X30CM NEVELIA","val":"211.500,00","uni":"RS"},
    {"conv":"UNIMED POA","med":"GABRIEL VEBER MOISES DA SILVA","prod":"PROTESE PENIANA INFLAVEL TITAN 20CM","val":"160.566,62","uni":"RS"},
    {"conv":"UNIMED POA","med":"EDUARDO GASTAL VIEIRA","prod":"CATETER DUPLO J VORTEK 7.0FR","val":"124.360,00","uni":"RS"},
    {"conv":"UNIMED POA","med":"GUSTAVO SCHROEDER","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"108.455,00","uni":"RS"}]},
{"c":"SANTA CASA - POA","val":1667872,"items":[
    {"conv":"PARTICULAR","med":"FELIPE PIONER MACHADO","prod":"SERVICO / LOCACAO","val":"233.000,00","uni":"Holep"},
    {"conv":"IPERGS","med":"BRUNO CHAO LISOT","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"113.565,21","uni":"RS"},
    {"conv":"PARTICULAR","med":"FABIO ANDRE DE AZEVEDO","prod":"SERVICO / LOCACAO","val":"88.900,00","uni":"Holep"},
    {"conv":"UNIMED POA","med":"GUSTAVO SCHROEDER","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"76.800,00","uni":"RS"}]},
{"c":"HOSPITAL REGINA","val":1400388,"items":[
    {"conv":"BRADESCO SAUDE","med":"LUIZ RICARDO BOTTON","prod":"LEVLIFE MR-BC - DOR CRONICA","val":"494.500,00","uni":"Traumato"},
    {"conv":"BRADESCO SAUDE","med":"JOEL C. WESTPHAL CORREA","prod":"LEVLIFE MR-BC - DOR CRONICA","val":"236.500,00","uni":"Traumato"},
    {"conv":"DOCTOR CLIN","med":"LUCAS LAMPERT","prod":"SERVICO / LOCACAO","val":"93.560,00","uni":"RS"},
    {"conv":"DOCTOR CLIN","med":"LUCAS LAMPERT","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"88.374,00","uni":"RS"}]},
{"c":"MOINHOS DE VENTO","val":1364202,"items":[
    {"conv":"CABERGS","med":"LIVIA SILVA SMIDT","prod":"MATRIZ DERMICA 20X30CM NEVELIA","val":"159.800,00","uni":"RS"},
    {"conv":"SAUDE PAS","med":"LIVIA SILVA SMIDT","prod":"SISTEMA ENXERTOS RIGENERA","val":"119.700,00","uni":"RS"},
    {"conv":"CABERGS","med":"LIVIA SILVA SMIDT","prod":"SISTEMA ENXERTOS RIGENERA","val":"110.700,00","uni":"RS"},
    {"conv":"BRADESCO SAUDE","med":"OTAVIO PEREIRA CADORE","prod":"BLOCK SAFE 21X120MM","val":"98.300,00","uni":"Traumato"}]},
{"c":"UNIMED VS","val":1153493,"items":[
    {"conv":"UNIMED VALE DO SINOS","med":"MARLON ROBERTO FIORENTINI","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"158.205,00","uni":"RS"},
    {"conv":"UNIMED VALE DO SINOS","med":"MARLON ROBERTO FIORENTINI","prod":"SERVICO / LOCACAO","val":"127.350,00","uni":"RS"},
    {"conv":"UNIMED VALE DO SINOS","med":"ELTON CARDOSO SANCHOTENE","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"101.490,00","uni":"RS"},
    {"conv":"UNIMED VALE DO SINOS","med":"ELTON CARDOSO SANCHOTENE","prod":"SERVICO / LOCACAO","val":"82.850,00","uni":"RS"}]},
{"c":"HOSPITAL MOINHOS DE VENTO","val":1124950,"items":[
    {"conv":"BRADESCO SAUDE","med":"ALESSANDRO J. PADILHA FENSTERSEIFER","prod":"LEVLIFE MR-BC - DOR CRONICA","val":"172.000,00","uni":"Traumato"},
    {"conv":"BRADESCO SAUDE","med":"LEANDRO EMMEL BECKER","prod":"KIT ACCURE G.BLOCK 120MM X 21G","val":"71.150,00","uni":"Traumato"},
    {"conv":"CASSI","med":"JARDEL PEREIRA TESSARI","prod":"FASTFIT ANCHOR RAZEK 2,5","val":"69.000,00","uni":"Traumato"},
    {"conv":"BRADESCO SAUDE","med":"JARDEL PEREIRA TESSARI","prod":"LEVLIFE MR-BC - DOR CRONICA","val":"64.500,00","uni":"Traumato"}]},
{"c":"HOSPITAL MAE DE DEUS","val":981990,"items":[
    {"conv":"IPERGS","med":"ALESSANDRO J. PADILHA FENSTERSEIFER","prod":"FASTFIT ANCHOR RAZEK 2,5","val":"109.200,00","uni":"Traumato"},
    {"conv":"IPERGS","med":"JOAO LUIZ MAISTER RAFAEL","prod":"BLOCK SAFE 21X120MM","val":"89.600,00","uni":"Traumato"},
    {"conv":"PETROBRAS","med":"OTAVIO PEREIRA CADORE","prod":"BLOCK SAFE 21X120MM","val":"75.300,00","uni":"Traumato"},
    {"conv":"BRADESCO SAUDE","med":"LEANDRO EMMEL BECKER","prod":"KIT ACCURE G.BLOCK 120MM X 21G","val":"68.500,00","uni":"Traumato"}]},
{"c":"UNIMED TORRE II","val":851645,"items":[
    {"conv":"PARTICULAR","med":"LUCAS LAMPERT","prod":"SERVICO / LOCACAO","val":"126.000,00","uni":"Holep"},
    {"conv":"PARTICULAR","med":"MARLON ROBERTO FIORENTINI","prod":"SERVICO / LOCACAO","val":"126.000,00","uni":"Holep"},
    {"conv":"UNIMED INTERCAMBIO","med":"LUCAS LAMPERT","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"58.705,00","uni":"RS"},
    {"conv":"UNIMED INTERCAMBIO","med":"MARLON ROBERTO FIORENTINI","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"54.200,00","uni":"RS"}]},
{"c":"SOC. SULINA DIVINA PROVIDENCIA","val":738890,"items":[
    {"conv":"IPERGS","med":"PAULO CONSTANTINO ROSSATO","prod":"BLOCK SAFE 21X120MM","val":"180.400,00","uni":"Traumato"},
    {"conv":"IPERGS","med":"JOEL C. WESTPHAL CORREA","prod":"BLOCK SAFE 21X120MM","val":"90.400,00","uni":"Traumato"},
    {"conv":"IPERGS","med":"JOEL C. WESTPHAL CORREA","prod":"BLOCK SAFE R3A 21X100MM","val":"68.500,00","uni":"Traumato"},
    {"conv":"IPERGS","med":"PAULO CONSTANTINO ROSSATO","prod":"BLOCK SAFE R3A 21X100MM","val":"51.800,00","uni":"Traumato"}]},
{"c":"MAE DE DEUS - AESC","val":723232,"items":[
    {"conv":"AMIL PLANOS","med":"ALESSANDRO ROSSOL","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"58.695,17","uni":"RS"},
    {"conv":"IPERGS","med":"TIAGO BORTOLINI","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"58.499,29","uni":"RS"},
    {"conv":"IPERGS","med":"TIAGO BORTOLINI","prod":"PROTESE PENIANA INFLAVEL TITAN 20CM","val":"57.697,93","uni":"RS"},
    {"conv":"PARTICULAR","med":"GABRIEL WEISS","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"52.100,00","uni":"RS"}]},
{"c":"BLANC POA","val":635250,"items":[
    {"conv":"AMIL PLANOS","med":"JOEL C. WESTPHAL CORREA","prod":"BLOCK SAFE 21X120MM","val":"124.500,00","uni":"Traumato"},
    {"conv":"AMIL PLANOS","med":"JOEL C. WESTPHAL CORREA","prod":"BLOCK SAFE 21X100MM","val":"99.600,00","uni":"Traumato"},
    {"conv":"AMIL PLANOS","med":"JOEL C. WESTPHAL CORREA","prod":"BLOCK SAFE R3A 21X100MM","val":"69.700,00","uni":"Traumato"},
    {"conv":"CASSI","med":"OTAVIO PEREIRA CADORE","prod":"BLOCK SAFE 21X120MM","val":"52.500,00","uni":"Traumato"}]},
{"c":"HOSPITAL DE CLINICAS","val":382190,"items":[
    {"conv":"PARTICULAR","med":"MAURO GHEDINI COSTA","prod":"SERVICO / LOCACAO","val":"68.800,00","uni":"RS"},
    {"conv":"IPE ADMINSTRATIVO","med":"GABRIEL WEISS","prod":"PROTESE INFLAVEL TITAN ESCROTAL 18CM","val":"57.476,74","uni":"RS"},
    {"conv":"PARTICULAR","med":"EDUARDO SCORTEGAGNA","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"51.454,89","uni":"RS"},
    {"conv":"CASSI","med":"GABRIEL WEISS","prod":"PROTESE PENIANA INFLAVEL TITAN 18CM","val":"49.200,00","uni":"RS"}]},
{"c":"CENTRO CLINICO GAUCHO","val":373824,"items":[
    {"conv":"CENTRO CLINICO GAUCHO","med":"CLEITON BICCA MESPAQUE","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"63.688,00","uni":"RS"},
    {"conv":"CENTRO CLINICO GAUCHO","med":"RAFAEL CARVALHO IPE DA SILVA","prod":"EXTRATOR DORMIA NO-TIP 1.5FR","val":"51.143,00","uni":"RS"},
    {"conv":"CENTRO CLINICO GAUCHO","med":"CLEITON BICCA MESPAQUE","prod":"BAINHA ACESSO URETERAL 10/12FR","val":"43.860,00","uni":"RS"},
    {"conv":"CENTRO CLINICO GAUCHO","med":"CLEITON BICCA MESPAQUE","prod":"FIBRA LASER REUTILIZAVEL 270","val":"42.750,00","uni":"RS"}]},
{"c":"HOSPITAL TACCHINI","val":302500,"items":[
    {"conv":"PARTICULAR","med":"NURY JAFAR ABBOUT FILHO","prod":"SERVICO / LOCACAO","val":"122.500,00","uni":"Holep"},
    {"conv":"IPERGS","med":"NURY JAFAR ABBOUT FILHO","prod":"SERVICO / LOCACAO","val":"70.000,00","uni":"Holep"},
    {"conv":"PARTICULAR","med":"ORESTES BLANCO NETTO","prod":"SERVICO / LOCACAO","val":"43.750,00","uni":"Holep"},
    {"conv":"SULAMERICA","med":"NURY JAFAR ABBOUT FILHO","prod":"FIBRA LASER 200UM SINGLE USE","val":"66.250,00","uni":"Holep"}]}
]

CIR_TIPO = [
# Dados reais BI analise/41 Mai/2026 - ordenado por subtotal desc
["PROTESE PENIANA INFLAVEL",918511,12],["BLOQUEIO",305900,13],["FLEXIVEL",210443,67],
["ARTROSCOPIA",103489,3],["OUTROS",120762,34],["HOLEP",166450,44],
["UROLIFT",114600,7],["PROTESE PENIANA MALEAVEL",105600,11],
["PROTESE PENIANA INFLAVEL + PERICARDIO",70000,1],["RIGIDA",62450,21],
["ANASTOMAT",51800,17],["PERICARDIO",38800,3],["CRYO",28500,1],
["PROTESE PENIANA MALEAVEL",27500,3],["DISCECTOMIA",24900,1],
["MATRIZ DERMICA",20870,1],["(LCA) LIGAMENTO CRUZADO ANTERIOR",11110,1],
["VORTEK",12436,1],["ASP-ELEFANT",9109,4],["ANASTOMAT",9000,2],
["RTU",7350,5],["FLEX+PERC",7865,1],["SEM ACOMPANHAMENTO",6218,5],
["CISTOLITO",750,1],["URETROTOMIA",750,1]
]
CIR_HOSPITAL = [
["MOINHOS DE VENTO",373562],["HOSPITAL MORIAH",192000],["HOSPITAL BLANC",132687],
["REGINA",120300],["UNIMED CHAPECO",96300],["MAE DE DEUS CENTER",79140],
["HOSPITAL CLINICAS PASSO FUNDO",79000],["UNIMED TORRE II",77330],
["UROSAS CLINICA SANTANNA",46800],["HOSPITAL TACCHINI",43600],
["NAO INFORMADO",42588],["FJ BAHIA",40000],["PUC",34244],["UNIMED PA-SL",33200],["OUTROS",123010]
]
CIR_CONVENIO = [
["PARTICULAR",491660],["BRADESCO SAUDE",219386],["CASSI",204070],
["VENDA DIRETA",155507],["AMIL PLANOS",128950],["UNIMED",110078],
["UNIMED POA",71166],["SULAMERICA",47116],["UNIMED INTERCAMBIO",38937],
["SAUDE CAIXA",30950],["POSTAL SAUDE",22187],["IPERGS",15750],["OUTROS",99755]
]
CIR_UNIDADE = [
# Dados reais BI analise/41 Mai/2026 - tipos por unidade ordenados por subtotal desc
{"un":"RS","val":860696,"qtd":155,"tipos":[
    ["PROTESE PENIANA INFLAVEL",409605,5],["FLEXIVEL",210443,67],
    ["RIGIDA",62450,21],["OUTROS",45701,21],["PROTESE PENIANA MALEAVEL",27500,3],
    ["HOLEP",24550,16],["MATRIZ DERMICA",20870,1],["OUTROS TIPOS",59577,20]]},
{"un":"Traumato","val":474792,"qtd":20,"tipos":[
    ["BLOQUEIO",305900,13],["ARTROSCOPIA",103489,3],["CRYO",28500,1],
    ["DISCECTOMIA",24900,1],["LCA - LIGAMENTO CRUZADO ANTERIOR",11110,1],["OUTROS",892,1]]},
{"un":"PR","val":388906,"qtd":14,"tipos":[
    ["PROTESE PENIANA INFLAVEL",240306,3],["PROTESE PENIANA INFLAVEL + PERICARDIO",70000,1],
    ["PROTESE PENIANA MALEAVEL",48600,5],["UROLIFT",20000,1],["ANASTOMAT",10000,4]]},
{"un":"SP","val":272468,"qtd":25,"tipos":[
    ["PROTESE PENIANA INFLAVEL",135000,2],["OUTROS",63968,10],
    ["UROLIFT",40000,2],["PROTESE PENIANA MALEAVEL",18500,2],["ANASTOMAT",15000,6]]},
{"un":"SC","val":181100,"qtd":13,"tipos":[
    ["PROTESE PENIANA INFLAVEL",93600,1],["UROLIFT",54600,4],
    ["ANASTOMAT",17800,5],["OUTROS",10200,2],["ASP-ELEFANT",4900,1]]},
{"un":"Holep","val":141900,"qtd":28,"tipos":[
    ["HOLEP",141900,28]]},
{"un":"BA","val":78800,"qtd":5,"tipos":[
    ["PROTESE PENIANA INFLAVEL",40000,1],["PERICARDIO",27800,2],
    ["PROTESE PENIANA MALEAVEL",11000,1],["ANASTOMAT DOACAO",0,1]]}
]

# Serialize

# ── Evolução de Faturamento por Mês/Ano ──────────────────────────────────────
FAT_EVOL = {
    "2023": [1011411, 715638, 1112228, 965169, 840928, 695651, 893185, 941595, 1165759, 785090, 1050677, 1103647],
    "2024": [950754, 844576, 1416027, 1504918, 889837, 1143892, 1410437, 1642347, 1316600, 1603626, 1583010, 1209414],
    "2025": [1614871, 1199783, 1558333, 2042439, 1940688, 2179188, 2013382, 2499096, 2466728, 2001449, 2144927, 2089765],
    "2026": [2161944, 2109384, 2311749, 2601247, 3087631, 887791, 0, 0, 0, 0, 0, 0]
}

# ── Fluxo de Caixa (dashboard/95) ────────────────────────────────────────────
FLUXO_CAIXA = {
    "a_receber": 698693.16,
    "a_pagar": 480254.34,
    "pagas": 0.00,
    "recebidas": 0.00,
    "periodo": "Mai/26"
}  # Fonte: bi.emultec.com.br/dashboard/55 (Maio 2026)

# ── Faturamento Pendente (dashboard/92) ──────────────────────────────────────
FAT_PENDENTE = {
    "RS":      {"pendente": 485000, "processos": 18},
    "Traumato":{"pendente": 312000, "processos": 14},
    "SP":      {"pendente": 178000, "processos": 8},
    "SC":      {"pendente": 95000,  "processos": 5},
    "Holep":   {"pendente": 65000,  "processos": 4},
    "BA":      {"pendente": 42000,  "processos": 3},
    "PR":      {"pendente": 28000,  "processos": 2},
    "total":   1205000
}

# ── Saldo Bancário (posição Mar/2026 — Fonte: Excel reunião gerencial) ────────
SALDO_BANCARIO = {
    "ref": "10/06/2026",
    "total_cc": 1609370.74,
    "total_invest": 2809560.71,
    "total_geral": 4418931.45,
    "obs": "Exclui saldo fabricante (R$ 139.627,25 custódia XP) e conta PR (Santander 130071322 sem extrato)",
    "contas": [
        {
            "nome": "Itaú Porto Alegre", "conta": "99670-3", "banco": "Itaú Ag. 0280",
            "un": "RS", "cc": 358126.73, "invest": 61293.47, "total": 419420.20,
            "invest_det": [
                {"desc": "Mapfre Confianza RF DI", "val": 61293.47}
            ]
        },
        {
            "nome": "Itaú Holep", "conta": "99305-6", "banco": "Itaú Ag. 0280",
            "un": "Holep", "cc": 462554.83, "invest": 858397.80, "total": 1320952.63,
            "invest_det": [
                {"desc": "Itaú Trust DI", "val": 257833.90},
                {"desc": "Itaú CB Empresas RF", "val": 257808.42},
                {"desc": "Itaú CB RF CP", "val": 253541.40},
                {"desc": "CDB-DI 96% (venc. 05/08/2030)", "val": 89214.08}
            ]
        },
        {
            "nome": "Itaú Santa Catarina", "conta": "99228-0", "banco": "Itaú Ag. 0280",
            "un": "SC", "cc": 80817.36, "invest": 124735.66, "total": 205553.02,
            "invest_det": [
                {"desc": "Itaú CB Empresas RF", "val": 124735.66}
            ]
        },
        {
            "nome": "Itaú Traumato", "conta": "99688-5", "banco": "Itaú Ag. 0280",
            "un": "Traumato", "cc": 490885.92, "invest": 1034133.96, "total": 1525019.88,
            "invest_det": [
                {"desc": "Itaú CB RF CP", "val": 208542.89},
                {"desc": "Itaú Trust DI", "val": 208522.62},
                {"desc": "Kinea Andes FIF CIC RF CP LP RL", "val": 204485.39},
                {"desc": "Global Dinâmico FIF RF CP", "val": 204116.71},
                {"desc": "Selic EMP FIF RF", "val": 104266.14},
                {"desc": "CDB-DI 98% (venc. 13/01/2031)", "val": 104200.21}
            ]
        },
        {
            "nome": "Itaú Bahia", "conta": "99487-7", "banco": "Itaú Ag. 8841",
            "un": "BA", "cc": 83952.48, "invest": 83951.48, "total": 167903.96,
            "invest_det": [
                {"desc": "Aplic. Aut. Mais (CDB)", "val": 83951.48}
            ]
        },
        {
            "nome": "BB São Paulo", "conta": "16918-8", "banco": "Banco do Brasil Ag. 3535-1",
            "un": "SP", "cc": 133033.42, "invest": 196600.02, "total": 329633.44,
            "invest_det": [
                {"desc": "CDB DI 95% (venc. 29/11/2030)", "val": 166000.0},
                {"desc": "Fundo RF Ref DI Plus Ágil", "val": 10.76},
                {"desc": "Fundo RF Ref DI 90 Mil", "val": 24945.26}
            ]
        },
        {
            "nome": "XP Investimentos", "conta": "9313357", "banco": "XP Investimentos",
            "un": "—", "cc": 0.0, "invest": 450448.32, "total": 450448.32,
            "invest_det": [
                {"desc": "Compromissadas", "val": 38135.25},
                {"desc": "Iridium Apollo FIF RF CP LP RL", "val": 29215.02},
                {"desc": "Tivio Institucional RF CP FIF RL", "val": 20382.27},
                {"desc": "Kinea Andes FIF CIC RF CP LP RL", "val": 124630.97},
                {"desc": "SulAmérica Premium Plus FIRF DI CP", "val": 238084.81}
            ]
        }
    ]
}

inad_js      = json.dumps(INADIMPLENTES,  ensure_ascii=False)
inad_unid_js = json.dumps(INAD_UNIDADE,   ensure_ascii=False)
# Auto-atualizar mês atual se bi_data.json tiver faturamento mais recente
if _bi.get("faturamento"):
    # Derivar período de 'coleta_em' se 'periodo' não existir
    _ini = ""
    if _bi.get("periodo"):
        _ini = _bi["periodo"].get("ini","")
    elif _bi.get("coleta_em"):
        import re as _re
        _m = _re.match(r'(\d{4})-(\d{2})-(\d{2})', str(_bi["coleta_em"]))
        if _m:
            _ini = f"{_m.group(1)}-{_m.group(2)}-01"
    if _ini:
        _yr  = _ini[2:4]; _mo = int(_ini[5:7])
        _mo_abbr = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"][_mo-1]
        _cur_key = _mo_abbr + _yr
        _cur_lbl = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"][_mo-1] + "/" + _yr
        if _cur_key not in FAT_PERIODS:
            # Novo mês detectado → criar entrada automaticamente
            _by_un = sorted(_bi.get("faturamento_por_un",{}).items(), key=lambda x:-x[1])
            FAT_PERIODS[_cur_key] = {
                "label": _cur_lbl,
                "ini": _bi["periodo"]["ini"],
                "fim": _bi["periodo"].get("fim", _bi["periodo"]["ini"]),
                "total": round(_bi["faturamento"], 2),
                "nf_count": _bi.get("nf_count", 0),
                "prazo": 30,
                "parcial": True,
                "byUN": [[k,int(v)] for k,v in _by_un],
                "byGrupo": []
            }
            print(f"[AUTO] Novo mês {{_cur_key}} adicionado ao FAT_PERIODS: R${{_bi['faturamento']:,.2f}}")
        else:
            # Mês existente → atualizar valores
            FAT_PERIODS[_cur_key]["total"] = round(_bi["faturamento"], 2)
            FAT_PERIODS[_cur_key]["fim"]   = _bi.get("periodo",{}).get("fim","")
            if _bi.get("nf_count"):
                FAT_PERIODS[_cur_key]["nf_count"] = int(_bi["nf_count"])
            if _bi.get("faturamento_por_un"):
                _by_un = sorted(_bi["faturamento_por_un"].items(), key=lambda x:-x[1])
                FAT_PERIODS[_cur_key]["byUN"] = [[k,int(v)] for k,v in _by_un]
            print(f"[AUTO] {_cur_key} atualizado: R${_bi['faturamento']:,.2f}")
            # Auto-atualizar despesas do mês atual
            if _bi.get("despesas") and _cur_key in DESP_PERIODS:
                DESP_PERIODS[_cur_key]["total"] = round(_bi["despesas"], 2)
                print(f"[AUTO] Despesas {_cur_key} atualizadas: R${_bi['despesas']:,.2f}")
        # Auto-atualizar FAT_EVOL com os totais mensais de FAT_PERIODS
        _MES_IDX = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
        for _fk, _fp in FAT_PERIODS.items():
            if len(_fk) == 5 and _fk[:3] in _MES_IDX:
                _yr_str = "20" + _fk[3:5]
                _mi = _MES_IDX.index(_fk[:3])
                if _yr_str in FAT_EVOL and _mi < len(FAT_EVOL[_yr_str]):
                    FAT_EVOL[_yr_str][_mi] = round(_fp["total"])

fat_per_js   = json.dumps(FAT_PERIODS,    ensure_ascii=False)
desp_per_js  = json.dumps(DESP_PERIODS,   ensure_ascii=False)
fat_cl_js    = json.dumps(FAT_CLIENTES,   ensure_ascii=False)
cir_tipo_js  = json.dumps(CIR_TIPO,       ensure_ascii=False)
cir_hosp_js  = json.dumps(CIR_HOSPITAL,   ensure_ascii=False)
cir_conv_js  = json.dumps(CIR_CONVENIO,   ensure_ascii=False)
cir_unid_js  = json.dumps(CIR_UNIDADE,    ensure_ascii=False)
grand_fmt    = f"{INAD_GRAND_TOTAL:,.2f}".replace(",","X").replace(".",",").replace("X",".")
fat_evol_js    = json.dumps(FAT_EVOL,        ensure_ascii=False)
fluxo_js       = json.dumps(FLUXO_CAIXA,    ensure_ascii=False)
fat_pend_js    = json.dumps(FAT_PENDENTE,   ensure_ascii=False)
saldo_banc_js  = json.dumps(SALDO_BANCARIO, ensure_ascii=False)

# --- Defaults pré-renderizados (sincronizados com os dados atuais) ---
# Ordena períodos mensais por data real (ex: "mai26" → 2026-05, "abr26" → 2026-04)
_MES = {"jan":1,"fev":2,"mar":3,"abr":4,"mai":5,"jun":6,"jul":7,"ago":8,"set":9,"out":10,"nov":11,"dez":12}
def _period_order(k):
    return (int("20"+k[3:5]), _MES.get(k[:3], 0)) if len(k)==5 and k[:3] in _MES else (0,0)
_DEF_PERIOD    = sorted([k for k in FAT_PERIODS if k != "1t26"], key=_period_order)[-1]
_def_fp        = FAT_PERIODS[_DEF_PERIOD]
_def_dp        = DESP_PERIODS.get(_DEF_PERIOD, {"total": 0})
def _fmt_kpi(v):
    s = f"{v:,.0f}".replace(",","X").replace(".",",").replace("X",".")
    return f"R$ {s}"
_def_fat_str   = _fmt_kpi(_def_fp["total"])
_def_desp_str  = _fmt_kpi(_def_dp["total"])
_def_prazo     = f"{_def_fp.get('prazo',0)} dias"
_def_prazo_sub = f"Media {_def_fp['label']}"
# --------------------------------------------------------------------------

import datetime as _datetime_mod
_today_str = _datetime_mod.date.today().strftime("%d/%m/%Y")
# --- Gerar listas
_periodos_mensais_js = []
_periodos_trim_js = []
for _k in sorted([k for k in FAT_PERIODS if k[:3] in _MES and len(k)==5], key=_period_order):
    _lbl = FAT_PERIODS[_k]["label"]
    _periodos_mensais_js.append('{"key":"'+_k+'","label":"'+_lbl+'"}' )
for _k in sorted([k for k in FAT_PERIODS if not(k[:3] in _MES and len(k)==5)]):
    _lbl = FAT_PERIODS[_k]["label"]
    _periodos_trim_js.append('{"key":"'+_k+'","label":"'+_lbl+'"}' )
_periodos_mensais_str = "[" + ",".join(_periodos_mensais_js) + "]"
_periodos_trim_str    = "[" + ",".join(_periodos_trim_js)    + "]"

# ── Gerar lista completa de meses Jan/2022 até hoje ────────
import datetime as _dt
_start_year, _start_month = 2022, 1
_now = _dt.date.today()
_all_months = []
_m = _dt.date(_start_year, _start_month, 1)
_end = _dt.date(_now.year, _now.month, 1)
while _m <= _end:
    _mk = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"][_m.month-1] + str(_m.year)[2:]
    _ml = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"][_m.month-1] + "/" + str(_m.year)[2:]
    _all_months.append((_mk, _ml, _mk in FAT_PERIODS))
    _m = (_m.replace(day=28) + _dt.timedelta(days=4)).replace(day=1)

# Últimos 3 COM dados = botões; resto = dropdown
_mens_sorted = [k for k,l,d in _all_months if d]
_trim_sorted = sorted([k for k in FAT_PERIODS if not(k[:3] in _MES and len(k)==5)])
_recent3     = _mens_sorted[-3:]
_historic_with_data = _mens_sorted[:-3]  # meses anteriores COM dados

# Montar dropdown: TODOS os meses históricos (com e sem dados)
_hist_for_dropdown = [(k,l,d) for k,l,d in _all_months if k not in _recent3 and k not in _trim_sorted]
_chips_parts = []
if _hist_for_dropdown:
    _opts = []
    for _k,_l,_hd in reversed(_hist_for_dropdown):  # mais recentes primeiro
        if _hd:
            _opts.append(f'<option value="{_k}">{_l}</option>')
        else:
            _opts.append(f'<option value="{_k}" class="no-data">📊 {_l}</option>')
    _opts_html = "".join(_opts)
    _titulo = f"📁 Histórico ({len(_hist_for_dropdown)} meses)"
    _chips_parts.append(f'<select class="period-hist-select" onchange="if(this.value){{setActivePeriod(this.value);this.value=&quot;&quot;}}"><option value="">' + _titulo + f'</option>' + _opts_html + '</select>')

for _k in _recent3:
    _active = " active" if _k == _DEF_PERIOD else ""
    _parcial = " 🔄" if FAT_PERIODS[_k].get("parcial") else ""
    _chips_parts.append(f'<button class="period-chip{_active}" data-key="{_k}" onclick="setActivePeriod(this.dataset.key)">{FAT_PERIODS[_k]["label"]}{_parcial}</button>')
if _trim_sorted:
    _chips_parts.append('<div style="width:1px;background:var(--border);margin:0 4px;align-self:stretch;"></div>')
    for _k in _trim_sorted:
        _active = " active" if _k == _DEF_PERIOD else ""
        _chips_parts.append(f'<button class="period-chip trim{_active}" data-key="{_k}" onclick="setActivePeriod(this.dataset.key)">{FAT_PERIODS[_k]["label"]}</button>')
_period_chips_html = "".join(_chips_parts)
# -------------------------------------------

# Chart: Faturamento × Recebida × Despesas — gerado dinamicamente de FAT_PERIODS/DESP_PERIODS_RAW
_chart_ks        = sorted([k for k in FAT_PERIODS if k[:3] in _MES and len(k)==5 and FAT_PERIODS[k].get("total",0)>0], key=_period_order)
_chart_labels_js = json.dumps([FAT_PERIODS[k]["label"]                              for k in _chart_ks])
_chart_fat_js    = json.dumps([round(FAT_PERIODS[k].get("total",0),2)               for k in _chart_ks])
_chart_desp_js   = json.dumps([round(DESP_PERIODS_RAW.get(k,{}).get("total",0),2)   for k in _chart_ks])
# Receita recebida e Despesa paga por mês — analise/45 (pagar_receber_agrupado)
# Lido de bi_data.json["a45_por_mes"] (chave "AAAA-MM"). Fallback hardcoded se ausente.
_A45_FALLBACK = {
    "2026-03": {"rec": 2992980.59, "desp": 2025489.86},
    "2026-04": {"rec": 2261912.91, "desp": 2395797.02},
    "2026-05": {"rec": 2457910.74, "desp": 2096914.47},
    "2026-06": {"rec": 1249236.09, "desp":  810987.11},
}
_A45 = {**_A45_FALLBACK, **_bi.get("a45_por_mes", {})}
def _a45key(k):
    _mn = {"jan":"01","fev":"02","mar":"03","abr":"04","mai":"05","jun":"06",
           "jul":"07","ago":"08","set":"09","out":"10","nov":"11","dez":"12"}
    return "20" + k[3:] + "-" + _mn.get(k[:3],"00")
_chart_rec_js  = json.dumps([_A45.get(_a45key(k),{}).get("rec",  0) for k in _chart_ks])
_chart_desp_js = json.dumps([_A45.get(_a45key(k),{}).get("desp", 0) for k in _chart_ks])

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Dashboard Executivo | Magnum Import</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{{--teal:#00CCCC;--navy:#153066;--blue:#476AAE;--green:#4FC454;--yellow:#E8AF1B;--red:#D44;--bg:#F0F2F5;--card:#fff;--text:#2D3748;--muted:#718096;--border:#E2E8F0;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);font-family:'Segoe UI',Arial,sans-serif;color:var(--text);font-size:14px}}
.header{{background:linear-gradient(135deg,var(--navy) 0%,#1a4080 60%,#0e6e8e 100%);padding:16px 28px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 2px 10px rgba(0,0,0,.3)}}
.header-left{{display:flex;align-items:center;gap:16px}}
.header img{{height:46px}}
.header h1{{color:#fff;font-size:21px;font-weight:800;letter-spacing:.3px}}
.header h1 span{{color:var(--teal)}}
.header-right{{text-align:right;color:rgba(255,255,255,.8);font-size:12px}}
.header-right .upd{{color:var(--teal);font-size:11px;margin-top:3px}}
.period-bar{{background:#fff;border-bottom:2px solid var(--border);padding:12px 28px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.period-bar label{{font-size:12px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.5px}}
.period-chips{{display:flex;gap:8px}}
.period-chip{{padding:7px 20px;border-radius:20px;font-size:14px;font-weight:700;cursor:pointer;background:var(--border);color:var(--muted);border:none;transition:all .2s}}
.period-chip.active{{background:var(--navy);color:#fff;box-shadow:0 2px 8px rgba(21,48,102,.4)}}
.period-chip.trim{{background:#EEF2FF;color:var(--blue);border:2px solid #BCC8E8}}
.period-chip.trim.active{{background:var(--blue);color:#fff;border-color:var(--blue)}}
.period-chips{{display:flex;gap:8px;align-items:center}}
.period-hist-select{{padding:6px 14px;border-radius:20px;font-size:13px;font-weight:700;cursor:pointer;background:var(--border);color:var(--muted);border:2px solid transparent;transition:all .2s;outline:none;}}
.period-hist-select:hover{{background:#dde3ed}}
.period-hist-select:focus{{border-color:var(--blue)}}
.period-hist-select option{{font-weight:600;background:#fff}}
.period-badge{{font-size:12px;background:#EEF2FF;color:var(--blue);padding:4px 14px;border-radius:12px;font-weight:700;margin-left:auto}}
.kpi-strip{{display:flex;gap:14px;padding:16px 28px;overflow-x:auto}}
.kpi-card{{background:var(--card);border-radius:10px;padding:14px 20px;min-width:180px;box-shadow:0 1px 4px rgba(0,0,0,.07);border-left:4px solid var(--teal);flex:1}}
.kpi-card.red{{border-left-color:var(--red)}}.kpi-card.green{{border-left-color:var(--green)}}
.kpi-card.yellow{{border-left-color:var(--yellow)}}.kpi-card.blue{{border-left-color:var(--blue)}}
.has-tooltip{{cursor:help}}
.kpi-label{{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;font-weight:700}}
.kpi-value{{font-size:20px;font-weight:900;color:var(--navy);margin-top:4px}}
.kpi-sub{{font-size:11px;color:var(--muted);margin-top:3px}}
.main{{padding:0 28px 28px}}.main.dash-grid{{padding:18px 28px 28px}}
.section-card{{background:var(--card);border-radius:12px;margin-bottom:18px;box-shadow:0 2px 8px rgba(0,0,0,.06);overflow:hidden}}
.sec-head{{display:flex;align-items:center;justify-content:space-between;padding:16px 22px;cursor:pointer;border-bottom:2px solid transparent;transition:border-color .2s;user-select:none}}
.sec-head:hover{{background:#f8fafc}}
.sec-head.open{{border-bottom-color:var(--border)}}
.sec-title{{display:flex;align-items:center;gap:10px}}
.sec-icon{{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px}}
.sec-icon.r{{background:#FFF0F0}}.sec-icon.t{{background:#E6FFFF}}.sec-icon.b{{background:#EEF2FF}}.sec-icon.g{{background:#F0FFF4}}
.sec-h2{{font-size:16px;font-weight:700;color:var(--navy)}}
.sec-sub{{font-size:12px;color:var(--muted);margin-top:1px}}
.sec-totals{{display:flex;gap:20px;align-items:center}}
.sec-total-item{{text-align:right}}
.sec-total-label{{font-size:11px;color:var(--muted);text-transform:uppercase}}
.sec-total-value{{font-size:18px;font-weight:900}}
.sec-total-value.r{{color:var(--red)}}.sec-total-value.t{{color:#009999}}.sec-total-value.b{{color:var(--blue)}}.sec-total-value.g{{color:#2E9E38}}
.expand-btn{{width:28px;height:28px;border-radius:50%;background:var(--border);display:flex;align-items:center;justify-content:center;transition:transform .3s;font-size:14px;color:var(--muted);flex-shrink:0;pointer-events:none}}
.sec-head.open .expand-btn{{transform:rotate(180deg);background:var(--navy);color:#fff}}
.sec-body{{display:none;padding:20px 22px}}
.sec-body.open{{display:block}}
.insights-row{{display:flex;gap:14px;margin-bottom:16px;flex-wrap:wrap}}
.insight-card{{background:var(--bg);border-radius:10px;padding:14px 18px;flex:1;min-width:140px;border:1px solid var(--border)}}
.insight-icon{{font-size:22px;margin-bottom:6px}}
.insight-val{{font-size:20px;font-weight:900;color:var(--navy)}}
.insight-label{{font-size:11px;color:var(--muted);margin-top:2px;font-weight:600}}
.insight-note{{font-size:11px;color:var(--muted);margin-top:4px}}
.chrow{{display:flex;gap:16px;margin-bottom:16px;flex-wrap:wrap}}
.chbox{{background:#f8fafc;border-radius:10px;padding:16px;flex:1;min-width:220px}}
.chbox h3{{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:12px}}
.chw{{position:relative;height:220px}}
.det-toggle{{display:flex;align-items:center;justify-content:center;gap:8px;padding:10px;cursor:pointer;background:var(--bg);border-radius:8px;font-size:13px;font-weight:700;color:var(--navy);border:1px solid var(--border);margin-top:8px;transition:all .2s;user-select:none}}
.det-toggle:hover{{background:#e8edf5;border-color:#aab}}
.det-toggle .det-arrow{{transition:transform .3s;font-size:14px}}
.det-toggle.open .det-arrow{{transform:rotate(180deg)}}
.det-panel{{display:none;margin-top:14px}}
.tabs{{display:flex;border-bottom:2px solid var(--border);margin-bottom:18px;flex-wrap:wrap}}
.tab-btn{{padding:8px 18px;background:none;border:none;border-bottom:2px solid transparent;margin-bottom:-2px;font-size:13px;font-weight:700;color:var(--muted);cursor:pointer;transition:all .2s}}
.tab-btn.active{{color:var(--navy);border-bottom-color:var(--teal)}}
.tab-pane{{display:none}}.tab-pane.active{{display:block}}
.dtbl{{width:100%;border-collapse:collapse;font-size:13px}}
.dtbl th{{background:var(--navy);color:#fff;padding:9px 12px;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.5px;white-space:nowrap}}
.dtbl th.r{{text-align:right}}.dtbl th.c{{text-align:center}}
.dtbl td{{padding:8px 12px;border-bottom:1px solid var(--border);vertical-align:middle}}
.dtbl tr:hover td{{background:#f0f9ff}}
.dtbl .val{{text-align:right;font-weight:700;font-family:monospace;font-size:13px}}
.dtbl .ctr{{text-align:center}}
.bdg{{display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700}}
.bdg-r{{background:#FFF0F0;color:#C0392B}}.bdg-o{{background:#FFF5E6;color:#E67E22}}
.bdg-y{{background:#FFFDE7;color:#B7860B}}.bdg-g{{background:#F0FFF4;color:#27AE60}}
.bdg-t{{background:#E0FFFF;color:#007777}}.bdg-b{{background:#EEF2FF;color:var(--blue)}}
.bdg-gray{{background:#F0F2F5;color:var(--muted)}}.bdg-un{{background:var(--navy);color:#fff}}
.exp-row{{background:#F8FAFF!important;display:none}}
.exp-inner{{padding:12px 16px 16px}}
.sub-tbl{{width:100%;border-collapse:collapse;font-size:12px}}
.sub-tbl th{{background:#E8EDF5;color:var(--navy);padding:6px 10px;font-size:11px;text-transform:uppercase}}
.sub-tbl td{{padding:6px 10px;border-bottom:1px solid #e8edf5}}
.sub-tbl .val{{text-align:right;font-weight:600;font-family:monospace}}
.togrow{{cursor:pointer}}.togrow:hover td{{background:#EBF8FF!important}}
.unid-grid{{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}}
.unid-pill{{background:var(--bg);border:2px solid var(--border);border-radius:8px;padding:10px 16px;display:flex;flex-direction:column;align-items:center;min-width:110px;cursor:pointer;transition:all .2s}}
.unid-pill:hover{{border-color:var(--teal);background:#E6FFFF}}
.unid-pill.active{{border-color:var(--navy);background:var(--navy)}}
.unid-pill.active .u-name,.unid-pill.active .u-cnt{{color:#fff}}
.unid-pill.active .u-val{{color:var(--teal)}}
.u-name{{font-size:13px;font-weight:800;color:var(--navy)}}
.u-val{{font-size:15px;font-weight:900;color:var(--teal);margin-top:2px;font-family:monospace}}
.u-cnt{{font-size:10px;color:var(--muted)}}
.search-bar{{position:relative;margin-bottom:14px}}
.search-bar input{{width:100%;max-width:340px;padding:8px 12px 8px 34px;border:1px solid var(--border);border-radius:8px;font-size:13px;background:#f8fafc;outline:none}}
.search-bar input:focus{{border-color:var(--teal);background:#fff}}
.search-bar::before{{content:"\\1F50D";position:absolute;left:10px;top:8px;font-size:14px}}
.tscroll{{overflow-x:auto;border-radius:8px}}
.days-big{{font-size:52px;font-weight:900;color:var(--navy);line-height:1}}
.days-box{{background:linear-gradient(135deg,#E6FFFF,#CCF5FF);border-radius:10px;padding:20px;text-align:center;border:1px solid var(--teal)}}
.filter-bar{{display:flex;align-items:center;gap:8px;padding:8px 0;font-size:12px;color:var(--muted)}}
.filter-bar strong{{color:var(--navy)}}
.btn-clear{{background:none;border:1px solid var(--border);border-radius:6px;padding:3px 10px;font-size:11px;cursor:pointer;color:var(--muted)}}
.btn-clear:hover{{background:var(--bg)}}
.footer{{text-align:center;padding:16px;font-size:11px;color:var(--muted)}}
.ov-kpis{{display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap}}
.ov-kpi{{background:var(--bg);border-radius:10px;padding:12px 18px;flex:1;min-width:150px;border:1px solid var(--border);display:flex;align-items:center;gap:14px}}
.ov-kpi-icon{{font-size:26px}}
.ov-kpi-val{{font-size:17px;font-weight:900;color:var(--navy)}}
.ov-kpi-lbl{{font-size:10px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.4px}}
.ov-kpi-note{{font-size:11px;color:var(--muted);margin-top:3px}}
@media(max-width:768px){{.kpi-strip,.main{{padding:12px 14px}}.header,.period-bar{{padding:12px 14px}}.chrow{{flex-direction:column}}.sec-totals{{display:none}}}}
.sec-preview{{background:linear-gradient(90deg,#f0f4ff 0%,#f8fafc 100%);border-bottom:1px solid var(--border);padding:10px 22px;display:flex;gap:0;flex-wrap:wrap;align-items:stretch}}
.prev-item{{display:flex;flex-direction:column;gap:2px;padding:6px 20px 6px 0;margin-right:20px;border-right:1px solid var(--border);justify-content:center}}.prev-item:last-child{{border-right:none}}
.prev-lbl{{font-size:10px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.4px}}
.prev-val{{font-size:16px;font-weight:900;color:var(--navy);line-height:1.3}}
.prev-badge{{font-size:12px;font-weight:700;padding:3px 12px;border-radius:12px;display:inline-block}}
.badge-green{{background:#E8FFF0;color:#1a9e38}}.badge-red{{background:#FFF0F0;color:#C0392B}}
.badge-yellow{{background:#FFFDE7;color:#B7860B}}.badge-teal{{background:#E0FFFF;color:#007777}}
.badge-blue{{background:#EEF2FF;color:#476AAE}}.badge-gray{{background:#F0F2F5;color:#718096}}
.fluxo-kpi{{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:14px 18px;flex:1;min-width:150px;display:flex;align-items:center;gap:14px}}
.fluxo-kpi.green-b{{border-left:4px solid var(--green)}}.fluxo-kpi.red-b{{border-left:4px solid var(--red)}}
.fluxo-kpi.teal-b{{border-left:4px solid var(--teal)}}.fluxo-kpi.yellow-b{{border-left:4px solid var(--yellow)}}
.fluxo-kpi-icon{{font-size:24px}}.fluxo-kpi-val{{font-size:18px;font-weight:900;color:var(--navy)}}
.fluxo-kpi-lbl{{font-size:11px;color:var(--muted);font-weight:600}}
/* ── 2-column grid layout ── */
.dash-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;align-items:start}}
.span2{{grid-column:1/-1}}
/* ── always-visible mini charts ── */
.mini-ch{{background:var(--card);border-top:1px solid var(--border)}}
.mini-ch-inner{{padding:10px 22px 16px}}
.mini-ch-inner h4{{font-size:10px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px}}
.mini-chw{{position:relative;height:145px}}
/* ── Compact headers for 2-col cards ── */
.dash-grid .section-card:not(.span2) .sec-head{{padding:11px 14px}}
.dash-grid .section-card:not(.span2) .sec-h2{{font-size:13px}}
.dash-grid .section-card:not(.span2) .sec-sub{{font-size:10px;margin-top:1px}}
.dash-grid .section-card:not(.span2) .sec-icon{{width:28px;height:28px;font-size:15px}}
.dash-grid .section-card:not(.span2) .sec-total-value{{font-size:13px}}
.dash-grid .section-card:not(.span2) .sec-total-label{{font-size:9px}}
.dash-grid .section-card:not(.span2) .sec-totals{{gap:10px}}
.dash-grid .section-card:not(.span2) .sec-totals .sec-total-item:nth-child(2){{display:none}}
.dash-grid .section-card:not(.span2) .sec-preview{{padding:8px 14px}}
.dash-grid .section-card:not(.span2) .prev-item{{padding:4px 12px 4px 0;margin-right:12px}}
.dash-grid .section-card:not(.span2) .prev-val{{font-size:13px}}
.dash-grid .section-card:not(.span2) .prev-lbl{{font-size:9px}}
.dash-grid .section-card:not(.span2) .prev-badge{{font-size:11px;padding:2px 8px}}
.dash-grid .section-card:not(.span2) .sec-body{{padding:14px 16px}}
.mini-ch-inner{{padding:10px 16px 14px}}
@media(max-width:900px){{.dash-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>

<div class="header">
  <div class="header-left">
    <img src="https://magnumimport.com.br/wp-content/uploads/2024/04/magnum-logo-white.png" alt="Magnum" onerror="this.style.display='none'">
    <div>
      <h1>Dashboard <span>Executivo</span></h1>
      <div style="color:rgba(255,255,255,.6);font-size:11px;margin-top:2px">Painel de Gestao — Diretoria</div>
    </div>
  </div>
  <div class="header-right">
    <div id="hDate">03/06/2026</div>
    <div class="upd">bi.emultec.com.br</div>
  </div>
</div>

<div class="period-bar">
  <label>📅 Periodo:</label>
  <div class="period-chips" id="period-chips-container">{_period_chips_html}</div>
  <span class="period-badge" id="periodLabel">{FAT_PERIODS[_DEF_PERIOD]["label"]}</span>
</div>

<div class="kpi-strip">
  <div class="kpi-card green">
    <div class="kpi-label">Faturamento</div>
    <div class="kpi-value" id="kpiFatValue">{_def_fat_str}</div>
    <div class="kpi-sub" id="kpiFatSub">—</div>
  </div>
  <div class="kpi-card yellow">
    <div class="kpi-label">Despesas</div>
    <div class="kpi-value" id="kpiDespValue">{_def_desp_str}</div>
    <div class="kpi-sub" id="kpiDespSub">—</div>
  </div>
  <div class="kpi-card red">
    <div class="kpi-label">Inadimplencia Total</div>
    <div class="kpi-value">R$ {grand_fmt}</div>
    <div class="kpi-sub">95 titulos · 7 unidades</div>
  </div>
  <div class="kpi-card blue has-tooltip" data-tooltip="Tempo médio entre a data da cirurgia e a emissão da nota fiscal">
    <div class="kpi-label">Prazo Cirug./NF</div>
    <div class="kpi-value" id="kpiPrazo">{_def_prazo}</div>
    <div class="kpi-sub" id="kpiPrazoSub">{_def_prazo_sub}</div>
  </div>
</div>

<!-- Ciclo Operacional — 2 cards calculados de cirurgia → nota e cirurgia → recebimento -->
<div class="kpi-strip" style="margin-top:8px">
  <div class="kpi-card blue has-tooltip" data-tooltip="Média {_ciclo_ref}: tempo entre data da cirurgia e emissão da NF. Base: {_ciclo_nota['n']:,} registros.">
    <div class="kpi-label">Ciclo Cirurgia → NF</div>
    <div class="kpi-value" id="kpiCicloNota">{_ciclo_nota['media']} dias</div>
    <div class="kpi-sub">Média · {_ciclo_nota['n']:,} registros · dados até {_ciclo_ate}</div>
  </div>
  <div class="kpi-card teal has-tooltip" data-tooltip="Média {_ciclo_ref}: tempo entre data da cirurgia e o recebimento efetivo. Base: {_ciclo_receb['n']:,} registros.">
    <div class="kpi-label">Ciclo Cirurgia → Recebimento</div>
    <div class="kpi-value" id="kpiCicloReceb">{_ciclo_receb['media']} dias</div>
    <div class="kpi-sub">Média · {_ciclo_receb['n']:,} registros · dados até {_ciclo_ate}</div>
  </div>
</div>



<div class="main dash-grid">

<!-- 1. ANALISES — Evolução de Faturamento + Receita vs Despesa -->
<div class="section-card span2">
  <div class="sec-head open" data-target="bodyAnalise">
    <div class="sec-title">
      <div class="sec-icon b">📊</div>
      <div><div class="sec-h2">Análises & Evolução</div>
           <div class="sec-sub">Evolução histórica de faturamento e comparativo Receita × Despesa</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label" id="analFatYtdLbl">Faturamento 2026</div>
        <div class="sec-total-value b" id="analFatYtdVal">R$ 11.908.549</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevAnalise">
    <div class="prev-item"><div class="prev-lbl">Faturamento 2026 (acumulado)</div><div class="prev-val" id="prevAnaliseFat2026">—</div></div>
    <div class="prev-item"><div class="prev-lbl">vs 2025 mesmo período</div><div class="prev-val"><span class="prev-badge badge-green" id="prevAnaliseCrescimento">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl has-tooltip" data-tooltip="(Faturamento − Despesas) / Faturamento × 100">Margem Operacional</div><div class="prev-val"><span class="prev-badge badge-teal" id="prevAnaliseMargem">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl has-tooltip" data-tooltip="100% − (Inadimplência total / Faturamento acumulado 2026)">Índice Recebimento</div><div class="prev-val"><span class="prev-badge badge-blue" id="prevAnaliseRecTaxa">—</span></div></div>
  </div>
  <div class="sec-body open" id="bodyAnalise">
    <div class="chrow">
      <div class="chbox" style="flex:2;min-width:300px">
        <h3>📈 Evolução de Faturamento por Ano (R$)</h3>
        <div class="chw" style="height:280px"><canvas id="chFatEvol"></canvas></div>
      </div>
    </div>
    <div class="chrow">
      <div class="chbox" style="flex:1;min-width:280px">
        <h3>⚖️ Faturamento × Recebida × Despesas — Mensal 2026</h3>
        <div class="chw" style="height:220px"><canvas id="chFatDesp"></canvas></div>
      </div>
      <div class="chbox" style="flex:1;min-width:240px">
        <h3>🏆 Top Grupos por Período</h3>
        <div style="overflow-y:auto;max-height:220px" id="analiseTopGrupos"></div>
      </div>
    </div>
  </div>
</div>

<!-- 2. INADIMPLENTES -->
<div class="section-card">
  <div class="sec-head" data-target="bodyInad">
    <div class="sec-title">
      <div class="sec-icon r">⚠️</div>
      <div><div class="sec-h2">Inadimplentes Atuais</div>
           <div class="sec-sub" id="inadSecSub">Titulos vencidos — ordenados por atraso decrescente</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Total em Aberto (BI)</div>
        <div class="sec-total-value r">R$ {grand_fmt}</div></div>
      <div class="sec-total-item"><div class="sec-total-label">Mais afetada</div>
        <div class="sec-total-value r">Traumato</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevInad">
    <div class="prev-item"><div class="prev-lbl">Total Inadimplência</div><div class="prev-val" id="prevInadTotal">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Unidade mais afetada</div><div class="prev-val" id="prevInadTopUN">Traumato</div></div>
    <div class="prev-item"><div class="prev-lbl">Títulos em aberto</div><div class="prev-val" id="prevInadCount">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Taxa inadimplência</div><div class="prev-val"><span class="prev-badge badge-red" id="prevInadTaxa">—</span></div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>Inadimplência por Unidade (R$)</h4>
    <div class="mini-chw"><canvas id="chMiniInad"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodyInad">
    <div class="insights-row" id="inadInsightCards"></div>
    <div class="chrow">
      <div class="chbox"><h3>Inadimplencia por Unidade (R$)</h3>
        <div class="chw"><canvas id="chInadUnid"></canvas></div></div>
      <div class="chbox" style="flex:1.3"><h3>Distribuicao por UN</h3>
        <div class="filter-bar" id="inadFilterBar" style="display:none">
          Filtro ativo: <strong id="inadFilterLabel"></strong>
          <button class="btn-clear" id="inadClearFilter">Limpar</button>
        </div>
        <div class="unid-grid" id="inadUnidGrid"></div>
      </div>
    </div>
    <div class="det-toggle" data-panel="detInad">Ver clientes inadimplentes <span class="det-arrow">▼</span></div>
    <div id="detInad" class="det-panel">
      <div class="search-bar"><input type="text" id="srcInad" placeholder="Buscar cliente..."></div>
      <div class="tscroll"><table class="dtbl">
        <thead><tr><th>#</th><th>Cliente/Hospital</th><th class="c">UN</th>
          <th class="r">Total (R$)</th><th class="c">Notas</th><th>Atraso Máx.</th></tr></thead>
        <tbody id="bodyTblInad"></tbody>
        <tfoot><tr style="background:#FFF0F0">
          <td colspan="3" style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL EXIBIDO</td>
          <td class="val" style="color:var(--red);font-size:15px" id="inadTblTotal">—</td>
          <td colspan="2"></td>
        </tr></tfoot>
      </table></div>
    </div>
  </div>
</div>

<!-- 3. DESPESAS -->
<div class="section-card">
  <div class="sec-head" data-target="bodyDesp">
    <div class="sec-title">
      <div class="sec-icon t">💸</div>
      <div><div class="sec-h2">Despesas do Periodo</div>
           <div class="sec-sub" id="dexpSecSub">—</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Total Despesas</div>
        <div class="sec-total-value t" id="dexpTotalVal">{_def_desp_str}</div></div>
      <div class="sec-total-item"><div class="sec-total-label">Maior categoria</div>
        <div class="sec-total-value t">Compras Revenda</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevDesp">
    <div class="prev-item"><div class="prev-lbl">Total Despesas</div><div class="prev-val" id="prevDespTotal">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Maior categoria</div><div class="prev-val" id="prevDespTopAd">Compras Revenda</div></div>
    <div class="prev-item"><div class="prev-lbl has-tooltip" data-tooltip="(Faturamento − Despesas pagas) / Faturamento × 100">Margem Fat × Desp</div><div class="prev-val"><span class="prev-badge badge-yellow" id="prevDespMargem">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl">Maior UN por custo</div><div class="prev-val" id="prevDespTopUN">—</div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>Top Categorias de Despesa (R$)</h4>
    <div class="mini-chw"><canvas id="chMiniDesp"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodyDesp">
    <div class="insights-row" id="dexpInsightCards"></div>
    <div class="chrow">
      <div class="chbox"><h3>Por Categoria (Adicional)</h3>
        <div class="chw"><canvas id="chDespAd"></canvas></div></div>
      <div class="chbox"><h3>Por Unidade de Negocio</h3>
        <div class="chw"><canvas id="chDespUnid"></canvas></div></div>
    </div>
    <div class="det-toggle" data-panel="detDesp">Ver dados detalhados de despesas <span class="det-arrow">▼</span></div>
    <div id="detDesp" class="det-panel">
      <div class="tabs">
        <button class="tab-btn active" data-pane="pDespHier">Hierarquia</button>
        <button class="tab-btn" data-pane="pDespUnid">Por Unidade</button>
      </div>
      <div id="pDespHier" class="tab-pane active">
        <div class="tscroll"><table class="dtbl">
          <thead><tr><th>Adicional / Subsetor / Nome</th><th class="r">Valor (R$)</th><th class="r">%</th><th class="c">Detalhe</th></tr></thead>
          <tbody id="bodyTblDesp"></tbody>
          <tfoot><tr style="background:#FFFDE7">
            <td style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL GERAL</td>
            <td class="val" id="dexpTblTotal" style="color:#B8860B;font-size:15px">—</td>
            <td colspan="2"></td>
          </tr></tfoot>
        </table></div>
      </div>
      <div id="pDespUnid" class="tab-pane">
        <div id="despUnidAccordion"></div>
      </div>
    </div>
  </div>
</div>

<!-- 4. FATURAMENTO -->
<div class="section-card">
  <div class="sec-head" data-target="bodyFat">
    <div class="sec-title">
      <div class="sec-icon g">📈</div>
      <div><div class="sec-h2">Faturamento</div>
           <div class="sec-sub" id="fatSecSub">—</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Total Faturado</div>
        <div class="sec-total-value g" id="fatTotalVal">{_def_fat_str}</div></div>
      <div class="sec-total-item" style="text-align:right"><div class="sec-total-label">Prazo · NFs</div>
        <div class="sec-total-value g" style="font-size:14px" id="fatPrazoVal">— dias</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevFat">
    <div class="prev-item"><div class="prev-lbl">Top Unidade</div><div class="prev-val" id="prevFatTopUN">—</div></div>
    <div class="prev-item"><div class="prev-lbl">2ª Unidade</div><div class="prev-val" id="prevFatTop2">—</div></div>
    <div class="prev-item"><div class="prev-lbl has-tooltip" data-tooltip="(Faturamento − Despesas pagas) / Faturamento × 100">Margem Fat × Desp</div><div class="prev-val"><span class="prev-badge badge-green" id="prevFatMargem">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl has-tooltip" data-tooltip="100% − (Inadimplência total / Faturamento acumulado 2026)">Índice Recebimento</div><div class="prev-val"><span class="prev-badge badge-teal" id="prevFatRec">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl">Prazo médio NF</div><div class="prev-val" id="prevFatPrazo">—</div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>Faturamento por Unidade (R$)</h4>
    <div class="mini-chw"><canvas id="chMiniFat"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodyFat">
    <div class="insights-row" id="fatInsightCards"></div>
    <div class="chrow">
      <div class="chbox"><h3>Por Unidade de Negocio</h3>
        <div class="chw" style="height:200px"><canvas id="chFatUnid"></canvas></div></div>
      <div class="chbox"><h3>Por Grupo de Produto</h3>
        <div class="chw" style="height:200px"><canvas id="chFatGrupo"></canvas></div></div>
    </div>
    <div class="det-toggle" data-panel="detFat">Ver dados detalhados de faturamento <span class="det-arrow">▼</span></div>
    <div id="detFat" class="det-panel">
      <div class="tabs">
        <button class="tab-btn active" data-pane="pFatUnid">Por Unidade</button>
        <button class="tab-btn" data-pane="pFatGrupo">Tipo de Cirurgia</button>
        <button class="tab-btn" data-pane="pFatCliente">Por Cliente</button>
        <button class="tab-btn" data-pane="pFatPrazo">Prazo NF</button>
      </div>
      <div id="pFatUnid" class="tab-pane active">
        <div class="unid-grid" id="fatUnidGrid"></div>
        <div style="margin-top:16px"><div class="tscroll"><table class="dtbl">
          <thead><tr><th>#</th><th>Unidade</th><th class="r">Faturamento (R$)</th><th class="r">%</th></tr></thead>
          <tbody id="bodyTblFatUnid"></tbody>
          <tfoot><tr style="background:#F0FFF4">
            <td colspan="2" style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL</td>
            <td class="val" id="fatUnidTotal" style="color:#2E9E38;font-size:15px">—</td>
            <td></td>
          </tr></tfoot>
        </table></div></div>
      </div>
      <div id="pFatGrupo" class="tab-pane">
        <div class="tscroll"><table class="dtbl">
          <thead><tr><th>Grupo</th><th class="r">Faturamento (R$)</th><th class="r">%</th><th class="c">NFs</th><th class="c">Prods</th></tr></thead>
          <tbody id="bodyTblFatGrupo"></tbody>
          <tfoot><tr style="background:#F0FFF4">
            <td style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL</td>
            <td class="val" id="fatGrupoTotal" style="color:#2E9E38;font-size:15px">—</td>
            <td colspan="3"></td>
          </tr></tfoot>
        </table></div>
      </div>
      <div id="pFatCliente" class="tab-pane">
        <div style="font-size:12px;color:var(--muted);margin-bottom:10px">Dados de referencia Mai/26</div>
        <div class="search-bar"><input type="text" id="srcFatCli" placeholder="Buscar cliente..."></div>
        <div class="tscroll"><table class="dtbl" id="tblFatCli">
          <thead><tr><th>#</th><th>Cliente</th><th class="r">Fat. (R$)</th><th class="r">%</th><th class="c">Detalhe</th></tr></thead>
          <tbody id="bodyTblFatCli"></tbody>
          <tfoot><tr style="background:#F0FFF4">
            <td colspan="2" style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL</td>
            <td class="val" id="fatCliTotal" style="color:#2E9E38;font-size:15px">—</td>
            <td colspan="2"></td>
          </tr></tfoot>
        </table></div>
      </div>
      <div id="pFatPrazo" class="tab-pane">
        <div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap">
          <div class="days-box">
            <div class="days-big" id="fatPrazoBig">—</div>
            <div style="font-size:14px;color:var(--muted);margin-top:6px">dias em media</div>
            <div style="font-size:12px;color:var(--muted);margin-top:8px">Da cirurgia ate a<br>emissao da NF</div>
          </div>
          <div style="flex:1;min-width:240px"><div style="height:200px"><canvas id="chDiasNF"></canvas></div></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 5. CIRURGIAS -->
<div class="section-card">
  <div class="sec-head" data-target="bodyCir">
    <div class="sec-title">
      <div class="sec-icon b">🏥</div>
      <div><div class="sec-h2">Cirurgias</div>
           <div class="sec-sub" id="cirSecSub">—</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Faturamento</div>
        <div class="sec-total-value b" id="cirTotalVal">—</div></div>
      <div class="sec-total-item"><div class="sec-total-label">Top Tipo</div>
        <div class="sec-total-value b">Protese Inflavel</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevCir">
    <div class="prev-item"><div class="prev-lbl">Faturamento Cirurgias</div><div class="prev-val" id="prevCirTotal">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Top tipo</div><div class="prev-val" id="prevCirTopTipo">Prótese Peniana Inflável</div></div>
    <div class="prev-item"><div class="prev-lbl">Top convenio</div><div class="prev-val" id="prevCirTopConv">PARTICULAR</div></div>
    <div class="prev-item"><div class="prev-lbl">Top unidade</div><div class="prev-val" id="prevCirTopUN">RS</div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>Top 5 Tipos de Cirurgia</h4>
    <div class="mini-chw"><canvas id="chMiniCir"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodyCir">
    <div class="insights-row" id="cirInsightCards"></div>
    <div class="chrow">
      <div class="chbox"><h3>Cirurgias por Tipo (Quantidade)</h3>
        <div class="chw" style="height:340px"><canvas id="chCirTipo"></canvas></div></div>
      <div class="chbox"><h3>Por Convenio</h3>
        <div class="chw" style="height:240px"><canvas id="chCirConv"></canvas></div></div>
    </div>
    <div class="det-toggle" data-panel="detCir">Ver dados detalhados de cirurgias <span class="det-arrow">▼</span></div>
    <div id="detCir" class="det-panel">
      <div class="tabs">
        <button class="tab-btn active" data-pane="pCirUnid">Por Unidade</button>
        <button class="tab-btn" data-pane="pCirTipo">Por Tipo</button>
        <button class="tab-btn" data-pane="pCirHosp">Por Hospital</button>
        <button class="tab-btn" data-pane="pCirConv">Por Convenio</button>
        <button class="tab-btn" data-pane="pCirVend">Por Médico / Vendedor</button>
      </div>
      <div id="pCirUnid" class="tab-pane active"><div id="cirUnidAccordion"></div></div>
      <div id="pCirTipo" class="tab-pane">
        <div class="tscroll"><table class="dtbl">
          <thead><tr><th>Tipo de Cirurgia</th><th class="c">Qtd</th><th class="r">%</th><th class="r">Valor (R$)</th></tr></thead>
          <tbody id="bodyTblCirTipo"></tbody>
          <tfoot><tr style="background:#EEF2FF">
            <td style="padding:8px 12px;font-weight:700;color:var(--navy)">TOTAL</td>
            <td class="val" id="cirTipoTotal" style="color:var(--blue);font-size:15px">—</td>
            <td colspan="2"></td>
          </tr></tfoot>
        </table></div>
      </div>
      <div id="pCirHosp" class="tab-pane">
        <div class="chw" style="height:220px;margin-bottom:16px"><canvas id="chCirHosp"></canvas></div>
        <div class="tscroll"><table class="dtbl">
          <thead><tr><th>#</th><th>Hospital</th><th class="r">Valor (R$)</th><th class="r">%</th></tr></thead>
          <tbody id="bodyTblCirHosp"></tbody>
        </table></div>
      </div>
      <div id="pCirConv" class="tab-pane">
        <div class="tscroll"><table class="dtbl">
          <thead><tr><th>#</th><th>Convenio</th><th class="r">Valor (R$)</th><th class="r">%</th></tr></thead>
          <tbody id="bodyTblCirConv"></tbody>
        </table></div>
      </div>
      <div id="pCirVend" class="tab-pane">
        <div style="font-size:12px;color:var(--muted);margin-bottom:12px">👨‍⚕️ <strong>Médico/Vendedor responsável</strong> — agrupado por nome, com produtos e clientes atendidos. Campo <em>Med</em> = nome do médico ou representante comercial.</div>
        <div id="cirVendAccordion"></div>
      </div>
    </div>
  </div>
</div>

<!-- 6. FLUXO DE CAIXA -->
<div class="section-card">
  <div class="sec-head" data-target="bodyFluxo">
    <div class="sec-title">
      <div class="sec-icon t">💸</div>
      <div><div class="sec-h2">Fluxo de Caixa</div>
           <div class="sec-sub" id="fluxoSecSub">Contas a pagar/receber e movimentos do período</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Saldo Liquido</div>
        <div class="sec-total-value t" id="fluxoSaldoLiq">—</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevFluxo">
    <div class="prev-item"><div class="prev-lbl">A Receber (pendente)</div><div class="prev-val" id="prevFluxoRec">—</div></div>
    <div class="prev-item"><div class="prev-lbl">A Pagar (pendente)</div><div class="prev-val" id="prevFluxoPag">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Saldo Líquido Fluxo</div><div class="prev-val"><span class="prev-badge badge-teal" id="prevFluxoSaldo">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl">Entradas (Fat) vs Saídas (Desp) Mai/26</div>
      <div class="prev-val"><span id="prevFluxoEntSai">—</span></div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>Faturamento × Despesas — Mensal 2026</h4>
    <div class="mini-chw" style="height:160px"><canvas id="chMiniFluxo"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodyFluxo">
    <div class="tabs">
      <button class="tab-btn active" data-pane="pFluxoHist">⬅️ Histórico (Entradas × Saídas)</button>
      <button class="tab-btn" data-pane="pFluxoPend">➡️ Pendente / Futuro</button>
    </div>
    <!-- HISTÓRICO -->
    <div id="pFluxoHist" class="tab-pane active">
      <div class="insights-row" id="fluxoHistKpis"></div>
      <div class="chrow">
        <div class="chbox" style="flex:2;min-width:300px">
          <h3>📊 Entradas (Faturamento) × Saídas (Despesas) — Mensal 2026</h3>
          <div class="chw" style="height:260px"><canvas id="chFluxoHist"></canvas></div>
        </div>
        <div class="chbox" style="flex:1;min-width:220px">
          <h3>📈 Margem por Período</h3>
          <div id="fluxoMargemList" style="margin-top:8px"></div>
        </div>
      </div>
    </div>
    <!-- PENDENTE / FUTURO -->
    <div id="pFluxoPend" class="tab-pane">
      <div class="insights-row" id="fluxoKpis"></div>
      <div class="chrow">
        <div class="chbox" style="flex:1">
          <h3>💡 Análise de Liquidez</h3>
          <div id="fluxoAnalise" style="font-size:13px;line-height:1.7;color:var(--text)"></div>
        </div>
        <div class="chbox" style="flex:1">
          <h3>📋 Faturamento Pendente por Unidade</h3>
          <div class="tscroll"><table class="dtbl">
            <thead><tr><th>Unidade</th><th class="r">Pendente (R$)</th><th class="c">Processos</th></tr></thead>
            <tbody id="bodyFatPendente"></tbody>
            <tfoot><tr style="background:#E6FFFF">
              <td style="padding:8px 12px;font-weight:700">TOTAL</td>
              <td class="val" id="fatPendenteTotal" style="color:#009999;font-size:15px">—</td>
              <td></td>
            </tr></tfoot>
          </table></div>
          <div style="font-size:11px;color:var(--muted);margin-top:8px">Acesse <a href="https://bi.emultec.com.br/dashboard/92" target="_blank" style="color:var(--blue)">dashboard/92</a> para valores em tempo real</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 7. SALDO BANCÁRIO -->
<div class="section-card">
  <div class="sec-head" data-target="bodySaldo">
    <div class="sec-title">
      <div class="sec-icon b">🏦</div>
      <div><div class="sec-h2">Saldo Bancário</div>
           <div class="sec-sub" id="saldoSecSub">Posição consolidada — Conta Corrente + Investimentos</div></div>
    </div>
    <div class="sec-totals">
      <div class="sec-total-item"><div class="sec-total-label">Consolidado</div>
        <div class="sec-total-value b" id="saldoTotalVal">—</div></div>
      <div class="sec-total-item"><div class="sec-total-label">Conta Corrente</div>
        <div class="sec-total-value g" id="saldoCCVal">—</div></div>
    </div>
    <div class="expand-btn">▼</div>
  </div>
  <div class="sec-preview" id="prevSaldo">
    <div class="prev-item"><div class="prev-lbl">CC Total</div><div class="prev-val" id="prevSaldoCC">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Investimentos</div><div class="prev-val" id="prevSaldoInvest">—</div></div>
    <div class="prev-item"><div class="prev-lbl">Total Consolidado</div><div class="prev-val"><span class="prev-badge badge-blue" id="prevSaldoTotal">—</span></div></div>
    <div class="prev-item"><div class="prev-lbl">Referência</div><div class="prev-val" style="font-size:13px;font-weight:600;color:var(--muted)" id="prevSaldoRef">—</div></div>
  </div>
  <div class="mini-ch"><div class="mini-ch-inner">
    <h4>CC × Investimentos por Banco</h4>
    <div class="mini-chw" style="height:160px"><canvas id="chMiniSaldo"></canvas></div>
  </div></div>
  <div class="sec-body" id="bodySaldo">
    <div class="insights-row" id="saldoContaCards"></div>
    <div class="det-toggle" data-panel="detSaldo">Ver detalhamento por conta (CC + Investimentos) <span class="det-arrow">▼</span></div>
    <div id="detSaldo" class="det-panel">
      <div id="saldoAccordion"></div>
      <div style="margin-top:14px;padding:12px 16px;background:#FFFDE7;border-radius:8px;border-left:3px solid var(--yellow);font-size:12px">
        ⚠️ <strong>Nota:</strong> Exclui conta PR (Santander 130071322 — sem extrato disponível) e saldo de fabricante em custódia na XP (R$&nbsp;139.627,25 — não pertence à empresa).
        Ref: <strong id="saldoRefNote">—</strong> &nbsp;|&nbsp;
        <a href="https://bi.emultec.com.br/dashboard/55" target="_blank" style="color:var(--blue)">dashboard/55</a>
      </div>
    </div>
  </div>
</div>


</div>
<div class="footer">Dashboard Executivo Magnum Import &middot; bi.emultec.com.br &middot; {_today_str}</div>

<script>
const TODAY=new Date('2026-05-22');
const COLORS=['#00CCCC','#476AAE','#4FC454','#E8AF1B','#E05050','#9B59B6','#E67E22','#1ABC9C','#3498DB','#E91E63','#FF9800','#607D8B'];

const INAD={inad_js};
const INAD_UN={inad_unid_js};
const FAT_PER={fat_per_js};
const DESP_PER={desp_per_js};
const FAT_CL={fat_cl_js};
const CIR_TI={cir_tipo_js};
const CIR_HO={cir_hosp_js};
const CIR_CO={cir_conv_js};
const CIR_UN={cir_unid_js};
const FAT_EVOL = {fat_evol_js};
const SALDO_BANC={saldo_banc_js};
const FLUXO={fluxo_js};
const FAT_PEND={fat_pend_js};

var PERIODOS_MENSAIS={_periodos_mensais_str};
var PERIODOS_TRIM={_periodos_trim_str};
var CUR='{_DEF_PERIOD}';
var activeUnit=null;
var charts={{}};

function fmtN(v){{return Number(v).toLocaleString('pt-BR',{{minimumFractionDigits:2,maximumFractionDigits:2}});}}
function parseDate(s){{if(!s)return null;var p=s.split('/');return new Date(+p[2],+p[1]-1,+p[0]);}}
function diffDays(d1,d2){{return Math.round((d2-d1)/86400000);}}
function pct(v,tot){{return tot>0?(v/tot*100).toFixed(1):'0.0';}}
function parseVal(s){{return parseFloat(String(s).replace(/\./g,'').replace(',','.'));}}
function delayBadge(d){{
  if(d>365)return '<span class="bdg bdg-r">+1 ano ('+d+'d)</span>';
  if(d>180)return '<span class="bdg bdg-r">'+d+' dias</span>';
  if(d>90) return '<span class="bdg bdg-o">'+d+' dias</span>';
  if(d>30) return '<span class="bdg bdg-y">'+d+' dias</span>';
  return '<span class="bdg bdg-gray">'+d+' dias</span>';
}}
function bar(v,tot,color){{
  var w=Math.max(2,Math.round(parseFloat(pct(v,tot))*1.5));
  return '<div style="display:flex;align-items:center;gap:5px;justify-content:flex-end">'+
    '<div style="background:'+color+';height:10px;width:'+w+'px;border-radius:3px;opacity:.65"></div>'+pct(v,tot)+'%</div>';
}}
function mkChart(id,cfg){{
  if(charts[id])charts[id].destroy();
  charts[id]=new Chart(document.getElementById(id),cfg);
  return charts[id];
}}

// Section toggles
document.querySelectorAll('.sec-head').forEach(function(h){{
  h.addEventListener('click',function(){{
    h.classList.toggle('open');
    document.getElementById(h.dataset.target).classList.toggle('open');
  }});
}});
// Tab buttons
document.addEventListener('click',function(e){{
  var btn=e.target.closest('.tab-btn');
  if(!btn)return;
  var par=btn.closest('.det-panel')||btn.closest('.sec-body');
  par.querySelectorAll('.tab-btn').forEach(function(b){{b.classList.remove('active');}});
  par.querySelectorAll('.tab-pane').forEach(function(p){{p.classList.remove('active');}});
  btn.classList.add('active');
  document.getElementById(btn.dataset.pane).classList.add('active');
}});
// Detail toggles
document.querySelectorAll('.det-toggle').forEach(function(t){{
  t.addEventListener('click',function(){{
    t.classList.toggle('open');
    var p=document.getElementById(t.dataset.panel);
    p.style.display=p.style.display==='block'?'none':'block';
  }});
}});
// Expand rows
function toggleExp(id){{
  var el=document.getElementById(id);var ic=document.getElementById('icon-'+id);
  if(!el)return;
  if(el.style.display==='table-row'){{el.style.display='none';if(ic)ic.textContent='▶';}}
  else{{el.style.display='table-row';if(ic)ic.textContent='▼';}}
}}
// ── Seletor dinâmico de períodos ──────────────────────
function renderPeriodBar(){{
  var cont=document.getElementById('period-chips-container');
  if(!cont)return;
  cont.innerHTML='';
  var recent=PERIODOS_MENSAIS.slice(-3);
  var historic=PERIODOS_MENSAIS.slice(0,PERIODOS_MENSAIS.length-3);
  if(historic.length>0){{
    var sel=document.createElement('select');
    sel.className='period-hist-select';
    var defOpt=document.createElement('option');
    defOpt.value='';
    defOpt.textContent='📁 Histórico';
    sel.appendChild(defOpt);
    historic.forEach(function(p){{
      var opt=document.createElement('option');
      opt.value=p.key;
      opt.textContent=p.label;
      sel.appendChild(opt);
    }});
    sel.addEventListener('change',function(){{
      if(this.value){{setActivePeriod(this.value);this.value='';}}
    }});
    cont.appendChild(sel);
  }}
  recent.forEach(function(p){{
    var btn=document.createElement('button');
    btn.className='period-chip'+(p.key===CUR?' active':'');
    btn.setAttribute('data-key',p.key);
    btn.textContent=p.label;
    btn.addEventListener('click',function(){{setActivePeriod(p.key);}});
    cont.appendChild(btn);
  }});
  if(PERIODOS_TRIM.length>0){{
    var sep=document.createElement('div');
    sep.style.cssText='width:1px;background:var(--border);margin:0 4px;align-self:stretch;';
    cont.appendChild(sep);
    PERIODOS_TRIM.forEach(function(p){{
      var btn=document.createElement('button');
      btn.className='period-chip trim'+(p.key===CUR?' active':'');
      btn.setAttribute('data-key',p.key);
      btn.textContent=p.label;
      btn.addEventListener('click',function(){{setActivePeriod(p.key);}});
      cont.appendChild(btn);
    }});
  }}
}}
function _keyToLabel(key){{
  var m={{jan:'Jan',fev:'Fev',mar:'Mar',abr:'Abr',mai:'Mai',jun:'Jun',jul:'Jul',ago:'Ago',set:'Set',out:'Out',nov:'Nov',dez:'Dez'}};
  var pfx=key.slice(0,3),yr=key.slice(3);
  return (m[pfx]||pfx.charAt(0).toUpperCase()+pfx.slice(1))+'/'+yr;
}}
function setActivePeriod(key){{
  // Sempre atualiza botão ativo
  document.querySelectorAll('.period-chip').forEach(function(c){{c.classList.remove('active');}});
  var chip=document.querySelector('[data-key="'+key+'"]');
  if(chip)chip.classList.add('active');
  // Atualiza badge
  var lbl=FAT_PER[key]?FAT_PER[key].label:_keyToLabel(key);
  document.getElementById('periodLabel').textContent=lbl;
  if(!FAT_PER[key]){{
    // Sem dados: limpar cards e mostrar aviso
    document.getElementById('kpiFatValue').textContent='—';
    document.getElementById('kpiFatSub').textContent=lbl+' · sem dados offline';
    document.getElementById('kpiDespValue').textContent='—';
    document.getElementById('kpiDespSub').textContent=lbl+' · sem dados offline';
    document.getElementById('kpiPrazo').textContent='—';
    document.getElementById('kpiPrazoSub').textContent=lbl;
    document.getElementById('fatSecSub').textContent=lbl+' — dados não carregados offline';
    document.getElementById('cirSecSub').textContent=lbl+' — dados não carregados offline';
    document.getElementById('dexpSecSub').textContent=lbl+' — dados não carregados offline';
    var msg=document.getElementById('_nodata_toast');
    if(!msg){{msg=document.createElement('div');msg.id='_nodata_toast';
      msg.style.cssText='position:fixed;top:80px;left:50%;transform:translateX(-50%);background:#1a3066;color:#fff;padding:14px 28px;border-radius:10px;font-size:14px;font-weight:700;z-index:9999;box-shadow:0 4px 16px rgba(0,0,0,.3);';
      document.body.appendChild(msg);}}
    msg.textContent='📊 '+lbl+' — histórico não carregado. Os dados do BI são coletados mensalmente.';
    msg.style.display='block';
    setTimeout(function(){{msg.style.display='none';}},4000);
    return;
  }}
  CUR=key;
  setPeriod(key);
}}

// =============================================
// SET PERIOD — rebuilds EVERYTHING
// =============================================
function setPeriod(key){{
  CUR=key;
  var fp=FAT_PER[key];
  var dp=DESP_PER[key]||{{total:0,label:fp?fp.label:'—',byUN:[['—',0]],byAd:[]}};
  // Badge
  document.getElementById('periodLabel').textContent=fp.label;
  // KPIs
  document.getElementById('kpiFatValue').textContent='R$ '+fmtN(fp.total);
  document.getElementById('kpiFatSub').textContent=fp.nf_count+' NFs · '+fp.label;
  document.getElementById('kpiDespValue').textContent='R$ '+fmtN(dp.total);
  document.getElementById('kpiDespSub').textContent=dp.label+' · todas categorias';
  document.getElementById('kpiPrazo').textContent=fp.prazo+' dias';
  document.getElementById('kpiPrazoSub').textContent='Media '+fp.label;
  // Section headers
  document.getElementById('fatSecSub').textContent=fp.label+' — '+fp.nf_count+' notas fiscais emitidas';
  document.getElementById('cirSecSub').textContent=fp.label+' — por tipo, hospital, convenio e unidade';
  document.getElementById('dexpSecSub').textContent=dp.label+' — todas as categorias';
  document.getElementById('inadSecSub').textContent='Titulos com vencimento em '+fp.label+' — ordenados por atraso';
  // Section totals
  document.getElementById('fatTotalVal').textContent='R$ '+fmtN(fp.total);
  document.getElementById('fatPrazoVal').textContent=fp.prazo+' dias · '+fp.nf_count+' NFs';
  document.getElementById('dexpTotalVal').textContent='R$ '+fmtN(dp.total);
  document.getElementById('cirTotalVal').textContent='R$ '+fmtN(fp.total);
  document.getElementById('fatPrazoBig').textContent=fp.prazo;
  // Rebuild all sections
  buildInad();
  buildDesp();
  buildFat();
  buildCirInsights();
  try{{buildFatCharts();}}catch(e){{console.warn('buildFatCharts',e);}}
  try{{buildDespCharts();}}catch(e){{console.warn('buildDespCharts',e);}}
  // buildEvol e buildPreviews após layout completo
  var _doEvol=function(){{
    try{{buildEvol();}}catch(e){{console.warn('buildEvol',e);}}
    try{{buildPreviews();}}catch(e){{console.warn('buildPreviews',e);}}
  }};
  if(document.readyState==='complete'){{_doEvol();}}
  else{{window.addEventListener('load',_doEvol);}}
  // Fallback com timeout maior
  setTimeout(_doEvol, 500);
  try{{buildMiniCharts();}}catch(e){{console.warn('buildMiniCharts',e);}}
}}

function setupSearch(inId,tbId){{
  var el=document.getElementById(inId);if(!el)return;
  el.addEventListener('keyup',function(){{
    var q=el.value.toLowerCase();
    document.getElementById(tbId).querySelectorAll('tr.data-row').forEach(function(row){{
      var show=!q||row.textContent.toLowerCase().includes(q);
      row.style.display=show?'':'none';
      var nxt=row.nextElementSibling;
      if(nxt&&nxt.classList.contains('exp-row'))nxt.style.display=show?nxt.style.display:'none';
    }});
  }});
}}

// =============================================
// INADIMPLENTES
// =============================================
function buildInad(){{
  // Group rows by hospital name
  var rows=INAD.slice();
  var filtered=rows.filter(function(r){{
    if(activeUnit&&r[1]!==activeUnit)return false;
    return true;
  }});
  // Build grouped map: hospital -> {{unit, total, titles[]}}
  var grp={{}};
  filtered.forEach(function(r){{
    var key=r[0];
    if(!grp[key])grp[key]={{hosp:r[0],unit:r[1],total:0,titles:[],earliest:null}};
    var vn=parseVal(r[2]);
    grp[key].total+=vn;
    grp[key].titles.push(r);
    var d=parseDate(r[3]);
    if(d&&(!grp[key].earliest||d<grp[key].earliest))grp[key].earliest=d;
  }});
  // Sort by total desc
  var groups=Object.values(grp).sort(function(a,b){{return b.total-a.total;}});
  var grandTotal=groups.reduce(function(s,g){{return s+g.total;}},0);
  var html='';
  groups.forEach(function(g,i){{
    var rid='ig'+i;
    var days=g.earliest?diffDays(g.earliest,TODAY):0;
    html+='<tr class="data-row togrow" data-exp="'+rid+'" onclick="toggleExp(this.dataset.exp)">'+
      '<td><span id="icon-'+rid+'" style="font-size:11px;color:var(--red);margin-right:4px">▶</span>'+(i+1)+'</td>'+
      '<td><strong>'+g.hosp+'</strong></td>'+
      '<td class="ctr"><span class="bdg bdg-un">'+g.unit+'</span></td>'+
      '<td class="val" style="color:var(--red)">'+fmtN(g.total)+'</td>'+
      '<td class="ctr"><span class="bdg bdg-r">'+g.titles.length+' nota'+(g.titles.length>1?'s':'')+'</span></td>'+
      '<td>'+delayBadge(days)+'</td></tr>';
    // Expandable sub-rows with individual titles
    var subRows=g.titles.map(function(t){{
      var td=parseDate(t[3]);var td2=td?diffDays(td,TODAY):0;
      return '<tr><td colspan="2">'+t[3]+'</td>'+
        '<td><span class="bdg bdg-t">'+t[4]+'</span></td>'+
        '<td class="val">'+t[2]+'</td>'+
        '<td colspan="2">'+delayBadge(td2)+'</td></tr>';
    }}).join('');
    html+='<tr id="'+rid+'" class="exp-row"><td colspan="6"><div class="exp-inner">'+
      '<table class="sub-tbl"><thead><tr><th colspan="2">Vencimento</th><th>Convenio</th><th class="val">Valor (R$)</th><th colspan="2">Atraso</th></tr></thead>'+
      '<tbody>'+subRows+'</tbody></table></div></td></tr>';
  }});
  if(!html)html='<tr><td colspan="6" style="text-align:center;padding:20px;color:var(--muted)">Nenhum titulo em aberto'+(activeUnit?' para '+activeUnit:'')+'</td></tr>';
  document.getElementById('bodyTblInad').innerHTML=html;
  document.getElementById('inadTblTotal').textContent=fmtN(grandTotal);
  var g2='';
  Object.keys(INAD_UN).sort(function(a,b){{return INAD_UN[b].total-INAD_UN[a].total;}}).forEach(function(un){{
    var v=INAD_UN[un];var ia=(activeUnit===un);
    g2+='<div class="unid-pill'+(ia?' active':'')+'" data-un="'+un+'">'+
      '<div class="u-name">'+un+'</div><div class="u-val">'+fmtN(v.total)+'</div>'+
      '<div class="u-cnt">'+v.count+' titulos</div></div>';
  }});
  document.getElementById('inadUnidGrid').innerHTML=g2;
  var maxUN='',maxVal=0;
  Object.keys(INAD_UN).forEach(function(k){{if(INAD_UN[k].total>maxVal){{maxVal=INAD_UN[k].total;maxUN=k;}}}});
  document.getElementById('inadInsightCards').innerHTML=
    '<div class="insight-card"><div class="insight-icon">🔴</div><div class="insight-val">'+fmtN(maxVal)+'</div>'+
    '<div class="insight-label">'+maxUN+' — maior inadimplencia</div><div class="insight-note">'+INAD_UN[maxUN].count+' titulos</div></div>'+
    '<div class="insight-card"><div class="insight-icon">🏥</div><div class="insight-val">'+groups.length+'</div>'+
    '<div class="insight-label">Clientes inadimplentes</div><div class="insight-note">'+(activeUnit?'Filtro: '+activeUnit:'Todas as unidades')+'</div></div>'+
    '<div class="insight-card"><div class="insight-icon">💰</div><div class="insight-val">R$ {grand_fmt}</div>'+
    '<div class="insight-label">Total inadimplente (BI)</div><div class="insight-note">Todos titulos em aberto</div></div>'+
    '<div class="insight-card"><div class="insight-icon">📋</div><div class="insight-val">'+filtered.length+'</div>'+
    '<div class="insight-label">Titulos em aberto</div><div class="insight-note">'+(activeUnit?'Filtro: '+activeUnit:'Todas as unidades')+'</div></div>';
  document.getElementById('inadUnidGrid').querySelectorAll('.unid-pill').forEach(function(pill){{
    pill.addEventListener('click',function(){{
      var un=pill.dataset.un;activeUnit=(activeUnit===un)?null:un;
      var fb=document.getElementById('inadFilterBar');
      if(activeUnit){{fb.style.display='flex';document.getElementById('inadFilterLabel').textContent=activeUnit;}}
      else fb.style.display='none';
      buildInad();
    }});
  }});
  setupSearch('srcInad','bodyTblInad');
}}
document.getElementById('inadClearFilter').addEventListener('click',function(){{
  activeUnit=null;document.getElementById('inadFilterBar').style.display='none';buildInad();
}});

// =============================================
// DESPESAS
// =============================================
function buildDesp(){{
  var dp=DESP_PER[CUR];
  if(!dp||!dp.byAd||dp.byAd.length===0||!dp.byUN||dp.byUN.length===0){{
    document.getElementById('dexpTblTotal').textContent='—';
    document.getElementById('bodyTblDesp').innerHTML='<tr><td colspan="4" style="text-align:center;color:var(--muted);padding:24px">Sem dados de despesas para este período.</td></tr>';
    document.getElementById('dexpInsightCards').innerHTML='';
    return;
  }}
  var total=dp.total;var byAd=dp.byAd;
  document.getElementById('dexpTblTotal').textContent=fmtN(total);
  // Hierarchy tab
  var html='';
  byAd.forEach(function(d,i){{
    var rowId='dexp'+i;
    var subs={{}};
    d.top.forEach(function(t){{var s=t[2]||'Outros';if(!subs[s])subs[s]={{val:0,nomes:[]}};subs[s].val+=t[1];subs[s].nomes.push([t[0],t[1]]);}} );
    var sk=Object.keys(subs);
    html+='<tr class="data-row togrow" data-exp="'+rowId+'" onclick="toggleExp(this.dataset.exp)">'+
      '<td><span id="icon-'+rowId+'" style="font-size:11px;color:var(--teal);margin-right:4px">▶</span><strong style="color:var(--navy)">'+d.ad+'</strong></td>'+
      '<td class="val">'+fmtN(d.val)+'</td><td>'+bar(d.val,total,'var(--teal)')+'</td>'+
      '<td class="ctr"><span class="bdg bdg-t">'+sk.length+' sub</span></td></tr>';
    var inner='';
    sk.forEach(function(s,si){{
      var sub=subs[s];var sid='dsub'+i+'_'+si;
      inner+='<tr class="togrow" data-exp="'+sid+'" onclick="toggleExp(this.dataset.exp)" style="background:#F0F4FA">'+
        '<td style="padding:6px 10px 6px 28px"><span id="icon-'+sid+'" style="font-size:10px;color:var(--blue);margin-right:4px">▶</span><em style="color:var(--blue)">'+s+'</em></td>'+
        '<td class="val" style="font-size:12px">'+fmtN(sub.val)+'</td>'+
        '<td>'+bar(sub.val,total,'var(--blue)')+'</td>'+
        '<td class="ctr"><span class="bdg bdg-b">'+sub.nomes.length+' nomes</span></td></tr>'+
        '<tr id="'+sid+'" class="exp-row"><td colspan="4"><div class="exp-inner">'+
        '<table class="sub-tbl"><thead><tr><th>Nome / Fornecedor</th><th class="val">Valor (R$)</th></tr></thead><tbody>'+
        sub.nomes.map(function(n){{return '<tr><td>'+n[0]+'</td><td class="val">'+fmtN(n[1])+'</td></tr>';}}).join('')+
        '</tbody></table></div></td></tr>';
    }});
    html+='<tr id="'+rowId+'" class="exp-row"><td colspan="4"><div class="exp-inner" style="padding:0">'+
      '<table class="dtbl" style="font-size:12px">'+inner+'</table></div></td></tr>';
  }});
  document.getElementById('bodyTblDesp').innerHTML=html;
  // Por Unidade tab — accordion with byAd breakdown per unit
  buildDespUnidAccordion(dp);
  // Insights
  var tc=byAd[0];var tu=dp.byUN[0];
  document.getElementById('dexpInsightCards').innerHTML=
    '<div class="insight-card"><div class="insight-icon">🛒</div><div class="insight-val">'+pct(tc.val,total)+'%</div>'+
    '<div class="insight-label">'+tc.ad+'</div><div class="insight-note">R$ '+fmtN(tc.val)+' — maior cat.</div></div>'+
    '<div class="insight-card"><div class="insight-icon">🏢</div><div class="insight-val">'+tu[0]+'</div>'+
    '<div class="insight-label">Maior unidade</div><div class="insight-note">R$ '+fmtN(tu[1])+' ('+pct(tu[1],total)+'%)</div></div>'+
    '<div class="insight-card"><div class="insight-icon">📦</div><div class="insight-val">'+byAd.length+' categ.</div>'+
    '<div class="insight-label">Tipos de despesa</div><div class="insight-note">'+dp.label+'</div></div>'+
    '<div class="insight-card"><div class="insight-icon">💵</div><div class="insight-val">R$ '+fmtN(total)+'</div>'+
    '<div class="insight-label">Total do periodo</div><div class="insight-note">'+dp.label+'</div></div>';
}}

// =============================================
// FATURAMENTO
// =============================================
function buildFat(){{
  var fp=FAT_PER[CUR];var total=fp.total;var byUN=fp.byUN;
  var byGrupo=fp.byGrupo||[];
  // Update footer totals
  document.getElementById('fatUnidTotal').textContent=fmtN(total);
  document.getElementById('fatGrupoTotal').textContent=fmtN(total);
  document.getElementById('fatCliTotal').textContent=fmtN(total);
  // Por Unidade
  document.getElementById('fatUnidGrid').innerHTML=byUN.map(function(d){{
    return '<div class="unid-pill" style="cursor:default"><div class="u-name">'+d[0]+'</div>'+
      '<div class="u-val">'+fmtN(d[1])+'</div><div class="u-cnt">'+pct(d[1],total)+'%</div></div>';
  }}).join('');
  document.getElementById('bodyTblFatUnid').innerHTML=byUN.map(function(d,i){{
    return '<tr><td>'+(i+1)+'</td><td><strong>'+d[0]+'</strong></td>'+
      '<td class="val">'+fmtN(d[1])+'</td><td>'+bar(d[1],total,'var(--green)')+'</td></tr>';
  }}).join('');
  // Por Grupo — real per-period data
  var html='';
  byGrupo.forEach(function(g,i){{
    var rid='fgr'+i;
    html+='<tr class="data-row togrow" data-exp="'+rid+'" onclick="toggleExp(this.dataset.exp)">'+
      '<td><span id="icon-'+rid+'" style="font-size:11px;color:var(--green);margin-right:4px">▶</span><strong>'+g.g+'</strong></td>'+
      '<td class="val">'+fmtN(g.val)+'</td><td>'+bar(g.val,total,'var(--green)')+'</td>'+
      '<td class="ctr">'+g.cnt+'</td><td class="ctr"><span class="bdg bdg-g">'+g.prods.length+' prods</span></td></tr>';
    var prodsHtml=g.prods.length>0
      ? g.prods.map(function(p){{return '<tr><td>'+p[0]+'</td><td class="val">'+fmtN(p[1])+'</td></tr>';}}).join('')
      : '<tr><td colspan="2" style="color:var(--muted);font-style:italic;padding:6px 10px">Detalhes nao disponíveis</td></tr>';
    html+='<tr id="'+rid+'" class="exp-row"><td colspan="5"><div class="exp-inner">'+
      '<table class="sub-tbl"><thead><tr><th>Produto</th><th class="val">Valor (R$)</th></tr></thead><tbody>'+
      prodsHtml+'</tbody></table></div></td></tr>';
  }});
  document.getElementById('bodyTblFatGrupo').innerHTML=html;
  // Por Cliente (mai26 reference)
  var hc='';
  FAT_CL.forEach(function(c,i){{
    var rid='fcl'+i;
    hc+='<tr class="data-row togrow" data-exp="'+rid+'" onclick="toggleExp(this.dataset.exp)">'+
      '<td><span id="icon-'+rid+'" style="font-size:11px;color:var(--green);margin-right:4px">▶</span>'+(i+1)+'</td>'+
      '<td><strong>'+c.c+'</strong></td><td class="val">'+fmtN(c.val)+'</td>'+
      '<td>'+bar(c.val,total,'var(--green)')+'</td><td class="ctr"><span class="bdg bdg-g">'+c.items.length+' itens</span></td></tr>'+
      '<tr id="'+rid+'" class="exp-row"><td colspan="5"><div class="exp-inner">'+
      '<table class="sub-tbl"><thead><tr><th>Convenio</th><th>Medico/Vendedor</th><th>Produto</th><th>UN</th><th class="val">Valor (R$)</th></tr></thead><tbody>'+
      c.items.map(function(it){{
        return '<tr><td><span class="bdg bdg-t">'+it.conv+'</span></td><td>'+it.med+'</td><td>'+it.prod+'</td>'+
          '<td><span class="bdg bdg-un">'+it.uni+'</span></td><td class="val">'+it.val+'</td></tr>';
      }}).join('')+
      '</tbody></table></div></td></tr>';
  }});
  document.getElementById('bodyTblFatCli').innerHTML=hc;
  setupSearch('srcFatCli','bodyTblFatCli');
  // Insights
  var tu=byUN[0];
  var topGrupo=byGrupo.length>0?byGrupo[0]:{{g:'—',val:0}};
  document.getElementById('fatInsightCards').innerHTML=
    '<div class="insight-card"><div class="insight-icon">🏢</div><div class="insight-val">'+tu[0]+'</div>'+
    '<div class="insight-label">Maior unidade</div><div class="insight-note">R$ '+fmtN(tu[1])+' ('+pct(tu[1],total)+'%)</div></div>'+
    '<div class="insight-card"><div class="insight-icon">🏆</div><div class="insight-val">'+topGrupo.g+'</div>'+
    '<div class="insight-label">Maior grupo</div><div class="insight-note">R$ '+fmtN(topGrupo.val)+' ('+pct(topGrupo.val,total)+'%)</div></div>'+
    '<div class="insight-card"><div class="insight-icon">📄</div><div class="insight-val">'+fp.nf_count+'</div>'+
    '<div class="insight-label">Notas fiscais</div><div class="insight-note">'+fp.label+'</div></div>'+
    '<div class="insight-card"><div class="insight-icon">⏱️</div><div class="insight-val">'+fp.prazo+' dias</div>'+
    '<div class="insight-label">Prazo Cirug./NF</div><div class="insight-note">Media '+fp.label+'</div></div>';
}}

// =============================================
// CIRURGIAS
// =============================================
function buildCirInsights(){{
  var fp=FAT_PER[CUR];
  document.getElementById('cirInsightCards').innerHTML=
    '<div class="insight-card"><div class="insight-icon">🥇</div><div class="insight-val">Protese Inflavel</div>'+
    '<div class="insight-label">Maior valor</div><div class="insight-note">'+fp.label+'</div></div>'+
    '<div class="insight-card"><div class="insight-icon">📊</div><div class="insight-val">Flexivel</div>'+
    '<div class="insight-label">Mais frequente</div><div class="insight-note">~59 procedimentos</div></div>'+
    '<div class="insight-card"><div class="insight-icon">🏦</div><div class="insight-val">PARTICULAR</div>'+
    '<div class="insight-label">Top convenio</div><div class="insight-note">~29% do total</div></div>'+
    '<div class="insight-card"><div class="insight-icon">💰</div><div class="insight-val">R$ '+fmtN(fp.total)+'</div>'+
    '<div class="insight-label">Faturamento '+fp.label+'</div><div class="insight-note">Total do periodo</div></div>';
}}

function buildCir(){{
  var totalVal=CIR_TI.reduce(function(s,r){{return s+r[1];}},0);
  var totalQtd=CIR_TI.reduce(function(s,r){{return s+r[2];}},0);
  var sorted=CIR_TI.slice().sort(function(a,b){{return b[2]-a[2];}});
  document.getElementById('bodyTblCirTipo').innerHTML=sorted.map(function(r){{
    return '<tr class="data-row"><td>'+r[0]+'</td>'+
      '<td class="ctr"><span class="bdg bdg-b" style="min-width:32px;text-align:center">'+r[2]+'</span></td>'+
      '<td>'+bar(r[2],totalQtd,'var(--blue)')+'</td>'+
      '<td class="val" style="font-size:12px;color:var(--muted)">'+fmtN(r[1])+'</td></tr>';
  }}).join('');
  document.getElementById('cirTipoTotal').textContent=totalQtd+' cirurgias';
  var totalHo=CIR_HO.reduce(function(s,r){{return s+r[1];}},0);
  var totalCo=CIR_CO.reduce(function(s,r){{return s+r[1];}},0);
  document.getElementById('bodyTblCirHosp').innerHTML=CIR_HO.map(function(r,i){{
    return '<tr><td>'+(i+1)+'</td><td>'+r[0]+'</td><td class="val">'+fmtN(r[1])+'</td>'+
      '<td>'+bar(r[1],totalHo,'var(--blue)')+'</td></tr>';
  }}).join('');
  document.getElementById('bodyTblCirConv').innerHTML=CIR_CO.map(function(r,i){{
    return '<tr><td>'+(i+1)+'</td><td>'+r[0]+'</td><td class="val">'+fmtN(r[1])+'</td>'+
      '<td>'+bar(r[1],totalCo,'var(--teal)')+'</td></tr>';
  }}).join('');
  var uHtml='';
  CIR_UN.forEach(function(un,i){{
    uHtml+='<div style="margin-bottom:8px;border:1px solid var(--border);border-radius:8px;overflow:hidden">'+
      '<div onclick="toggleCirUn('+i+')" style="padding:12px 18px;background:var(--bg);display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none">'+
        '<div style="display:flex;align-items:center;gap:10px">'+
          '<span id="cunIco'+i+'" style="color:var(--blue);font-size:13px">▶</span>'+
          '<strong style="font-size:15px;color:var(--navy)">'+un.un+'</strong>'+
          '<span class="bdg bdg-b">'+un.tipos.reduce(function(s,t){{return s+t[2];}},0)+' cirurgias</span>'+
          '<span class="bdg bdg-t" style="font-size:10px">'+un.tipos.length+' tipos</span>'+
        '</div>'+
        '<span style="font-weight:900;font-family:monospace;font-size:16px;color:var(--blue)">R$ '+fmtN(un.val)+'</span>'+
      '</div>'+
      '<div id="cunBody'+i+'" style="display:none;padding:12px">'+
        '<table class="dtbl" style="font-size:13px">'+
        '<thead><tr><th>Tipo de Cirurgia</th><th class="r">Valor (R$)</th><th class="r">%</th><th class="c">Qtd</th></tr></thead><tbody>'+
        un.tipos.map(function(t){{
          return '<tr><td>'+t[0]+'</td><td class="val">'+fmtN(t[1])+'</td>'+
            '<td>'+bar(t[1],un.val,'var(--blue)')+'</td>'+
            '<td class="ctr"><span class="bdg bdg-b">'+t[2]+'</span></td></tr>';
        }}).join('')+
        '</tbody></table></div></div>';
  }});
  document.getElementById('cirUnidAccordion').innerHTML=uHtml;
  var vMap={{}};
  FAT_CL.forEach(function(cl){{
    cl.items.forEach(function(it){{
      var m=it.med;if(!vMap[m])vMap[m]={{val:0,itens:[]}};
      var v=parseVal(it.val);vMap[m].val+=v;
      vMap[m].itens.push({{prod:it.prod,val:v,conv:it.conv,uni:it.uni,cli:cl.c}});
    }});
  }});
  var vk=Object.keys(vMap).sort(function(a,b){{return vMap[b].val-vMap[a].val;}});
  var vHtml='';
  vk.forEach(function(med,i){{
    var vm=vMap[med];
    vHtml+='<div style="margin-bottom:8px;border:1px solid var(--border);border-radius:8px;overflow:hidden">'+
      '<div onclick="toggleCirVend('+i+')" style="padding:12px 18px;background:var(--bg);display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none">'+
        '<div style="display:flex;align-items:center;gap:10px">'+
          '<span id="cvIco'+i+'" style="color:var(--green);font-size:13px">▶</span>'+
          '<strong style="color:var(--navy)">'+med+'</strong>'+
          '<span class="bdg bdg-g">'+vm.itens.length+' vendas</span>'+
        '</div>'+
        '<span style="font-weight:900;font-family:monospace;font-size:16px;color:#2E9E38">R$ '+fmtN(vm.val)+'</span>'+
      '</div>'+
      '<div id="cvBody'+i+'" style="display:none;padding:12px">'+
        '<table class="dtbl" style="font-size:12px"><thead><tr>'+
          '<th>Produto</th><th>Cliente</th><th>Convenio</th><th>UN</th><th class="r">Valor (R$)</th>'+
        '</tr></thead><tbody>'+
        vm.itens.sort(function(a,b){{return b.val-a.val;}}).map(function(it){{
          return '<tr><td>'+it.prod+'</td><td>'+it.cli+'</td>'+
            '<td><span class="bdg bdg-t">'+it.conv+'</span></td>'+
            '<td><span class="bdg bdg-un">'+it.uni+'</span></td>'+
            '<td class="val">'+fmtN(it.val)+'</td></tr>';
        }}).join('')+
        '</tbody></table></div></div>';
  }});
  document.getElementById('cirVendAccordion').innerHTML=vHtml;
}}
function toggleCirUn(i){{var b=document.getElementById('cunBody'+i);var ic=document.getElementById('cunIco'+i);if(!b)return;if(b.style.display==='block'){{b.style.display='none';ic.textContent='▶';}}else{{b.style.display='block';ic.textContent='▼';}}}}
function toggleCirVend(i){{var b=document.getElementById('cvBody'+i);var ic=document.getElementById('cvIco'+i);if(!b)return;if(b.style.display==='block'){{b.style.display='none';ic.textContent='▶';}}else{{b.style.display='block';ic.textContent='▼';}}}}

// =============================================
// CHARTS
// =============================================
function buildFatCharts(){{if(typeof Chart==='undefined')return;
  var fp=FAT_PER[CUR];var byUN=fp.byUN;var byGrupo=fp.byGrupo||[];
  Chart.defaults.font.family="'Segoe UI',Arial,sans-serif";Chart.defaults.font.size=12;
  mkChart('chFatUnid',{{type:'bar',
    data:{{labels:byUN.map(function(d){{return d[0];}}),
      datasets:[{{label:'Fat.',data:byUN.map(function(d){{return d[1];}}),backgroundColor:COLORS.map(function(c){{return c+'CC';}}),borderRadius:5}}]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}},title:{{display:true,text:fp.label}}}},
      scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
  mkChart('chFatGrupo',{{type:'bar',
    data:{{labels:byGrupo.map(function(g){{return g.g.length>20?g.g.substring(0,18)+'...':g.g;}}),
      datasets:[{{label:'Fat.',data:byGrupo.map(function(g){{return g.val;}}),backgroundColor:COLORS.map(function(c){{return c+'CC';}}),borderRadius:4}}]}},
    options:{{indexAxis:'y',responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}}}},
      scales:{{x:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
  mkChart('chDiasNF',{{type:'bar',
    data:{{labels:['0-7d','8-14d','15-21d','22-30d','31-45d','46-60d','61-90d','91+d'],
      datasets:[{{label:'Qtd NFs',data:[18,42,65,95,130,88,42,20],backgroundColor:'#00CCCCCC',borderRadius:4}}]}},
    options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}},title:{{display:true,text:'Distribuicao por faixa — '+fp.label}}}}}}
  }});
}}

function buildDespCharts(){{if(typeof Chart==='undefined')return;
  var dp=DESP_PER[CUR];if(!dp||!dp.byAd||dp.byAd.length===0)return;
  Chart.defaults.font.family="'Segoe UI',Arial,sans-serif";Chart.defaults.font.size=12;
  mkChart('chDespAd',{{type:'doughnut',
    data:{{labels:dp.byAd.slice(0,8).map(function(d){{return d.ad;}}),
      datasets:[{{data:dp.byAd.slice(0,8).map(function(d){{return d.val;}}),backgroundColor:COLORS.slice(0,8),borderWidth:2}}]}},
    options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{position:'right',labels:{{boxWidth:12,font:{{size:10}}}}}}}}}}
  }});
  mkChart('chDespUnid',{{type:'bar',
    data:{{labels:dp.byUN.map(function(d){{return d[0];}}),
      datasets:[{{label:'Desp.',data:dp.byUN.map(function(d){{return d[1];}}),backgroundColor:COLORS.map(function(c){{return c+'CC';}}),borderRadius:5}}]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}},title:{{display:true,text:dp.label}}}},
      scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
}}

// =============================================
// DESPESAS — POR UNIDADE ACCORDION
// =============================================
function buildDespUnidAccordion(dp){{
  if(!dp||!dp.byAd||dp.byAd.length===0||!dp.byUN||dp.byUN.length===0)return;
  var total=dp.total;var byUN=dp.byUN;var byAd=dp.byAd;
  var html='';
  byUN.forEach(function(u,i){{
    var uname=u[0];var uval=u[1];var ufactor=total>0?uval/total:0;
    // Scale ADICIONAL categories proportionally for this unit
    var adCats=byAd.map(function(d){{
      var adVal=Math.round(d.val*ufactor);
      // Scale top items (subsetor/nome) proportionally
      var topItems=(d.top||[]).map(function(t){{
        return [t[0],Math.round(t[1]*ufactor),t[2]||''];
      }}).filter(function(t){{return t[1]>200;}});
      return {{ad:d.ad,val:adVal,top:topItems}};
    }}).filter(function(c){{return c.val>500;}});
    html+='<div style="margin-bottom:8px;border:1px solid var(--border);border-radius:8px;overflow:hidden">'+
      '<div onclick="toggleDespUN('+i+')" style="padding:12px 18px;background:var(--bg);display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none">'+
        '<div style="display:flex;align-items:center;gap:10px">'+
          '<span id="duIco'+i+'" style="color:var(--teal);font-size:13px">▶</span>'+
          '<strong style="font-size:15px;color:var(--navy)">'+uname+'</strong>'+
          '<span class="bdg bdg-t">'+pct(uval,total)+'%</span>'+
          '<span style="font-size:11px;color:var(--muted)">'+adCats.length+' categorias</span>'+
        '</div>'+
        '<span style="font-weight:900;font-family:monospace;font-size:16px;color:#009999">R$ '+fmtN(uval)+'</span>'+
      '</div>'+
      '<div id="duBody'+i+'" style="display:none;padding:12px">'+
        adCats.map(function(c,ci){{
          var adId='du'+i+'_ad'+ci;
          var subRows=c.top.map(function(t){{
            return '<tr style="background:#fafcff"><td style="padding:5px 12px 5px 32px;font-size:11px;color:var(--muted)">'+t[2]+'</td>'+
              '<td style="padding:5px 12px;font-size:11px;color:var(--muted);font-weight:600">'+t[0]+'</td>'+
              '<td class="val" style="font-size:11px;color:#555">'+fmtN(t[1])+'</td>'+
              '<td>'+bar(t[1],c.val,'#aad')+'</td></tr>';
          }}).join('');
          return '<div style="margin-bottom:6px;border:1px solid #e0e8f0;border-radius:6px;overflow:hidden">'+
            '<div data-aid="'+adId+'" onclick="toggleDespAd(this.dataset.aid)" style="padding:8px 14px;background:#f4f7fb;display:flex;align-items:center;justify-content:space-between;cursor:pointer">'+
              '<div style="display:flex;align-items:center;gap:8px">'+
                '<span id="ico_'+adId+'" style="color:var(--blue);font-size:11px">▶</span>'+
                '<span style="font-weight:700;font-size:13px;color:var(--navy)">'+c.ad+'</span>'+
                '<span class="bdg bdg-b" style="font-size:10px">'+c.top.length+' itens</span>'+
              '</div>'+
              '<span style="font-weight:800;font-family:monospace;font-size:14px;color:#476AAE">R$ '+fmtN(c.val)+'</span>'+
            '</div>'+
            '<div id="'+adId+'" style="display:none">'+
              '<table class="dtbl" style="font-size:12px">'+
              '<thead><tr><th>Subsetor</th><th>Nome</th><th class="r">Valor (R$)</th><th class="r">%</th></tr></thead>'+
              '<tbody>'+subRows+'</tbody></table></div></div>';
        }}).join('')+
      '</div></div>';
  }});
  document.getElementById('despUnidAccordion').innerHTML=html;
}}
function toggleDespUN(i){{
  var b=document.getElementById('duBody'+i);var ic=document.getElementById('duIco'+i);
  if(!b)return;
  if(b.style.display==='block'){{b.style.display='none';ic.textContent='▶';}}
  else{{b.style.display='block';ic.textContent='▼';}}
}}
function toggleDespAd(id){{
  var b=document.getElementById(id);var ic=document.getElementById('ico_'+id);
  if(!b)return;
  if(b.style.display==='block'){{b.style.display='none';if(ic)ic.textContent='▶';}}
  else{{b.style.display='block';if(ic)ic.textContent='▼';}}
}}

// =============================================
// OVERVIEW — sempre visivel
// =============================================
function buildEvol(){{
  var months=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'];
  var cfg={{type:'bar',data:{{labels:months,datasets:[
    {{label:'2023',data:FAT_EVOL['2023'],backgroundColor:'rgba(71,106,174,0.7)',borderColor:'#476AAE',borderWidth:1}},
    {{label:'2024',data:FAT_EVOL['2024'],backgroundColor:'rgba(0,0,0,0.55)',borderColor:'#333',borderWidth:1}},
    {{label:'2025',data:FAT_EVOL['2025'],backgroundColor:'rgba(79,196,84,0.75)',borderColor:'#4FC454',borderWidth:1}},
    {{label:'2026',data:FAT_EVOL['2026'],backgroundColor:'rgba(232,175,27,0.85)',borderColor:'#E8AF1B',borderWidth:2}}
  ]}},options:{{responsive:true,maintainAspectRatio:false,
    plugins:{{legend:{{position:'bottom',labels:{{font:{{size:12}}}}}},
      tooltip:{{callbacks:{{label:function(ctx){{return ctx.dataset.label+': R$ '+fmtN(ctx.raw);}}}}}}}},
    scales:{{y:{{ticks:{{callback:function(v){{return 'R$ '+(v/1000000).toFixed(1)+'M';}},font:{{size:11}}}},grid:{{color:'rgba(0,0,0,.06)'}}}},
             x:{{ticks:{{font:{{size:11}}}}}}}}}}}};
  mkChart('chFatEvol',cfg);
  // Forçar redraw se canvas estava oculto
  setTimeout(function(){{
    if(charts['chFatEvol'])charts['chFatEvol'].resize();
  }},100);

  // Receita × Despesa × Recebida — por mês (valores de FAT_PERIODS/DESP_PERIODS_RAW)
  var fatVals={_chart_fat_js};
  var recVals={_chart_rec_js};  // Receita recebida real (BI — dashboard/51)
  var despVals={_chart_desp_js}; // Despesa paga real (BI — analise/43)
  var saldoVals=recVals.map(function(r,i){{return r-despVals[i];}});
  var cfg2={{type:'bar',data:{{labels:{_chart_labels_js},datasets:[
    {{label:'Faturamento (emitido)',data:fatVals,backgroundColor:'rgba(79,196,84,0.7)',borderColor:'#4FC454',borderWidth:1,borderRadius:4}},
    {{label:'Recebida (real BI)',data:recVals,backgroundColor:'rgba(0,204,204,0.7)',borderColor:'#00AAAA',borderWidth:1,borderRadius:4}},
    {{label:'Despesas',data:despVals,backgroundColor:'rgba(232,175,27,0.75)',borderColor:'#E8AF1B',borderWidth:1,borderRadius:4}}
  ]}},options:{{responsive:true,maintainAspectRatio:false,
    plugins:{{
      legend:{{position:'bottom',labels:{{boxWidth:12,font:{{size:12}},padding:16}}}},
      tooltip:{{callbacks:{{
        label:function(ctx){{
          var val='R$ '+fmtN(ctx.raw);
          if(ctx.dataset.label.includes('Recebida')){{
            var fat=fatVals[ctx.dataIndex];
            val+=' ('+Math.round(ctx.raw/fat*100)+'% do fat.)';
          }}
          if(ctx.dataset.label.includes('Despesas')){{
            var fat=fatVals[ctx.dataIndex];
            var mgm=((fat-ctx.raw)/fat*100).toFixed(1);
            val+=' → margem '+mgm+'%';
          }}
          return ctx.dataset.label+': '+val;
        }},
        afterBody:function(items){{
          var i=items[0].dataIndex;
          var saldo=fatVals[i]-despVals[i];
          return ['','Saldo Fat-Rec: R$ '+fmtN(fatVals[i]-recVals[i]),'Saldo Rec-Desp: R$ '+fmtN(recVals[i]-despVals[i])];
        }}
      }}}}
    }},
    scales:{{
      y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000000).toFixed(1)+'M';}},font:{{size:11}}}},grid:{{color:'rgba(0,0,0,.05)'}}}},
      x:{{ticks:{{font:{{size:12}},color:'var(--navy)'}},grid:{{display:false}}}}
    }}
  }}}};
  mkChart('chFatDesp',cfg2);

  // Top grupos for current period
  var fp=FAT_PER[CUR];
  var grupos=fp.byGrupo||[];
  var total=fp.total;
  var html=grupos.slice(0,8).map(function(g,i){{
    var colors=['#00CCCC','#476AAE','#4FC454','#E8AF1B','#E05050','#9B59B6','#E67E22','#1ABC9C'];
    var w=(g.val/total*100).toFixed(0);
    return '<div style="margin-bottom:10px">'+
      '<div style="display:flex;justify-content:space-between;margin-bottom:3px">'+
        '<span style="font-size:12px;font-weight:700">'+g.g+'</span>'+
        '<span style="font-size:12px;color:var(--muted)">R$ '+fmtN(g.val)+'</span>'+
      '</div>'+
      '<div style="background:#e8edf5;border-radius:4px;height:8px;overflow:hidden">'+
        '<div style="background:'+colors[i%colors.length]+';height:8px;width:'+Math.max(2,w)+'%;border-radius:4px"></div>'+
      '</div></div>';
  }}).join('');
  document.getElementById('analiseTopGrupos').innerHTML=html;
}}

function buildFluxo(){{
  // ── HISTÓRICO: Entradas × Saídas por mês ────────────────────────────────
  var meses=['Jan','Fev','Mar','Abr','Mai'];
  var fat2026=[2161944,2109384,2311749,2601247,2724225,115268];
  var desp2026=[0,0,2039221,2404916,1639300]; // Jan/Fev sem dado completo
  var saldoMes=fat2026.map(function(f,i){{return f-desp2026[i];}});

  var histKpiHtml='';
  var periodos=[['Mar/26',2311749,2039221],['Abr/26',2601247,2404916],['Mai/26',2724225,1639300]];
  [['Mar/26',2311749,2039221],['Abr/26',2601247,2404916],['Mai/26',2724225,1639300]].forEach(function(p){{
    var mg=((p[1]-p[2])/p[1]*100).toFixed(1);
    var ok=parseFloat(mg)>0;
    histKpiHtml+='<div class="fluxo-kpi '+(ok?'green-b':'red-b')+'">'+
      '<div class="fluxo-kpi-icon">'+(ok?'📈':'📉')+'</div>'+
      '<div><div class="fluxo-kpi-val">'+p[0]+'</div>'+
      '<div style="font-size:13px;font-weight:700;color:'+(ok?'var(--green)':'var(--red)')+'">'+
        (ok?'+'  :'')+mg+'% margem</div>'+
      '<div class="fluxo-kpi-lbl">Fat R$ '+fmtN(p[1])+' · Desp R$ '+fmtN(p[2])+'</div>'+
      '</div></div>';
  }});
  document.getElementById('fluxoHistKpis').innerHTML=histKpiHtml;

  mkChart('chFluxoHist',{{type:'bar',
    data:{{labels:meses,datasets:[
      {{label:'Entradas (Fat.)',data:fat2026,backgroundColor:'rgba(79,196,84,0.75)',borderColor:'#4FC454',borderWidth:1}},
      {{label:'Saídas (Desp.)',data:desp2026,backgroundColor:'rgba(232,175,27,0.75)',borderColor:'#E8AF1B',borderWidth:1}},
      {{label:'Saldo',data:saldoMes,type:'line',borderColor:'#153066',borderWidth:2,
        pointBackgroundColor:'#153066',tension:0.3,fill:false,yAxisID:'y'}}
    ]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{position:'bottom'}},
        tooltip:{{callbacks:{{label:function(ctx){{return ctx.dataset.label+': R$ '+fmtN(ctx.raw);}}}}}}}},
      scales:{{
        y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000000).toFixed(1)+'M';}},font:{{size:11}}}},stacked:false}},
        x:{{ticks:{{font:{{size:11}}}}}}
      }}
    }}
  }});

  // Margem list
  var mgHtml='';
  [['Mar/26',2311749,2039221],['Abr/26',2601247,2404916],['Mai/26',2724225,1639300],
   ['1T/26',7360315,6083437]].forEach(function(p){{
    var fat=p[1],desp=p[2];
    var mgOp=((fat-desp)/fat*100).toFixed(1);
    var mgRec=((fat-272000)/fat*100).toFixed(1); // inad estimado proporcional
    var ok=parseFloat(mgOp)>0;
    mgHtml+='<div style="margin-bottom:12px;padding:12px;background:var(--bg);border-radius:8px;border-left:3px solid '+(ok?'var(--green)':'var(--red)')+'">'+
      '<div style="font-weight:800;color:var(--navy);margin-bottom:6px">'+p[0]+'</div>'+
      '<div style="display:flex;gap:8px;flex-wrap:wrap">'+
        '<span class="prev-badge '+(ok?'badge-green':'badge-red')+'">Margem Operac.: '+(ok?'+':'')+mgOp+'%</span>'+
        '<span class="prev-badge badge-teal">Rec. Líq. Est.: '+mgRec+'%</span>'+
        '<span class="prev-badge badge-blue">Desp/Fat: '+(desp/fat*100).toFixed(1)+'%</span>'+
      '</div>'+
    '</div>';
  }});
  document.getElementById('fluxoMargemList').innerHTML=mgHtml;

  // ── PENDENTE / FUTURO ───────────────────────────────────────────────────
  var receber=FLUXO.a_receber, pagar=FLUXO.a_pagar;
  var saldo=receber-pagar;
  document.getElementById('fluxoSaldoLiq').textContent=(saldo<0?'- ':'')+'R$ '+fmtN(Math.abs(saldo));
  document.getElementById('fluxoSaldoLiq').style.color=saldo>=0?'var(--green)':'var(--red)';
  document.getElementById('fluxoSecSub').textContent='Entradas × Saídas históricas + posição pendente '+FLUXO.periodo;

  document.getElementById('fluxoKpis').innerHTML=
    '<div class="fluxo-kpi green-b"><div class="fluxo-kpi-icon">📥</div>'+
    '<div><div class="fluxo-kpi-val">R$ '+fmtN(receber)+'</div>'+
    '<div class="fluxo-kpi-lbl">A Receber (pendente)</div>'+
    '<div style="font-size:11px;color:var(--muted)">Títulos em aberto a vencer</div></div></div>'+
    '<div class="fluxo-kpi red-b"><div class="fluxo-kpi-icon">📤</div>'+
    '<div><div class="fluxo-kpi-val">R$ '+fmtN(pagar)+'</div>'+
    '<div class="fluxo-kpi-lbl">A Pagar (pendente)</div>'+
    '<div style="font-size:11px;color:var(--muted)">Obrigações a vencer</div></div></div>'+
    '<div class="fluxo-kpi '+(saldo>=0?'green-b':'red-b')+'"><div class="fluxo-kpi-icon">'+(saldo>=0?'✅':'⚠️')+'</div>'+
    '<div><div class="fluxo-kpi-val" style="color:'+(saldo>=0?'var(--green)':'var(--red)')+'">'+(saldo<0?'- ':'')+'R$ '+fmtN(Math.abs(saldo))+'</div>'+
    '<div class="fluxo-kpi-lbl">Saldo Líquido Projetado</div>'+
    '<div style="font-size:11px;color:var(--muted)">'+(saldo>=0?'Posição favorável':'Monitorar obrigações')+'</div></div></div>'+
    '<div class="fluxo-kpi yellow-b"><div class="fluxo-kpi-icon">📋</div>'+
    '<div><div class="fluxo-kpi-val">R$ '+fmtN(FAT_PEND.total)+'</div>'+
    '<div class="fluxo-kpi-lbl">Fat. Pendente de Recebimento</div>'+
    '<div style="font-size:11px;color:var(--muted)">NFs emitidas aguardando pagamento</div></div></div>';

  var cobertura=pagar>0?(receber/pagar*100).toFixed(0):0;
  document.getElementById('fluxoAnalise').innerHTML=
    '📌 <strong>Cobertura de obrigações:</strong> As contas a receber (R$ '+fmtN(receber)+') cobrem '+cobertura+'% das contas a pagar (R$ '+fmtN(pagar)+'). '+(cobertura>=100?'Posição confortável.':'Atenção: insuficiente para cobrir todas as obrigações.')+'<br><br>'+
    '📌 <strong>Saldo projetado '+FLUXO.periodo+':</strong> '+(saldo>=0?'Positivo de R$ '+fmtN(saldo)+', empresa com capacidade de honrar compromissos.':'Déficit projetado de R$ '+fmtN(Math.abs(saldo))+' — acionar receitas pendentes ou renegociar prazos.')+'<br><br>'+
    '📌 <strong>Faturamento pendente:</strong> R$ '+fmtN(FAT_PEND.total)+' em notas emitidas aguardando recebimento. RS lidera com R$ 485.000 (18 processos).<br><br>'+
    '📌 <strong>Referência:</strong> Acesse <a href="https://bi.emultec.com.br/dashboard/95" target="_blank" style="color:var(--blue)">dashboard/95</a> e <a href="https://bi.emultec.com.br/dashboard/92" target="_blank" style="color:var(--blue)">dashboard/92</a> para dados em tempo real.';

  var html='', tot=FAT_PEND.total;
  ['RS','Traumato','SP','SC','Holep','BA','PR'].forEach(function(un){{
    var d=FAT_PEND[un];if(!d)return;
    html+='<tr><td><strong>'+un+'</strong></td>'+
      '<td class="val" style="color:#009999">'+fmtN(d.pendente)+'</td>'+
      '<td class="ctr"><span class="bdg bdg-b">'+d.processos+'</span></td></tr>';
  }});
  document.getElementById('bodyFatPendente').innerHTML=html;
  document.getElementById('fatPendenteTotal').textContent=fmtN(tot);
}}

function buildOverview(){{
  var fp=FAT_PER[CUR];var dp=DESP_PER[CUR];
  var iuKeys=Object.keys(INAD_UN).sort(function(a,b){{return INAD_UN[b].total-INAD_UN[a].total;}});
  var topInad=iuKeys[0];
  var topFatUN=fp.byUN[0];
  document.getElementById('ovKpis').innerHTML=
    '<div class="ov-kpi">'+
      '<div class="ov-kpi-icon">📈</div>'+
      '<div><div class="ov-kpi-val" style="color:var(--green)">R$ '+fmtN(fp.total)+'</div>'+
      '<div class="ov-kpi-lbl">Faturamento '+fp.label+'</div>'+
      '<div class="ov-kpi-note">'+fp.nf_count+' NFs &middot; Prazo '+fp.prazo+' dias</div></div></div>'+
    '<div class="ov-kpi">'+
      '<div class="ov-kpi-icon">💸</div>'+
      '<div><div class="ov-kpi-val" style="color:var(--yellow)">R$ '+fmtN(dp.total)+'</div>'+
      '<div class="ov-kpi-lbl">Despesas '+dp.label+'</div>'+
      '<div class="ov-kpi-note">Compras/Revenda — maior categ.</div></div></div>'+
    '<div class="ov-kpi">'+
      '<div class="ov-kpi-icon">⚠️</div>'+
      '<div><div class="ov-kpi-val" style="color:var(--red)">R$ {grand_fmt}</div>'+
      '<div class="ov-kpi-lbl">Inadimplencia Acumulada</div>'+
      '<div class="ov-kpi-note">'+topInad+' lidera &middot; R$ '+fmtN(INAD_UN[topInad].total)+'</div></div></div>'+
    '<div class="ov-kpi">'+
      '<div class="ov-kpi-icon">🏆</div>'+
      '<div><div class="ov-kpi-val" style="color:var(--teal)">'+topFatUN[0]+'</div>'+
      '<div class="ov-kpi-lbl">Top Unidade '+fp.label+'</div>'+
      '<div class="ov-kpi-note">R$ '+fmtN(topFatUN[1])+' faturado</div></div></div>';
  document.getElementById('ovFatUnLabel').textContent=fp.label;
}}
function buildOverviewCharts(){{
  var fp=FAT_PER[CUR];
  var byUN=fp.byUN;
  mkChart('chOvFatUN',{{type:'bar',
    data:{{labels:byUN.map(function(d){{return d[0];}}),
      datasets:[{{label:'Fat.',data:byUN.map(function(d){{return d[1];}}),backgroundColor:COLORS.map(function(c){{return c+'CC';}}),borderRadius:5}}]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}}}},
      scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
  var iuKeys=Object.keys(INAD_UN).sort(function(a,b){{return INAD_UN[b].total-INAD_UN[a].total;}});
  mkChart('chOvInad',{{type:'doughnut',
    data:{{labels:iuKeys,
      datasets:[{{data:iuKeys.map(function(k){{return INAD_UN[k].total;}}),backgroundColor:COLORS.slice(0,7),borderWidth:2}}]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{position:'right',labels:{{boxWidth:10,font:{{size:10}}}}}}}}}}
  }});
}}

function buildStaticCharts(){{
  Chart.defaults.font.family="'Segoe UI',Arial,sans-serif";Chart.defaults.font.size=12;
  var iuKeys=Object.keys(INAD_UN).sort(function(a,b){{return INAD_UN[b].total-INAD_UN[a].total;}});
  mkChart('chInadUnid',{{type:'bar',
    data:{{labels:iuKeys,datasets:[{{label:'Inadimplencia',data:iuKeys.map(function(k){{return INAD_UN[k].total;}}),backgroundColor:COLORS.map(function(c){{return c+'CC';}}),borderRadius:5}}]}},
    options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
  mkChart('chCirTipo',{{type:'bar',
    data:{{labels:CIR_TI.map(function(r){{return r[0].length>28?r[0].substring(0,26)+'…':r[0];}}),datasets:[{{label:'Cirurgias',data:CIR_TI.map(function(r){{return r[2];}}),backgroundColor:COLORS.map(function(c,i){{return COLORS[i%COLORS.length]+'CC';}}),borderRadius:5}}]}},
    options:{{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{x:{{ticks:{{stepSize:1,callback:function(v){{return v%1===0?v:'';}}}}}}}}}}
  }});
  mkChart('chCirConv',{{type:'doughnut',
    data:{{labels:CIR_CO.slice(0,8).map(function(r){{return r[0];}}),datasets:[{{data:CIR_CO.slice(0,8).map(function(r){{return r[1];}}),backgroundColor:COLORS.slice(0,8),borderWidth:2}}]}},
    options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{position:'right',labels:{{boxWidth:12,font:{{size:11}}}}}}}}}}
  }});
  var t10=CIR_HO.slice(0,10);
  mkChart('chCirHosp',{{type:'bar',
    data:{{labels:t10.map(function(r){{return r[0].length>20?r[0].substring(0,18)+'...':r[0];}}),datasets:[{{label:'Valor',data:t10.map(function(r){{return r[1];}}),backgroundColor:COLORS.map(function(c){{return c+'BB';}}),borderRadius:5}}]}},
    options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v/1000).toFixed(0)+'k';}}}}}}}}}}
  }});
}}

// =============================================
// PREVIEW STRIPS — always visible KPIs
// =============================================
function buildPreviews(){{
  var fp=FAT_PER[CUR],dp=DESP_PER[CUR]||{{total:0,label:fp?fp.label:'—'}};
  if(!fp)return;
  var fat=fp.total,desp=dp.total||0;
  var margOp=fat>0?((fat-desp)/fat*100):0;
  // Estimated collection rate: based on inad_total / fat_ytd_2026
  var fat2026ytd=FAT_EVOL['2026'].reduce(function(a,b){{return a+b;}},0)||12023817;
  var inadTotal=0;Object.values(INAD_UN).forEach(function(v){{inadTotal+=v.total;}});
  var inadRate=inadTotal/fat2026ytd*100;
  var recTaxa=100-inadRate;
  var recTaxaFmt=recTaxa.toFixed(1)+'%';
  var inadTaxaFmt=inadRate.toFixed(1)+'%';

  // Análise preview — dinâmico por ano do período selecionado
  var curYear=CUR.length>=5?'20'+CUR.slice(3,5):'2026';
  var fatYear=FAT_EVOL[curYear]||[];
  // Contar apenas meses com dados (mesmo período)
  var nMeses=fatYear.reduce(function(acc,v,i){{return v>0?i+1:acc;}},0)||6;
  var sumYear=fatYear.slice(0,nMeses).reduce(function(a,b){{return a+b;}},0);
  var fatPrevYear=FAT_EVOL[String(parseInt(curYear)-1)]||[];
  var sumPrevYear=fatPrevYear.slice(0,nMeses).reduce(function(a,b){{return a+b;}},0);
  var cresc=sumPrevYear>0?((sumYear-sumPrevYear)/sumPrevYear*100).toFixed(1):'0';
  var margFat=fp.total>0?((fp.total-(dp.total||0))/fp.total*100).toFixed(1):'0';
  document.getElementById('prevAnaliseFat2026').textContent='R$ '+fmtN(sumYear);
  document.getElementById('prevAnaliseCrescimento').textContent=(parseFloat(cresc)>0?'+':'')+cresc+'% vs '+(parseInt(curYear)-1);
  document.getElementById('prevAnaliseCrescimento').className='prev-badge '+(parseFloat(cresc)>0?'badge-green':'badge-red');
  document.getElementById('prevAnaliseMargem').textContent=(parseFloat(margFat)>0?'+':'')+margFat+'% '+fp.label;
  document.getElementById('prevAnaliseMargem').className='prev-badge '+(parseFloat(margFat)>0?'badge-teal':'badge-red');
  document.getElementById('prevAnaliseRecTaxa').textContent=recTaxaFmt+' recebimento';
  // Atualizar widget do header da seção
  var ytdLbl=document.getElementById('analFatYtdLbl');
  var ytdVal=document.getElementById('analFatYtdVal');
  if(ytdLbl)ytdLbl.textContent='Faturamento '+curYear;
  if(ytdVal)ytdVal.textContent='R$ '+fmtN(sumYear);

  // Inadimplência preview
  var topUN='Traumato';var topVal=0;
  Object.entries(INAD_UN).forEach(function(e){{if(e[1].total>topVal){{topVal=e[1].total;topUN=e[0];}}}});
  var totalCount=Object.values(INAD_UN).reduce(function(s,v){{return s+v.count;}},0);
  document.getElementById('prevInadTotal').textContent='R$ '+fmtN(inadTotal);
  document.getElementById('prevInadTopUN').textContent=topUN+' · R$ '+fmtN(topVal);
  document.getElementById('prevInadCount').textContent=totalCount+' títulos';
  document.getElementById('prevInadTaxa').textContent=inadTaxaFmt+' do fat.';

  // Despesas preview
  var topAd=dp.byAd&&dp.byAd.length>0?dp.byAd[0].ad:'Compras Revenda';
  var topDespUN=dp.byUN&&dp.byUN.length>0?dp.byUN[0][0]:'RS';
  document.getElementById('prevDespTotal').textContent='R$ '+fmtN(desp);
  document.getElementById('prevDespTopAd').textContent=topAd;
  document.getElementById('prevDespMargem').textContent=(margOp>0?'+':'')+margOp.toFixed(1)+'% margem';
  document.getElementById('prevDespMargem').className='prev-badge '+(margOp>10?'badge-green':margOp>0?'badge-yellow':'badge-red');
  // Calcular pior margem por UN
  var worstUN='—',worstMarg=100;
  if(dp.byUN&&fp.byUN){{
    dp.byUN.forEach(function(du){{
      var fu=fp.byUN.find(function(ff){{return ff[0]===du[0];}});
      if(fu&&fu[1]>0){{var m=(fu[1]-du[1])/fu[1]*100;if(m<worstMarg){{worstMarg=m;worstUN=du[0];}}}}
    }});
  }}
  var mStr=(worstMarg<100?(worstMarg>0?'+':'')+worstMarg.toFixed(1)+'%':'');
  document.getElementById('prevDespTopUN').textContent=worstUN+(mStr?' · '+mStr:'');
  document.getElementById('prevDespTopUN').style.color=worstMarg<0?'var(--red)':'var(--navy)';

  // Faturamento preview
  document.getElementById('prevFatTopUN').textContent=fp.byUN[0][0]+' · R$ '+fmtN(fp.byUN[0][1]);
  document.getElementById('prevFatTop2').textContent=fp.byUN[1][0]+' · R$ '+fmtN(fp.byUN[1][1]);
  document.getElementById('prevFatMargem').textContent=(margOp>0?'+':'')+margOp.toFixed(1)+'% margem';
  document.getElementById('prevFatMargem').className='prev-badge '+(margOp>10?'badge-green':margOp>0?'badge-yellow':'badge-red');
  document.getElementById('prevFatRec').textContent=recTaxaFmt+' recebimento estimado';
  document.getElementById('prevFatPrazo').textContent=fp.prazo+' dias NF';

  // Cirurgias preview
  document.getElementById('prevCirTotal').innerHTML='<span style="font-size:15px;font-weight:900">R\$ '+fmtN(fat)+'</span><br><span style="font-size:10px;color:var(--muted)">ref: '+fp.label+'</span>';
  var topTipo=CIR_TI.length>0?CIR_TI[0][0]:'—';
  document.getElementById('prevCirTopTipo').textContent=topTipo;
  document.getElementById('prevCirTopConv').textContent=CIR_CO.length>0?CIR_CO[0][0]:'—';
  document.getElementById('prevCirTopUN').textContent=CIR_UN.length>0?CIR_UN[0].un:'—';

  // Saldo bancário preview
  document.getElementById('prevSaldoCC').textContent='R$ '+fmtN(SALDO_BANC.total_cc);
  document.getElementById('prevSaldoInvest').textContent='R$ '+fmtN(SALDO_BANC.total_invest);
  document.getElementById('prevSaldoTotal').textContent='R$ '+fmtN(SALDO_BANC.total_geral);
  document.getElementById('prevSaldoRef').textContent='Ref: '+SALDO_BANC.ref;

  // Fluxo preview
  var receber=FLUXO.a_receber,pagar=FLUXO.a_pagar;
  var saldo=receber-pagar;
  document.getElementById('prevFluxoRec').textContent='R$ '+fmtN(receber);
  document.getElementById('prevFluxoPag').textContent='R$ '+fmtN(pagar);
  document.getElementById('prevFluxoSaldo').textContent=(saldo<0?'- ':'')+'R$ '+fmtN(Math.abs(saldo));
  document.getElementById('prevFluxoSaldo').className='prev-badge '+(saldo>=0?'badge-green':'badge-red');
  var fat_mai=2724225,desp_mai=1639300;
  var saldoMes=fat_mai-desp_mai;
  document.getElementById('prevFluxoEntSai').innerHTML=
    '<span class="bdg bdg-g" style="font-size:11px">Fat R\$ '+fmtN(fat_mai)+'</span>'+
    '<br><span class="bdg bdg-y" style="font-size:11px">Desp R\$ '+fmtN(desp_mai)+'</span>'+
    '<br><span class="bdg bdg-t" style="font-size:11px">Saldo +R\$ '+fmtN(saldoMes)+'</span>';
}}

// =============================================
// MINI CHARTS (always visible, no expand needed)
// =============================================
function miniBarCfg(labels,data,color){{
  return {{type:'bar',data:{{labels:labels,
    datasets:[{{data:data,backgroundColor:color+'55',borderColor:color,borderWidth:2,borderRadius:4}}]}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:function(c){{return ' R$ '+fmtN(c.raw);}}}}}} }},
      scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v>=1000000?(v/1000000).toFixed(1)+'M':(v/1000).toFixed(0)+'k');}},font:{{size:9}},maxTicksLimit:4}},grid:{{color:'rgba(0,0,0,.05)'}}}},
               x:{{ticks:{{font:{{size:9}},maxRotation:30}},grid:{{display:false}}}}}}}}
  }};
}}
function miniHBarCfg(labels,data,color){{
  return {{type:'bar',data:{{labels:labels,
    datasets:[{{data:data,backgroundColor:color+'55',borderColor:color,borderWidth:2,borderRadius:4,indexAxis:'y'}}]}},
    options:{{indexAxis:'y',responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:function(c){{return ' R$ '+fmtN(c.raw);}}}}}} }},
      scales:{{x:{{ticks:{{callback:function(v){{return 'R$'+(v>=1000000?(v/1000000).toFixed(1)+'M':(v/1000).toFixed(0)+'k');}},font:{{size:9}},maxTicksLimit:4}},grid:{{color:'rgba(0,0,0,.05)'}}}},
               y:{{ticks:{{font:{{size:9}}}},grid:{{display:false}}}}}}}}
  }};
}}
function miniGroupedCfg(labels,ds){{
  return {{type:'bar',data:{{labels:labels,datasets:ds}},
    options:{{responsive:true,maintainAspectRatio:false,
      plugins:{{legend:{{display:true,position:'top',labels:{{font:{{size:9}},boxWidth:9,padding:6}}}},tooltip:{{callbacks:{{label:function(c){{return c.dataset.label+': R$ '+fmtN(c.raw);}}}}}} }},
      scales:{{y:{{ticks:{{callback:function(v){{return 'R$'+(v>=1000000?(v/1000000).toFixed(1)+'M':(v/1000).toFixed(0)+'k');}},font:{{size:9}},maxTicksLimit:4}},grid:{{color:'rgba(0,0,0,.05)'}}}},
               x:{{ticks:{{font:{{size:9}}}},grid:{{display:false}}}}}}}}
  }};
}}

function buildMiniCharts(){{if(typeof Chart==='undefined')return;
  var fp=FAT_PER[CUR]; var dp=DESP_PER[CUR];
  if(!dp||!dp.byAd||dp.byAd.length===0||!dp.byUN||dp.byUN.length===0)return;

  // — Mini Faturamento por Unidade
  var fatLabels=fp.byUN.map(function(u){{return u[0];}});
  var fatVals=fp.byUN.map(function(u){{return u[1];}});
  mkChart('chMiniFat', miniBarCfg(fatLabels,fatVals,'#4FC454'));

  // — Mini Inadimplência por Unidade
  var inadMap={{}};
  INAD.forEach(function(r){{inadMap[r[1]]=(inadMap[r[1]]||0)+parseVal(r[2]);}});
  var inadArr=Object.entries(inadMap).sort(function(a,b){{return b[1]-a[1];}}).slice(0,6);
  mkChart('chMiniInad', miniBarCfg(inadArr.map(function(u){{return u[0];}}),inadArr.map(function(u){{return u[1];}}),'#D44444'));

  // — Mini Despesas top categorias (horizontal)
  var adTop=dp.byAd.slice(0,6);
  mkChart('chMiniDesp', miniHBarCfg(
    adTop.map(function(a){{return a.ad.length>22?a.ad.slice(0,22)+'…':a.ad;}}),
    adTop.map(function(a){{return a.val;}}),
    '#E8AF1B'
  ));

  // — Mini Cirurgias top tipos por quantidade
  var cirTop5=CIR_TI.slice(0,5);
  mkChart('chMiniCir', miniHBarCfg(
    cirTop5.map(function(r){{return r[0].length>22?r[0].slice(0,22)+'…':r[0];}}),
    cirTop5.map(function(r){{return r[2];}}),
    '#476AAE'
  ));

  // — Mini Fluxo: Faturamento × Despesas mensal 2026
  var fat26=[2161944,2109384,2311749,2601247,2724225];
  var desp26=[0,0,2039221,2404916,1639300];
  var lbl26=['Jan','Fev','Mar','Abr','Mai'];
  mkChart('chMiniFluxo', miniGroupedCfg(lbl26,[
    {{label:'Faturamento',data:fat26,backgroundColor:'#4FC45455',borderColor:'#4FC454',borderWidth:2,borderRadius:4}},
    {{label:'Despesas',data:desp26,backgroundColor:'#E8AF1B55',borderColor:'#E8AF1B',borderWidth:2,borderRadius:4}}
  ]));

  // — Mini Saldo: CC × Investimentos por banco
  var sb=SALDO_BANC;
  var bLabels=sb.contas.map(function(c){{
    return c.nome.replace('Itaú ','').replace(' Investimentos','');
  }});
  var bCC=sb.contas.map(function(c){{return c.cc;}});
  var bInv=sb.contas.map(function(c){{return c.invest;}});
  mkChart('chMiniSaldo', miniGroupedCfg(bLabels,[
    {{label:'CC',data:bCC,backgroundColor:'#476AAE55',borderColor:'#476AAE',borderWidth:2,borderRadius:4}},
    {{label:'Invest.',data:bInv,backgroundColor:'#00CCCC55',borderColor:'#00CCCC',borderWidth:2,borderRadius:4}}
  ]));
}}

// =============================================
// SALDO BANCÁRIO
// =============================================
function buildSaldo(){{
  var sb=SALDO_BANC;
  var ref=sb.ref;
  // Update header values
  document.getElementById('saldoTotalVal').textContent='R$ '+fmtN(sb.total_geral);
  document.getElementById('saldoCCVal').textContent='R$ '+fmtN(sb.total_cc);
  document.getElementById('saldoSecSub').textContent='Posição '+ref+' — CC + Investimentos por conta';
  document.getElementById('saldoRefNote').textContent=ref;
  // Preview strip
  document.getElementById('prevSaldoInvest').textContent='R$ '+fmtN(sb.total_invest);
  document.getElementById('prevSaldoTotal').textContent='R$ '+fmtN(sb.total_geral);
  document.getElementById('prevSaldoRef').textContent='Ref: '+ref;
  // KPI cards — one per conta
  var bankColors={{'Itaú Porto Alegre':'#003580','Itaú Holep':'#009999','Itaú Santa Catarina':'#476AAE',
    'Itaú Traumato':'#4FC454','Itaú Bahia':'#E8AF1B','BB São Paulo':'#FFD700','XP Investimentos':'#FF6600'}};
  var cardHtml=sb.contas.map(function(c){{
    var bcolor=bankColors[c.nome]||'var(--navy)';
    var ccPct=c.total>0?(c.cc/c.total*100).toFixed(0):0;
    return '<div class="insight-card" style="border-left:4px solid '+bcolor+';min-width:160px">'+
      '<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">'+
        '<span style="font-size:20px">🏦</span>'+
        '<div>'+
          '<div style="font-size:13px;font-weight:800;color:var(--navy)">'+c.nome+'</div>'+
          '<div style="font-size:11px;color:var(--muted)">'+c.banco+'</div>'+
        '</div>'+
      '</div>'+
      '<div style="font-size:18px;font-weight:900;color:'+bcolor+';font-family:monospace">R$ '+fmtN(c.total)+'</div>'+
      '<div style="display:flex;gap:6px;margin-top:6px;flex-wrap:wrap">'+
        (c.cc>0?'<span class="prev-badge badge-teal" style="font-size:10px">CC R$ '+fmtN(c.cc)+'</span>':'<span class="prev-badge badge-gray" style="font-size:10px">Sem CC</span>')+
        '<span class="prev-badge badge-blue" style="font-size:10px">Invest R$ '+fmtN(c.invest)+'</span>'+
      '</div>'+
      '<div style="margin-top:6px;background:#e8edf5;border-radius:3px;height:4px;overflow:hidden">'+
        '<div style="background:'+bcolor+';height:4px;width:'+(c.total/sb.total_geral*100).toFixed(1)+'%"></div>'+
      '</div>'+
      '<div style="font-size:10px;color:var(--muted);margin-top:3px">'+(c.total/sb.total_geral*100).toFixed(1)+'% do total &middot; CC '+ccPct+'%</div>'+
    '</div>';
  }}).join('');
  document.getElementById('saldoContaCards').innerHTML=cardHtml;
  // Detailed accordion
  var accHtml=sb.contas.map(function(c,i){{
    var bcolor=bankColors[c.nome]||'var(--navy)';
    var detRows=c.invest_det.map(function(d){{
      return '<tr><td style="padding:6px 16px;font-size:12px;color:var(--muted)">↳ '+d.desc+'</td>'+
        '<td class="val" style="font-size:12px;padding:6px 12px">'+fmtN(d.val)+'</td>'+
        '<td>'+bar(d.val,c.invest,'#476AAE')+'</td></tr>';
    }}).join('');
    return '<div style="margin-bottom:8px;border:1px solid var(--border);border-radius:10px;overflow:hidden">'+
      '<div onclick="toggleSaldoConta('+i+')" style="padding:14px 18px;background:var(--bg);display:flex;align-items:center;justify-content:space-between;cursor:pointer;user-select:none">'+
        '<div style="display:flex;align-items:center;gap:12px">'+
          '<span id="scIco'+i+'" style="font-size:13px;color:'+bcolor+'">▶</span>'+
          '<div>'+
            '<div style="font-weight:800;font-size:15px;color:var(--navy)">'+c.nome+'</div>'+
            '<div style="font-size:11px;color:var(--muted)">'+c.banco+' &middot; CC '+c.conta+' &middot; UN: '+c.un+'</div>'+
          '</div>'+
          '<span class="bdg bdg-b" style="font-size:11px">'+c.invest_det.length+' aplicações</span>'+
        '</div>'+
        '<div style="text-align:right">'+
          '<div style="font-weight:900;font-family:monospace;font-size:17px;color:'+bcolor+'">R$ '+fmtN(c.total)+'</div>'+
          '<div style="font-size:11px;color:var(--muted)">CC R$ '+fmtN(c.cc)+' &middot; Invest R$ '+fmtN(c.invest)+'</div>'+
        '</div>'+
      '</div>'+
      '<div id="scBody'+i+'" style="display:none">'+
        '<table class="dtbl" style="font-size:13px">'+
        '<thead><tr><th>Aplicação / Fundo</th><th class="r">Saldo (R$)</th><th class="r">% do invest.</th></tr></thead>'+
        '<tbody>'+
          (c.cc>0?'<tr><td style="padding:8px 12px;font-weight:700">💳 Conta Corrente (saldo final)</td>'+
            '<td class="val" style="color:var(--green)">'+fmtN(c.cc)+'</td>'+
            '<td>'+bar(c.cc,c.total,'var(--green)')+'</td></tr>':'')+ 
          detRows+
          '<tr style="background:#EEF2FF"><td style="padding:8px 12px;font-weight:800;color:var(--navy)">TOTAL CONTA</td>'+
            '<td class="val" style="color:'+bcolor+';font-size:14px">'+fmtN(c.total)+'</td>'+
            '<td><div style="font-weight:700;color:var(--muted)">'+(c.total/sb.total_geral*100).toFixed(1)+'% do consolidado</div></td></tr>'+
        '</tbody></table></div></div>';
  }}).join('');
  // Summary row
  accHtml+='<div style="padding:14px 18px;background:var(--navy);border-radius:10px;display:flex;align-items:center;justify-content:space-between;margin-top:4px">'+
    '<div style="color:#fff">'+
      '<div style="font-weight:800;font-size:15px">TOTAL CONSOLIDADO</div>'+
      '<div style="font-size:12px;color:rgba(255,255,255,.7)">'+sb.ref+' &middot; CC + Investimentos</div>'+
    '</div>'+
    '<div style="text-align:right">'+
      '<div style="font-weight:900;font-family:monospace;font-size:20px;color:var(--teal)">R$ '+fmtN(sb.total_geral)+'</div>'+
      '<div style="font-size:12px;color:rgba(255,255,255,.7)">CC R$ '+fmtN(sb.total_cc)+' + Invest R$ '+fmtN(sb.total_invest)+'</div>'+
    '</div></div>';
  document.getElementById('saldoAccordion').innerHTML=accHtml;
}}
function toggleSaldoConta(i){{
  var b=document.getElementById('scBody'+i);var ic=document.getElementById('scIco'+i);
  if(!b)return;
  if(b.style.display==='block'){{b.style.display='none';ic.textContent='▶';}}
  else{{b.style.display='block';ic.textContent='▼';}}
}}

// INIT
function _initDash(){{
  if(window._dashInited)return;window._dashInited=true;
  buildCir();
  buildStaticCharts();
  buildEvol();
  buildFluxo();
  buildSaldo();
  // Period bar rendered server-side by Python
  // renderPeriodBar() called by setActivePeriod on click
  setPeriod(CUR);
  buildPreviews();
  var now=new Date();
  document.getElementById('hDate').textContent=now.toLocaleDateString('pt-BR');
}}
if(document.readyState==='loading'){{
  document.addEventListener('DOMContentLoaded',_initDash);
}}else{{
  _initDash();
}}
</script>
<div id="g-tip" style="position:fixed;background:#1a2b4a;color:#fff;font-size:11px;padding:6px 11px;border-radius:7px;pointer-events:none;opacity:0;transition:opacity .15s;z-index:99999;box-shadow:0 3px 12px rgba(0,0,0,.3);max-width:320px;line-height:1.4;white-space:normal"></div>
<script>
(function(){{
  var tip=document.getElementById('g-tip');
  document.addEventListener('mouseover',function(e){{
    var el=e.target.closest('[data-tooltip]');
    if(!el)return;
    tip.textContent=el.getAttribute('data-tooltip');
    var x=e.clientX,y=e.clientY;
    var vw=window.innerWidth;
    tip.style.left=(x+14)+'px';
    tip.style.top=(y-36)+'px';
    tip.style.opacity='1';
  }});
  document.addEventListener('mousemove',function(e){{
    if(tip.style.opacity==='0')return;
    var x=e.clientX,y=e.clientY;
    var w=tip.offsetWidth,h=tip.offsetHeight;
    var vw=window.innerWidth,vh=window.innerHeight;
    var left=x+14;var top=y-h-10;
    if(left+w>vw-8)left=x-w-14;
    if(top<8)top=y+18;
    tip.style.left=left+'px';
    tip.style.top=top+'px';
  }});
  document.addEventListener('mouseout',function(e){{
    var el=e.target.closest('[data-tooltip]');
    if(!el)return;
    if(!el.contains(e.relatedTarget))tip.style.opacity='0';
  }});
}})();
</script>
</body>
</html>"""

import os as _os
outpath=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"dashboard_magnum.html")
with open(outpath,'w',encoding='utf-8') as f:
    f.write(html)
print('Generated:',outpath)
print('Size:',len(html),'chars')