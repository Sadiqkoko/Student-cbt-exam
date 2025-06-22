import os
import time
import json
import random
import sqlite3
import io
import csv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cbt_secret_key'

start_time = time.time()
# wata processing
time.sleep(1)
end_time = time.time()
print("Time taken:", end_time - start_time)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('cbt_database.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

# CBT Exam Time Limit (e.g., 10 minutes for each exam)
TIME_LIMIT = 10  # minutes

# Function to fetch questions from the database

def get_questions_from_db(course_code):
    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT question_text, option_a, option_b, option_c, option_d, correct_option 
        FROM cbt_questions 
        WHERE course_code = ?
    """, (course_code,))
    
    questions = cursor.fetchall()
    conn.close()
    
    return questions

@app.route('/choose_course', methods=['GET', 'POST'])
def choose_course():
    if 'student_id' not in session:
        return redirect('/cbt_login')

    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course_code FROM cbt_questions")
    courses = [row[0] for row in cursor.fetchall()]
    conn.close()

    if request.method == 'POST':
        selected_course = request.form.get('course_code')
        return redirect(url_for('cbt_take_exam', course_code=selected_course))

    return render_template('choose_course.html', courses=courses)

@app.route('/cbt_take_exam/<course_code>', methods=['GET', 'POST'])
def cbt_take_exam(course_code):
    if 'student_id' not in session:
        return redirect('/cbt_login')

    admission_number = session.get('admission_number')  # assume admission_number is in session

    conn = sqlite3.connect('cbt_database.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # PREVENT RE-TAKE: Check if student already took this course
    cursor.execute("SELECT * FROM cbt_taken WHERE admission_number = ? AND course_code = ?", 
                   (admission_number, course_code))
    already_taken = cursor.fetchone()
    if already_taken:
        conn.close()
        return "You have already taken this CBT. Re-taking is not allowed."

    # Fetch questions
    cursor.execute("SELECT * FROM cbt_questions WHERE course_code = ?", (course_code,))
    all_questions = cursor.fetchall()

    if not all_questions:
        conn.close()
        return redirect(url_for('choose_course'))

    import random
    selected_questions = random.sample(all_questions, min(40, len(all_questions)))
    questions = [dict(row) for row in selected_questions]

    if request.method == 'POST':
        submitted_answers = request.form
        score = 0
        total_questions = len(questions)

        for q in questions:
            qid = str(q['id'])
            correct_answer = q['correct_answer']
            student_answer = submitted_answers.get(qid, '').strip().lower()
            if student_answer == correct_answer.strip().lower():
                score += 1

        percentage = (score / total_questions) * 100

        # Grade logic
        if percentage >= 70:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 45:
            grade = 'D'
        elif percentage >= 40:
            grade = 'E'
        else:
            grade = 'F'

        from datetime import datetime
        date_taken = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save result to cbt_admin_result
        cursor.execute('''
            INSERT INTO cbt_admin_result (admission_number, course_code, score, total_questions, date_taken)
            VALUES (?, ?, ?, ?, ?)
        ''', (admission_number, course_code, score, total_questions, date_taken))

        # Insert into cbt_taken to prevent re-take
        cursor.execute('''
            INSERT INTO cbt_taken (admission_number, course_code, date_taken)
            VALUES (?, ?, ?)
        ''', (admission_number, course_code, date_taken))

        conn.commit()
        conn.close()

        return redirect(url_for('exam_completed'))

    conn.close()
    return render_template('cbt_take_exam.html', questions=questions, course_code=course_code, TIME_LIMIT=40)

@app.route('/')
def index():
    return render_template('cbt_home.html')

@app.route('/cbt_register', methods=['GET', 'POST'])
def cbt_register():
    if request.method == 'POST':
        name = request.form['name']
        admission_number = request.form['admission_number']
        email = request.form['email']
        level = request.form['level']
        department = request.form['department']
        session = request.form['session']
        address = request.form['address']
        phone = request.form['phone']
        password = request.form['password']
        profile_picture = 'default.jpg'  # ko ka iya daina amfani da shi

        conn = get_db_connection()
        existing = conn.execute("SELECT * FROM students WHERE admission_number = ?", (admission_number,)).fetchone()
        if existing:
            conn.close()
            return "Admission number already registered!"

        conn.execute('''
            INSERT INTO students (
                name, admission_number, password, email,
                level, department, session, address, phone, profile_picture
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, admission_number, password, email, level, department, session, address, phone, profile_picture))

        conn.commit()
        conn.close()
        return redirect(url_for('cbt_login'))

    return render_template('cbt_register.html')

# Login (Admin/Student)
@app.route('/cbt_login', methods=['GET', 'POST'])
def cbt_login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        conn = get_db_connection()
        
        # Admin login
        admin = conn.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (user, password)).fetchone()
        if admin:
            session['admin'] = user
            conn.close()
            return redirect(url_for('cbt_admin_dashboard'))

        # Student login
        student = conn.execute("SELECT * FROM students WHERE admission_number = ? AND password = ?", (user, password)).fetchone()
        if student:
            session['student_id'] = student['id']
            session['student_name'] = student['name']
            session['admission_number'] = student['admission_number']
            conn.close()
            return redirect(url_for('cbt_student_dashboard'))

        conn.close()
        return "Invalid login"
    
    return render_template('cbt_login.html')

# Admin dashboard
@app.route('/cbt_admin_dashboard')
def cbt_admin_dashboard():
    if 'admin' in session:
        conn = sqlite3.connect('cbt_database.sqlite3')
        cursor = conn.cursor()

        # Jimillar students
        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]

        # Students da suka rubuta exam (assuming cbt_results ko cbt_scores table)
        cursor.execute("SELECT COUNT(DISTINCT admission_number) FROM student_submissions")
        students_exam_taken = cursor.fetchone()[0]

        conn.close()

        admin_name = session.get('admin_name', 'Admin User')
        admin_email = session.get('admin_email', 'admin@example.com')
        admin_photo_url = url_for('static', filename='images/admin_profile.png')

        return render_template('cbt_admin_dashboard.html', 
                               admin_name=admin_name, 
                               admin_email=admin_email,
                               admin_photo_url=admin_photo_url,
                               total_students=total_students,
                               students_exam_taken=students_exam_taken)
    return redirect(url_for('cbt_login'))

@app.route('/cbt_view_questions', methods=['GET'])
def cbt_view_questions():
    if 'admin' not in session:
        return redirect(url_for('cbt_login'))
    
    conn = sqlite3.connect('cbt_database.sqlite3')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM cbt_courses")
    courses = c.fetchall()

    course_code = request.args.get('course_code')
    questions = []
    if course_code:
        c.execute("SELECT * FROM cbt_questions WHERE course_code = ? LIMIT 40", (course_code,))
        questions = c.fetchall()

    conn.close()
    return render_template('cbt_view_questions.html', courses=courses, questions=questions, selected_course=course_code)

@app.route('/cbt_admin_add_questions', methods=['GET', 'POST'])
def cbt_admin_add_questions():
    if 'admin' not in session:
        return redirect(url_for('cbt_login'))
    
    conn = get_db_connection()
    courses = conn.execute('SELECT course_code, course_title FROM cbt_courses').fetchall()

    if request.method == 'POST':
        course_code = request.form['course_code']
        question = request.form['question']
        option_a = request.form['option_a']
        option_b = request.form['option_b']
        option_c = request.form['option_c']
        option_d = request.form['option_d']
        correct = request.form['correct']
        image_path = request.form.get('image_path', '')

        conn.execute('''
            INSERT INTO cbt_questions (course_code, question_text, option_a, option_b, option_c, option_d, correct_answer, image_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (course_code, question, option_a, option_b, option_c, option_d, correct, image_path)
        )
        conn.commit()
        conn.close()
        return "Question added successfully!"

    conn.close()
    return render_template('cbt_admin_add_questions.html', courses=courses)

# Student dashboard
@app.route('/cbt_student_dashboard')
def cbt_student_dashboard():
    if 'student_id' in session:
        return render_template('cbt_student_dashboard.html', name=session['student_name'])
    return redirect(url_for('cbt_login'))

# Create folder if not exists
if not os.path.exists('static/profile_pictures'):
    os.makedirs('static/profile_pictures')

# Define helper function to get student
def get_student_by_id(student_id):
    conn = get_db_connection()
    student = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    conn.close()
    return student

# Define helper function to update profile picture
def update_student_picture(student_id, filename):
    conn = get_db_connection()
    conn.execute("UPDATE students SET profile_picture = ? WHERE id = ?", (filename, student_id))
    conn.commit()
    conn.close()

# Student Profile Route
@app.route('/cbt_student_profile', methods=['GET', 'POST'])
def cbt_student_profile():
    student_id = session.get('student_id')
    if not student_id:
        return redirect(url_for('cbt_login'))

    student = get_student_by_id(student_id)

    if request.method == 'POST':
        if 'profile_picture' in request.files:
            profile_picture = request.files['profile_picture']
            if profile_picture.filename != '':
                filename = secure_filename(profile_picture.filename)
                filepath = os.path.join('static/profile_pictures', filename)
                profile_picture.save(filepath)
                update_student_picture(student_id, filename)
                flash('Profile picture updated successfully!', 'success')
                return redirect(url_for('cbt_student_profile'))

    return render_template('cbt_student_profile.html', student=student)

@app.route('/cbt_student_logout')
def cbt_student_logout():
    session.pop('student_id', None)
    flash("An fita daga CBT dashboard cikin nasara.", "info")
    return redirect(url_for('cbt_login'))

@app.route('/cbt_student_results/<admission_number>', methods=['GET', 'POST'])
def cbt_student_results(admission_number):
    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()

    # Dauko sunan student
    cursor.execute("SELECT name FROM students WHERE admission_number=?", (admission_number,))
    student = cursor.fetchone()
    if not student:
        return "Student not found", 404
    name = student[0]

    # Dauko results student din
    cursor.execute('''
        SELECT course_code, score, total_questions, date_taken
        FROM cbt_admin_result
        WHERE admission_number=?
    ''', (admission_number,))
    results = cursor.fetchall()
    conn.close()

    # Idan an danna download button
    if request.method == 'POST' and request.form.get('download') == 'Download':
        # Create CSV in-memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Course Code', 'Score', 'Total Questions', 'Date Taken'])
        writer.writerows(results)
        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode()),
                         mimetype='text/csv',
                         download_name=f'{admission_number}_results.csv',
                         as_attachment=True)

    return render_template('cbt_student_results.html', student_name=student_name, admission_number=admission_number, results=results)

# Admin Edit Result Page
@app.route('/cbt_admin_edit_result/<int:result_id>', methods=['GET'])
def cbt_admin_edit_result(result_id):
    if 'admin' not in session:
        return redirect(url_for('cbt_login'))

    conn = get_db_connection()
    result = conn.execute('''
        SELECT student_submissions.id, students.name, students.admission_number, student_submissions.score, student_submissions.date_taken, student_submissions.courses
        FROM student_submissions
        JOIN students ON student_submissions.student_id = students.id
        WHERE student_submissions.id = ?
    ''', (result_id,)).fetchone()

    conn.close()

    if result:
        return render_template('cbt_admin_edit_result.html', result=result)
    return redirect(url_for('cbt_admin_results'))


# Admin Update Result
@app.route('/cbt_admin_update_result/<int:result_id>', methods=['POST'])
def cbt_admin_update_result(result_id):
    if 'admin' not in session:
        return redirect(url_for('cbt_login'))

    score = request.form['score']
    courses = request.form['courses']

    conn = get_db_connection()
    conn.execute('''
        UPDATE student_submissions
        SET score = ?, courses = ?
        WHERE id = ?
    ''', (score, courses, result_id))

    conn.commit()
    conn.close()

    return redirect(url_for('cbt_admin_results'))

    conn = get_db_connection()
    results = conn.execute('''
        SELECT score, date_taken FROM student_submissions 
        WHERE student_id = ?
        ORDER BY date_taken DESC
    ''', (session['student_id'],)).fetchall()

    settings = conn.execute("SELECT * FROM exam_settings LIMIT 1").fetchone()
    conn.close()

    return render_template('cbt_student_result.html', results=[{
        'score': r['score'],
        'date_taken': r['date_taken'],
        'total': settings['total_questions']
    } for r in results])

@app.route('/cbt_admin_result', methods=['GET', 'POST'])
def cbt_admin_result():
    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()

    if request.method == 'POST':
        admission_number = request.form['admission_number']
        course_code = request.form['course_code']
        score = int(request.form['score'])
        total_questions = int(request.form['total_questions'])  # ya kamata a turo total_questions daga form
        date_taken = request.form['date_taken']  # misali '2025-05-17'
        session = request.form['session']
        semester = request.form['semester']

        # Grade system
        if score >= 70:
            grade = 'A'
        elif score >= 60:
            grade = 'B'
        elif score >= 50:
            grade = 'C'
        elif score >= 45:
            grade = 'D'
        elif score >= 40:
            grade = 'E'
        else:
            grade = 'F'

        # Calculate percentage
        percentage = (score / total_questions) * 100

        # Simple GPA calculation (example)
        gpa_dict = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'E':0.7, 'F':0.0}
        gpa = gpa_dict.get(grade, 0.0)

        # Insert into student_submissions
        cursor.execute('''
            INSERT INTO student_submissions 
            (admission_number, course_code, score, total_questions, percentage, grade, gpa, date_taken, result_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (admission_number, course_code, score, total_questions, percentage, grade, gpa, date_taken, 'Sent'))
        conn.commit()
        flash("Result sent to student successfully.")

    # Fetch all results from cbt_admin_result table
    cursor.execute('''
        SELECT admission_number, course_code, score, total_questions, date_taken
        FROM cbt_admin_result
        ORDER BY date_taken DESC
    ''')
    results = cursor.fetchall()
    conn.close()

    return render_template('student_result_detail.html', results=results)

@app.route('/cbt_admin_send_results', methods=['GET', 'POST'])
def cbt_admin_send_results():
    if request.method == 'POST':
        admission_number = request.form['admission_number']
        course_code = request.form['course_code']
        score = request.form['score']
        grade = request.form['grade']
        session = request.form['session']
        semester = request.form['semester']

        conn = sqlite3.connect('cbt_database.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO results (admission_number, course_code, score, grade, session, semester) VALUES (?, ?, ?, ?, ?, ?)", 
                  (admission_number, course_code, score, grade, session, semester))
        conn.commit()
        conn.close()
        flash('Result sent successfully!')
        return redirect(url_for('cbt_admin_send_results'))

    return render_template('cbt_admin_send_results.html')

@app.route('/view_student_result/<admission_number>')
def view_student_result(admission_number):
    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT course_code, score, total_questions, date_taken
        FROM cbt_admin_result
        WHERE admission_number = ?
    ''', (admission_number,))
    
    student_results = cursor.fetchall()
    conn.close()
    
    return render_template('student_result_detail.html', admission_number=admission_number, results=student_results)

@app.route('/cbt_admin_logout')
def cbt_admin_logout():
    session.pop('cbt_admin_logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('cbt_login'))  # change this if your login route name is different

@app.route('/exam_completed')
def exam_completed():
    score = len(session.get('answers', []))
    total = len(session.get('questions', []))
    session.clear()
    return render_template('exam_completed.html', score=score, total=total)

def get_cbt_courses_for_student(admission_number):
    conn = sqlite3.connect('cbt_database.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO cbt_courses (
        admission_number, course_code, course_title,
        department, level, semester
    ) VALUES (?, ?, ?, ?, ?, ?)
''', (admission_number, code, title, department, level, semester))
    courses = cursor.fetchall()
    conn.close()
    return courses

@app.route('/cbt_student_courses')
def cbt_student_courses():
    if 'admission_number' not in session:
        return redirect(url_for('cbt_login'))

    admission_number = session['admission_number']

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Samo department da level na ɗalibin
    cursor.execute("SELECT department, level FROM students WHERE admission_number = ?", (admission_number,))
    student = cursor.fetchone()

    if student is None:
        conn.close()
        return "Student not found."

    department = student['department']
    level = student['level']

    # Samo department courses
    cursor.execute("""
        SELECT * FROM cbt_courses
        WHERE department = ? AND level = ?
    """, (department, level))
    courses = cursor.fetchall()

    # Samo electives da suka dace da level
    cursor.execute("""
        SELECT * FROM cbt_courses
        WHERE department = 'Electives' AND level = ?
    """, (level,))
    electives = cursor.fetchall()

    conn.close()

    return render_template('cbt_student_courses.html', courses=courses, electives=electives)

@app.route('/save_selected_courses', methods=['POST'])
def save_selected_courses():
    if 'admission_number' not in session:
        return redirect(url_for('cbt_login'))

    selected = request.form.getlist('selected_courses')
    admission_number = session['admission_number']

    conn = get_db_connection()
    cursor = conn.cursor()

    for course_code in selected:
        cursor.execute("INSERT INTO student_selected_courses (admission_number, course_code) VALUES (?, ?)", 
                       (admission_number, course_code))

    conn.commit()
    conn.close()

    return "Courses selected successfully."

@app.route('/view_selected_courses')
def view_selected_courses():
    if 'admission_number' not in session:
        return redirect(url_for('cbt_login'))

    admission_number = session['admission_number']

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.course_code, c.course_title, c.semester
        FROM student_selected_courses s
        JOIN cbt_courses c ON s.course_code = c.course_code
        WHERE s.admission_number = ?
    """, (admission_number,))

    selected_courses = cursor.fetchall()
    conn.close()

    return render_template('view_selected_courses.html', selected_courses=selected_courses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)