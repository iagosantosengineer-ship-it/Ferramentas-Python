# Lista simples de IOC (Indicators of Compromise)
# Domínios frequentemente utilizados em atividades maliciosas
# ou infraestrutura de C2.
DOMINIOS_SUSPEITOS = [
    "pastebin.com",
    "ngrok.io",
    "duckdns.org",
    "no-ip.org",
    "discord.com",
    "raw.githubusercontent.com"
]


def verificar_threat_intel(conexoes):
    """
    Aplica uma verificação básica de Threat Intelligence.

    Compara conexões de rede com uma lista de domínios
    frequentemente utilizados por malware, C2 ou
    infraestrutura de ataque.
    """

    alertas = []

    for c in conexoes:

        ip = c["ip"]
        processo = c["processo"]

        for dominio in DOMINIOS_SUSPEITOS:

            # verifica se o domínio suspeito aparece no destino da conexão
            if dominio in ip:

                alerta = f"[THREAT INTEL] {processo} conectado a {ip}"
                alertas.append(alerta)

    return alertas