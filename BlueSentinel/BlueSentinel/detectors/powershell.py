import psutil


# Lista de processos frequentemente utilizados em ataques
# (LOLBins - Living off the Land Binaries)
PROCESSOS_SUSPEITOS = [
    "powershell.exe",
    "cmd.exe",
    "wscript.exe",
    "cscript.exe",
    "mshta.exe",
    "rundll32.exe"
]


def verificar_processos_suspeitos():
    """
    Identifica processos potencialmente abusados por atacantes.

    Muitos ataques utilizam binários legítimos do Windows
    para executar scripts ou payloads maliciosos sem levantar suspeitas.
    Essa técnica é conhecida como LOLBins (Living off the Land Binaries).
    """

    resultados = []

    for proc in psutil.process_iter(['pid', 'name']):

        try:
            nome = proc.info['name']

            if nome and nome.lower() in PROCESSOS_SUSPEITOS:

                resultados.append({
                    "processo": nome,
                    "pid": proc.info['pid']
                })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return resultados