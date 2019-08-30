import json

def load_raw(filename):
    with open(filename,"r") as file:
        return file.read()

def load_file(n):
    # n is an integer
    raw = load_raw("war_card_data/data/"+str(n)+".json")
    j = json.loads(raw)
    return j