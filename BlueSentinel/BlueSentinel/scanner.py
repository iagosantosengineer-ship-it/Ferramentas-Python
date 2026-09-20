import ipaddress

from detectors.allowlist import PROCESSOS_CONFIAVEIS, IPS_CONFIAVEIS, LOLBINS, PROCESSOS_SISTEMA
from detectors.conexoes import verificar_conexoes
from utils.config_loader import carregar_config
from detectors.powershell import verificar_processos_suspeitos
from detectors.persistencia import verificar_persistencia
from detectors.threatintel import verificar_threat_intel
from utils.logger import registrar_evento


# -------------------------
# CARREGAMENTO DE CONFIGURAÇÃO
# -------------------------

config = carregar_config()

IPS_CONFIAVEIS_CONFIG = config.get("ips_confiaveis", [])
PROCESSOS_CONFIAVEIS_CONFIG = config.get("processos_confiaveis", [])
PROCESSOS_SISTEMA_CONFIG = config.get("processos_sistema", [])
BEACON_THRESHOLD = config.get("beaconing_threshold", 3)


# -------------------------
# FUNÇÕES AUXILIARES
# -------------------------

def ip_confiavel(ip):
    """
    Verifica se o IP pertence à allowlist definida no config.json.
    """

    for prefixo in IPS_CONFIAVEIS_CONFIG:
        if ip.startswith(prefixo):
            return True

    return False


def ip_externo(ip):
    """
    Verifica se o IP é externo (não privado).
    """

    try:
        endereco = ipaddress.ip_address(ip)
        return not endereco.is_private
    except ValueError:
        return False


# -------------------------
# SCAN PRINCIPAL
# -------------------------

def scan_completo():
    """
    Executa todas as rotinas de detecção do BlueSentinel.

    Fluxo de análise:

    1. Coleta conexões de rede ativas
    2. Detecta processos suspeitos
    3. Detecta uso de LOLBins
    4. Verifica persistência no sistema
    5. Detecta possíveis conexões C2
    6. Aplica regras de Threat Intelligence
    """

    resultado = []

    # coleta conexões de rede do sistema
    conexoes = verificar_conexoes()

    contagem_conexoes = {}

    # -------------------------
    # BEACONING DETECTION
    # -------------------------
    # Beaconing ocorre quando um processo se conecta repetidamente
    # ao mesmo IP externo em intervalos regulares (comportamento comum em C2).

    for (processo, ip), quantidade in contagem_conexoes.items():

        # normaliza nome do processo para comparação
        processo_limpo = (processo or "").lower().strip()

        if processo_limpo in PROCESSOS_CONFIAVEIS_CONFIG:
            continue

        if processo_limpo in PROCESSOS_SISTEMA_CONFIG:
            continue

        if not ip_externo(ip):
            continue

        if ip_confiavel(ip):
            continue

        if quantidade >= BEACON_THRESHOLD:

            linha = f"[BEACONING SUSPEITO] {processo} conectou {quantidade} vezes ao IP {ip}"
            resultado.append(linha)

    # -------------------------
    # LISTA DE CONEXÕES
    # -------------------------

    for c in conexoes[:5]:

        linha = f"[CONEXAO] {c['processo']} -> {c['ip']}:{c['porta']}"
        resultado.append(linha)

    # -------------------------
    # PROCESSOS SUSPEITOS
    # -------------------------

    suspeitos = verificar_processos_suspeitos()

    for s in suspeitos:

        linha = f"[PROCESSO SUSPEITO] {s['processo']} PID:{s['pid']}"
        resultado.append(linha)

    # -------------------------
    # LOLBIN DETECTION
    # -------------------------
    # Detecta uso de LOLBins (Living off the Land Binaries).
    # LOLBins são binários legítimos do Windows frequentemente
    # abusados por atacantes para execução de payloads.

    for c in conexoes:

        processo = c["processo"].lower().strip()

        if processo in LOLBINS:

            linha = f"[LOLBIN DETECTADO] {c['processo']} usando rede {c['ip']}:{c['porta']}"
            resultado.append(linha)

    # -------------------------
    # PERSISTÊNCIA
    # -------------------------

    persistencias = verificar_persistencia()

    for p in persistencias:

        linha = f"[PERSISTENCIA] {p['nome']} -> {p['valor']}"
        resultado.append(linha)

    # -------------------------
    # DETECÇÃO DE C2
    # -------------------------
    # Detecta possíveis conexões de Command and Control.
    # Critérios:
    # - processo não confiável
    # - IP externo
    # - IP não presente na allowlist

    for c in conexoes:

        processo = c["processo"].lower().strip()

        if processo in PROCESSOS_CONFIAVEIS_CONFIG:
            continue

        if processo in PROCESSOS_SISTEMA_CONFIG:
            continue

        if ip_externo(c["ip"]) and not ip_confiavel(c["ip"]):

            linha = f"[ALERTA C2] {c['processo']} conectado a {c['ip']}:{c['porta']}"
            resultado.append(linha)

    # -------------------------
    # THREAT INTELLIGENCE
    # -------------------------

    alertas_ti = verificar_threat_intel(conexoes)

    for alerta in alertas_ti:
        resultado.append(alerta)
        registrar_evento(alerta)

    return resultado