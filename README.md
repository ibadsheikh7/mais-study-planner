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

## 🛠 How to Run (Step by Step)

### Step 1 — Extract the ZIP file
After downloading, right-click the `.zip` file and choose **"Extract All"**.
You will get a folder named `ai_study_planner`.

### Step 2 — Open in VS Code
1. Open **VS Code**.
2. Go to **File → Open Folder...**
3. Select the extracted `ai_study_planner` folder.
4. Open the built-in terminal: **View → Terminal** (or press `` Ctrl + ` ``).

### Step 3 — Make sure Python is installed
In the terminal type:
```bash
python --version
```
If you see a version (like `Python 3.11`), you’re good. If not, install Python from [python.org](https://www.python.org/downloads/) and tick *"Add Python to PATH"* during install.

### Step 4 — (Recommended) Create a Virtual Environment
```bash
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac / Linux:** `source venv/bin/activate`

You will see `(venv)` at the start of your terminal line.

### Step 5 — Install required libraries
```bash
pip install -r requirements.txt
```

### Step 6 — Run the Flask app
```bash
python app.py
```

You will see something like:
```
 * Running on http://127.0.0.1:5000
```

### Step 7 — Open in browser
Open this link in your browser:
```
http://127.0.0.1:5000
```

### Step 8 — Use the app
1. Click **"Create an account"** and register.
2. Login.
3. Add some subjects with marks on the dashboard.
4. Try **AI Chat**, **PDF Helper**, **Planner**, **Quiz**, **Reports**.
5. Click the 🌙 button (top right) to switch to **Dark Mode**.

---

## 💡 Notes for Teachers

- The AI features are **simple rule-based simulations** (not real ML models) to keep the project beginner-friendly.
- OOP concepts are clearly demonstrated in the `models/` folder.
- Code uses simple naming and comments for learning.
- SQLite is auto-created on first run – no setup needed.

---

## 👨‍💻 Made by
A 2nd Semester CIS Student 💻
