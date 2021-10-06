import json

#Dictionary commands

DB_FILE = "dictionary.json"

def read():
    with open(DB_FILE, "r") as f:
        data = f.read()
    try:
        return json.loads(data)
    except:
        print("Corrupted database file.")

def update(data):
    with open(DB_FILE, "w+") as f:
        f.write(json.dumps(data))

def sort(data):
    #return {k: v for k, v in sorted(data.items(), key=lambda item: -item[1]["ELO"])}
    return