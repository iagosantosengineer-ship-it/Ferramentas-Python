import os
import json
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "events.log")


def registrar_evento(evento):

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().isoformat()

    tipo = "INFO"

    if "[" in evento and "]" in evento:
        tipo = evento.split("]")[0].replace("[", "")

    log = {
        "timestamp": timestamp,
        "tipo": tipo,
        "evento": evento
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")