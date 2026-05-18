# 📚 MAIS STUDY PLANNER (MAIS STUDY PLANNER)

> A simple AI-powered study planner web app built by a 2nd semester CS student using **Python Flask**, **HTML**, **CSS**, a little **JavaScript**, and **SQLite**.

This project uses **OOP (Object Oriented Programming)** concepts learned in 2nd semester:
- Classes & Objects
- Constructors
- Method Handling
- Encapsulation
- Abstraction
- Inheritance (Single + Multilevel)
- Operator Overloading (`__add__`, `__lt__`)
- Method Overloading style (default arguments)

---

## ✨ Features

1. **Authentication** – Register, Login, Logout, Session
2. **Dashboard** – Welcome card, weak/average/strong subject stats, performance chart
3. **AI Chat Assistant** – 22+ predefined student replies + voice input (browser based)
4. **PDF Study Assistant** – Upload PDF → Summary, MCQs, Important topics
5. **Smart Study Planner** – Daily / Weekly / Monthly plan, adaptive (weak subjects get more time)
6. **Knowledge Map & Quiz** – Topic-based OOP quiz
7. **Reports & Analytics** – Download in PDF / TXT
8. **Beautiful UI** – Soft modern theme + 🌙 Dark Mode toggle

---

## 📁 Folder Structure

```
ai_study_planner/
│
├── app.py                  # Main Flask file
├── requirements.txt
├── README.md
│
├── models/                 # All OOP classes
│   ├── student.py          # Person -> Student (inheritance, encapsulation)
│   ├── subject.py          # BaseSubject (abstract) -> Subject -> Weak/Strong
│   ├── planner.py          # StudyPlanner (method/operator overloading)
│   ├── ai_helper.py        # AIChatBot + PDFHelper
│   └── report_maker.py     # ReportMaker (PDF/TXT)
│
├── templates/              # HTML pages
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── chat.html
│   ├── pdf.html
│   ├── planner.html
│   ├── quiz.html
│   └── reports.html
│
├── static/
│   ├── css/style.css       # Beautiful soft theme + dark mode
│   └── js/main.js          # Theme toggle (very basic JS)
│
├── uploads/                # Uploaded PDFs go here
├── reports/                # Generated reports go here
└── database/
    └── study.db            # SQLite database (auto-created)
```

---

 Step  — Use the app
1. Click **"Create an account"** and register.
2. Login.
3. Add some subjects with marks on the dashboard.
4. Try **AI Chat**, **PDF Helper**, **Planner**, **Quiz**, **Reports**.
5. Click the 🌙 button (top right) to switch to **Dark Mode**.

---

 💡 Notes for Teachers

- The AI features are **simple rule-based simulations** (not real ML models) to keep the project beginner-friendly.
- OOP concepts are clearly demonstrated in the `models/` folder.
- Code uses simple naming and comments for learning.
- SQLite is auto-created on first run – no setup needed.

---

👨‍💻 Made by
A 2nd Semester CIS Student 💻
