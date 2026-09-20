import requests

def update_blacklist():
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

    response = requests.get(url)

    with open("blacklist.txt", "w") as f:
        f.write(response.text)


def load_blacklist():
    try:
        with open("blacklist.txt", "r") as f:
            return set(line.strip() for line in f if line.strip() and not line.startswith("#"))
    except:
        return set()


def check_blacklist(ip, blacklist):
    return ip in blacklist