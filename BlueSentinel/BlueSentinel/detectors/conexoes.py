import psutil


def verificar_conexoes():
    """
    Coleta conexões de rede ativas do sistema e associa cada conexão
    ao processo responsável.

    Utilizado pelo scanner principal para identificar:
    - conexões externas
    - possíveis C2
    - uso de LOLBins em comunicação de rede
    """

    resultados = []

    # coleta conexões TCP/UDP IPv4 e IPv6
    for conn in psutil.net_connections(kind="inet"):

        # apenas conexões que possuem endereço remoto
        if conn.raddr:

            try:
                processo = psutil.Process(conn.pid)
                nome = processo.name()

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                nome = "desconhecido"

            ip = conn.raddr.ip
            porta = conn.raddr.port

            resultados.append({
                "processo": nome,
                "ip": ip,
                "porta": porta
            })

    return resultados