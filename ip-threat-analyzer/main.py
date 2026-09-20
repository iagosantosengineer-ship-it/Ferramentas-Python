import datetime

from core.enrichment import get_ip_info
from core.detection import load_blacklist, check_blacklist, update_blacklist
from core.scoring import calculate_score, classify
from utils.logger import save_log, print_json


def main():
    print("[*] Atualizando blacklist...")
    update_blacklist()

    blacklist = load_blacklist()

    ip = input("Digite um IP: ")

    data = get_ip_info(ip)

    is_blacklisted = check_blacklist(ip, blacklist)

    score = calculate_score(data, is_blacklisted)

    classification = classify(score)

    # motivo da classificação (diferencial SOC)
    reason = "Unknown"

    if is_blacklisted:
        reason = "IP found in threat intelligence blacklist"

    elif "tor" in data["hostname"].lower():
        reason = "Tor exit node detected (anonymization network)"

    elif data["hostname"] == "N/A":
        reason = "No reverse DNS (low confidence / unknown host)"

    output = {
        "ip": ip,
        "hostname": data["hostname"],
        "blacklisted": is_blacklisted,
        "score": score,
        "classification": classification,
        "reason": reason,
        "timestamp": str(datetime.datetime.now())
    }

    print("\n===== RESULTADO =====")
    print(f"IP: {ip}")
    print(f"Hostname: {data['hostname']}")
    print(f"Blacklist: {'SIM' if is_blacklisted else 'NAO'}")
    print(f"Score: {score}")
    print(f"Classificação: {classification}")
    print(f"Motivo: {reason}")

    print_json(output)
    save_log(output)


if __name__ == "__main__":
    main()