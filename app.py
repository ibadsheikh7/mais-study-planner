from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import os
import sqlite3
from werkzeug.utils import secure_filename

# Importing our own OOP classes from models folder
from models.student import Student
from models.subject import Subject, WeakSubject, StrongSubject
from models.planner import StudyPlanner
from models.ai_helper import AIChatBot, PDFHelper
from models.report_maker import ReportMaker

# ---------- Flask App Setup ----------
app = Flask(__name__)
app.secret_key = "my_secret_key_123"  # used for sessions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'reports'

# Make sure folders exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('reports', exist_ok=True)
os.makedirs('database', exist_ok=True)

DB_PATH = "database/study.db"


# ---------- Database Setup ----------
def create_tables():
    """Create tables if not exist. Simple SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE,
                    password TEXT,
                    semester TEXT
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    sub_name TEXT,
                    marks INTEGER
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS plans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    plan_type TEXT,
                    plan_text TEXT
                )""")
    conn.commit()
    conn.close()


create_tables()


# ---------- Routes ----------

@app.route('/')
def home():
    # If user logged in -> dashboard, else login
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


# ----- Register -----
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        semester = request.form['semester']

        # Using OOP Student class (constructor)
        new_student = Student(name, email, password, semester)
        ok = new_student.save_to_db(DB_PATH)

        if ok:
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error="Email already exists!")
    return render_template('register.html')


# ----- Login -----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        student = Student.login(DB_PATH, email, password)
        if student:
            session['user_id'] = student['id']
            session['user_name'] = student['name']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Wrong email or password!")
    return render_template('login.html')


# ----- Logout -----
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ----- Dashboard -----
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    student_id = session['user_id']

    # Get subjects from DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sub_name, marks FROM subjects WHERE student_id=?", (student_id,))
    rows = c.fetchall()
    conn.close()

    # Use OOP Subject classes (Inheritance + Abstraction)
    subject_list = []
    weak, avg, strong = [], [], []
    for r in rows:
        sub = Subject(r[0], r[1])
        subject_list.append(sub)
        level = sub.get_level()
        if level == "Weak":
            weak.append(sub.name)
        elif level == "Strong":
            strong.append(sub.name)
        else:
            avg.append(sub.name)

    # For chart
    chart_labels = [s.name for s in subject_list]
    chart_data = [s.marks for s in subject_list]

    return render_template('dashboard.html',
                           name=session['user_name'],
                           subjects=subject_list,
                           weak=weak, avg=avg, strong=strong,
                           chart_labels=chart_labels,
                           chart_data=chart_data)


# ----- Add Subject -----
@app.route('/add_subject', methods=['POST'])
def add_subject():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    sub_name = request.form['sub_name']
    marks = int(request.form['marks'])

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO subjects (student_id, sub_name, marks) VALUES (?, ?, ?)",
              (session['user_id'], sub_name, marks))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))


# ----- AI Chat -----
@app.route('/chat')
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('chat.html', name=session['user_name'])


@app.route('/chat_reply', methods=['POST'])
def chat_reply():
    user_msg = request.json.get('message', '')
    bot = AIChatBot()
    reply = bot.get_reply(user_msg)
    return jsonify({"reply": reply})


# ----- PDF Assistant -----
@app.route('/pdf', methods=['GET', 'POST'])
def pdf_assistant():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    summary, mcqs, important = None, None, None
    if request.method == 'POST':
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)

                # Use OOP PDFHelper
                helper = PDFHelper(path)
                summary = helper.make_summary()
                mcqs = helper.make_mcqs()
                important = helper.important_topics()

    return render_template('pdf.html', summary=summary, mcqs=mcqs, important=important)


