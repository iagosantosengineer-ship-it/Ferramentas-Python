def calculate_score(data, is_blacklisted):
    score = 0

    if is_blacklisted:
        score += 70

    hostname = data["hostname"].lower()

    if hostname == "n/a":
        score += 10

    if "tor" in hostname:
        score += 50

    return score


def classify(score):
    if score >= 70:
        return "MALICIOUS"
    elif score >= 30:
        return "SUSPICIOUS"
    else:
        return "BENIGN"