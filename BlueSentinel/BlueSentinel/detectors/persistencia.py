import winreg


# Chaves do registro que permitem execução automática de programas
# no login do usuário (persistência comum utilizada por malware)
RUN_KEYS = [
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
]


def verificar_persistencia():
    """
    Verifica possíveis mecanismos de persistência no registro do Windows.

    Muitas ameaças adicionam entradas nas Run Keys para garantir
    execução automática após reinicialização ou login do usuário.
    """

    resultados = []

    for hive, chave in RUN_KEYS:

        try:
            registro = winreg.OpenKey(
                hive,
                chave,
                0,
                winreg.KEY_READ
            )

            i = 0

            while True:

                try:
                    nome, valor, tipo = winreg.EnumValue(registro, i)

                    resultados.append({
                        "nome": nome,
                        "valor": valor
                    })

                    i += 1

                # EnumValue gera OSError quando não há mais entradas
                except OSError:
                    break

        except Exception as e:
            print("[ERRO] Falha ao acessar registro:", e)

    return resultados