# ----- Smart Planner -----
@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    plan = None
    plan_type = "daily"
    if request.method == 'POST':
        exam_date = request.form['exam_date']
        plan_type = request.form['plan_type']
        subjects_text = request.form['subjects']

        # Get weak/strong from db for adaptive plan
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT sub_name, marks FROM subjects WHERE student_id=?", (session['user_id'],))
        rows = c.fetchall()
        conn.close()

        weak_list = [r[0] for r in rows if r[1] < 50]
        strong_list = [r[0] for r in rows if r[1] >= 75]

        # Using OOP StudyPlanner (Method Overloading style + Operator Overloading)
        sp = StudyPlanner(exam_date, subjects_text.split(','))
        sp.set_levels(weak_list, strong_list)
        plan = sp.make_plan(plan_type)

        # Save in DB
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO plans (student_id, plan_type, plan_text) VALUES (?, ?, ?)",
                  (session['user_id'], plan_type, "\n".join(plan)))
        conn.commit()
        conn.close()

    return render_template('planner.html', plan=plan, plan_type=plan_type)


# ----- Quiz (PDF-based) -----
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    mcqs = None
    topic_name = None
    if request.method == 'POST':
        if 'pdf_file' in request.files:
            file = request.files['pdf_file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)

                # Quiz is generated only from uploaded PDF
                helper = PDFHelper(path)
                mcqs = helper.make_mcqs()
                topic_name = filename

    return render_template('quiz.html', mcqs=mcqs, topic_name=topic_name)


# ----- CGPA Calculator -----
@app.route('/cgpa', methods=['GET', 'POST'])
def cgpa():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    result = None
    rows_data = []
    if request.method == 'POST':
        names = request.form.getlist('course_name')
        credits = request.form.getlist('credit')
        grades = request.form.getlist('grade')
        marks_list = request.form.getlist('marks_obtained')

        # Grade point mapping (standard 4.0 scale)
        gp_map = {
            "A+": 4.0, "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0, "F": 0.0
        }

        def marks_to_grade(marks):
            if marks >= 95: return "A+"
            elif marks >= 90: return "A"
            elif marks >= 85: return "A-"
            elif marks >= 80: return "B+"
            elif marks >= 75: return "B"
            elif marks >= 70: return "B-"
            elif marks >= 65: return "C+"
            elif marks >= 60: return "C"
            elif marks >= 55: return "C-"
            elif marks >= 50: return "D+"
            elif marks >= 45: return "D"
            else: return "F"

        total_points = 0.0
        total_credits = 0.0
        # Pad marks_list if shorter
        while len(marks_list) < len(names):
            marks_list.append("")

        for n, cr, g, mk in zip(names, credits, grades, marks_list):
            if not n.strip():
                continue
            try:
                cr_v = float(cr)
            except:
                cr_v = 0
            # If marks provided, auto-derive grade
            if mk.strip():
                try:
                    mk_val = float(mk.strip())
                    g = marks_to_grade(mk_val)
                except:
                    pass
            gp = gp_map.get(g.upper().strip(), 0.0)
            points = cr_v * gp
            total_points += points
            total_credits += cr_v
            rows_data.append({"name": n, "credit": cr_v, "grade": g.upper(), "gp": gp, "points": round(points, 2)})

        if total_credits > 0:
            cgpa_val = round(total_points / total_credits, 2)
        else:
            cgpa_val = 0.0
        result = {"cgpa": cgpa_val, "total_credits": total_credits, "total_points": round(total_points, 2)}

    return render_template('cgpa.html', result=result, rows=rows_data)



# ----- Reports -----
@app.route('/reports')
def reports():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sub_name, marks FROM subjects WHERE student_id=?", (session['user_id'],))
    rows = c.fetchall()
    conn.close()

    return render_template('reports.html',
                           subjects=rows,
                           name=session['user_name'])


@app.route('/download/<ftype>')
def download_report(ftype):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sub_name, marks FROM subjects WHERE student_id=?", (session['user_id'],))
    rows = c.fetchall()
    conn.close()

    rm = ReportMaker(session['user_name'], rows)
    if ftype == "txt":
        path = rm.make_txt(app.config['REPORT_FOLDER'])
    else:
        path = rm.make_pdf(app.config['REPORT_FOLDER'])

    return send_file(path, as_attachment=True)


# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True)
