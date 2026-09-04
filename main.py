import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_entry():
    problem = input("Problem name: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    topic = input("Topic (Array/String/DP...): ")

    entry = {
        "problem": problem,
        "difficulty": difficulty,
        "topic": topic,
        "date": str(datetime.now().date())
    }

    data = load_data()
    data.append(entry)
    save_data(data)

    print("✅ Entry saved!")

add_entry()