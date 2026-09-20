import json
import socket
from datetime import datetime


def salvar_relatorio(alertas):

    dados = {
        "host": socket.gethostname(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "alertas": alertas
    }

    with open("relatorio_bluesentinel.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)