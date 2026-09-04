import json
from datetime import datetime
from collections import Counter

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

    print("✅ Entry saved")

def analyze():
    data = load_data()

    if not data:
        print("No data yet")
        return

    diff_count = Counter([d["difficulty"] for d in data])
    topic_count = Counter([d["topic"] for d in data])

    print("\n📊 Analysis")
    print("Difficulty:", dict(diff_count))
    print("Topics:", dict(topic_count))

    weak_topic = min(topic_count, key=topic_count.get)
    print("⚠️ Weak Area:", weak_topic)

while True:
    print("\n1. Add Entry")
    print("2. Analyze Data")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        analyze()
    elif choice == "3":
        break
    else:
        print("Invalid option")