import json

def save_log(output):
    with open("logs.json", "a") as f:
        f.write(json.dumps(output) + "\n")  


def print_json(output):
    print("\nJSON OUTPUT:")
    print(json.dumps(output, indent=4))  