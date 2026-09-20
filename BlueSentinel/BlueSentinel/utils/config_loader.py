import os
import sys
import json


def caminho_config():
    """
    Determina o caminho do arquivo de configuração.

    O comportamento muda dependendo de como o programa está sendo executado:

    - Executável (.exe): procura o config.json na mesma pasta do executável.
    - Modo desenvolvimento (python main.py): usa o config.json dentro da pasta config.
    """

    # Se o programa estiver rodando como executável (PyInstaller)
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
        return os.path.join(base_path, "config.json")

    # Se estiver rodando em modo desenvolvimento
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "..", "config", "config.json")


def caminho_template():
    """
    Caminho do arquivo de configuração padrão (template).

    Esse arquivo é usado caso o config.json não exista.
    """

    # Se rodando como executável
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
        return os.path.join(base_path, "config_template.json")

    # Modo desenvolvimento
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "..", "config", "config_template.json")


def carregar_config():
    """
    Carrega o arquivo config.json.

    Retorna:
        dict: configuração carregada.

        Comportamento:
        - Se config.json existir → usa ele
        - Se não existir → usa config_template.json
        - Se nenhum existir → retorna dicionário vazio
    """

    config_path = caminho_config()
    template_path = caminho_template()

    print("[DEBUG] Caminho do config:", config_path)

    # Se existir config.json
    if os.path.exists(config_path):

        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Se não existir, tenta usar o template
    print("[AVISO] config.json não encontrado, tentando usar config_template.json")

    if os.path.exists(template_path):

        with open(template_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Se nenhum existir
    print("[ERRO] Nenhum arquivo de configuração encontrado")

    return {}