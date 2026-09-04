# 🚀 Study Tracker (LeetCode)

A Python-based CLI application to track, store, and analyze LeetCode problems.  
Helps identify weak areas and improve consistency using simple data insights.

---

## 📌 Features

- ✅ Add solved problems (name, difficulty, topic)
- 📂 Store data in JSON format
- 📊 Analyze:
  - Problems by difficulty
  - Problems by topic
- ⚠️ Detect weakest topic automatically
- 🧠 Simple CLI interface

---

## 🛠️ Tech Stack

- Python 🐍
- JSON (data storage)
- collections.Counter
- Git & GitHub

---

## 📂 Project Structure

study-tracker/
│── main.py  
│── data.json  
│── README.md  

---

## ▶️ How to Run
python main.py

## 🧠 How It Works

- Add a solved problem with difficulty and topic
- Data is stored in `data.json`
- Analyze option shows:
  - Problems by difficulty
  - Problems by topic
  - Weakest topic (based on least count)
