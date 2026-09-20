"""
Arquivo principal do BlueSentinel.

Este módulo é o ponto de entrada da aplicação.
Ele registra o início da ferramenta no log e inicia
a interface gráfica do monitor de segurança.
"""

import interface
from utils.logger import registrar_evento


def main():
    """
    Inicializa o BlueSentinel.

    - Registra evento de inicialização
    - Inicia a interface gráfica do monitor
    """

    # registra no log que o sistema foi iniciado
    registrar_evento("BlueSentinel iniciado")

    # inicia a interface principal da aplicação
    interface.iniciar_interface()


if __name__ == "__main__":
    # garante que o programa só execute se este arquivo
    # for rodado diretamente (e não importado como módulo)
    main()