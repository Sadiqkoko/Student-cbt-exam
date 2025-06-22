import sqlite3
from datetime import datetime
import random  # ADD THIS

# Haɗa ko ƙirƙirar CBT database
conn = sqlite3.connect('cbt_database.sqlite3')
cursor = conn.cursor()

# --- Teburin Admin ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
cursor.execute("SELECT COUNT(*) FROM admin")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ('admin', '12345678'))

# --- Teburin Students ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        admission_number TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        level TEXT NOT NULL,
        department TEXT NOT NULL,
        session TEXT NOT NULL,
        address TEXT,
        phone TEXT,
        profile_picture TEXT DEFAULT ''
    )
''')

# Shigar da ɗalibai idan babu kowa a cikin teburin
cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO students (
            name, admission_number, password, email,
            level, department, session, address, phone, profile_picture
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        ('Abubakar Suleman', '2310203081', '12345678', 'abubakar@example.com',
         '100L', 'Computer Science', '2024/2025', 'Koko', '08012345678', ''),
        ('Sadik Musa', '2310203064', '12345678', 'sadik@example.com',
         '100L', 'Computer Science', '2024/2025', 'Koko', '08087654321', '')
    ])

# --- Ƙirƙirar Teburin CBT Courses ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cbt_courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT NOT NULL,
        course_title TEXT NOT NULL,
        department TEXT NOT NULL,
        level TEXT NOT NULL,
        semester TEXT NOT NULL
    )
''')

cbt_courses = []  # Fara da list ɗin a nan

# COMPUTER SCIENCE
cbt_courses += [
    # 100L First Semester
    ('CSC101', 'Intro to Computer Science', 'Computer Science', '100L', 'First'),
    ('CSC102', 'Digital Logic Design', 'Computer Science', '100L', 'First'),
    ('CSC103', 'Computer Fundamentals', 'Computer Science', '100L', 'First'),
    ('CSC104', 'Computer Applications', 'Computer Science', '100L', 'First'),
    ('CSC105', 'Intro to Programming', 'Computer Science', '100L', 'First'),
    ('CSC106', 'Discrete Mathematics', 'Computer Science', '100L', 'First'),
    ('CSC107', 'Computer Ethics', 'Computer Science', '100L', 'First'),

    # 100L Second Semester
    ('CSC108', 'Programming in C', 'Computer Science', '100L', 'Second'),
    ('CSC109', 'Computer Hardware', 'Computer Science', '100L', 'Second'),
    ('CSC110', 'Systems Software', 'Computer Science', '100L', 'Second'),
    ('CSC111', 'Basic Networking', 'Computer Science', '100L', 'Second'),
    ('CSC112', 'Computer Security Basics', 'Computer Science', '100L', 'Second'),
    ('CSC113', 'Web Design Fundamentals', 'Computer Science', '100L', 'Second'),
    ('CSC114', 'Human Computer Interaction', 'Computer Science', '100L', 'Second'),

    # 200L First Semester
    ('CSC201', 'Data Structures and Algorithms I', 'Computer Science', '200L', 'First'),
    ('CSC202', 'Object Oriented Programming', 'Computer Science', '200L', 'First'),
    ('CSC203', 'Computer Architecture', 'Computer Science', '200L', 'First'),
    ('CSC204', 'Operating Systems I', 'Computer Science', '200L', 'First'),
    ('CSC205', 'Numerical Methods', 'Computer Science', '200L', 'First'),
    ('CSC206', 'Database Management Systems', 'Computer Science', '200L', 'First'),
    ('CSC207', 'Computer Logic & Organization', 'Computer Science', '200L', 'First'),

    # 200L Second Semester
    ('CSC208', 'Data Structures and Algorithms II', 'Computer Science', '200L', 'Second'),
    ('CSC209', 'Software Engineering', 'Computer Science', '200L', 'Second'),
    ('CSC210', 'Web Application Development', 'Computer Science', '200L', 'Second'),
    ('CSC211', 'Computer Networks', 'Computer Science', '200L', 'Second'),
    ('CSC212', 'Theory of Computation', 'Computer Science', '200L', 'Second'),
    ('CSC213', 'Formal Languages and Automata', 'Computer Science', '200L', 'Second'),
    ('CSC214', 'Entrepreneurship in Tech', 'Computer Science', '200L', 'Second'),

    ('CSC301', 'Compiler Construction I', 'Computer Science', '300L', 'First'),
    ('CSC302', 'Advanced Database Systems', 'Computer Science', '300L', 'First'),
    ('CSC303', 'Artificial Intelligence', 'Computer Science', '300L', 'First'),
    ('CSC304', 'Advanced Computer Architecture', 'Computer Science', '300L', 'First'),
    ('CSC305', 'Software Project Management', 'Computer Science', '300L', 'First'),
    ('CSC306', 'Mobile App Development', 'Computer Science', '300L', 'First'),
    ('CSC307', 'Research Methodology', 'Computer Science', '300L', 'First'),        

('CSC308', 'Compiler Construction II', 'Computer Science', '300L', 'Second'),
    ('CSC309', 'Machine Learning', 'Computer Science', '300L', 'Second'),
    ('CSC310', 'Human Computer Interaction', 'Computer Science', '300L', 'Second'),
    ('CSC311', 'Distributed Systems', 'Computer Science', '300L', 'Second'),
    ('CSC312', 'Cloud Computing', 'Computer Science', '300L', 'Second'),
    ('CSC313', 'Professional Ethics in IT', 'Computer Science', '300L', 'Second'),
    ('CSC314', 'Computer Graphics', 'Computer Science', '300L', 'Second'),

    ('CSC401', 'Project Work I', 'Computer Science', '400L', 'First'),
    ('CSC402', 'Cybersecurity Principles', 'Computer Science', '400L', 'First'),
    ('CSC403', 'Data Mining & Knowledge Discovery', 'Computer Science', '400L', 'First'),
    ('CSC404', 'Software Quality Assurance', 'Computer Science', '400L', 'First'),
    ('CSC405', 'Advanced Operating Systems', 'Computer Science', '400L', 'First'),
    ('CSC406', 'Big Data Analytics', 'Computer Science', '400L', 'First'),
    ('CSC407', 'Research Seminar', 'Computer Science', '400L', 'First'),
                        
('CSC408', 'Project Work II', 'Computer Science', '400L', 'Second'),
    ('CSC409', 'Information Retrieval Systems', 'Computer Science', '400L', 'Second'),
    ('CSC410', 'Natural Language Processing', 'Computer Science', '400L', 'Second'),
    ('CSC411', 'Internet of Things (IoT)', 'Computer Science', '400L', 'Second'),
    ('CSC412', 'Advanced Machine Learning', 'Computer Science', '400L', 'Second'),
    ('CSC413', 'Blockchain Technologies', 'Computer Science', '400L', 'Second'),
    ('CSC414', 'IT Entrepreneurship', 'Computer Science', '400L', 'Second'),

    ('MTH101', 'Calculus I', 'Mathematics', '100L', 'First'),
    ('MTH102', 'Algebra I', 'Mathematics', '100L', 'First'),
    ('MTH103', 'Trigonometry', 'Mathematics', '100L', 'First'),
    ('MTH104', 'Elementary Set Theory', 'Mathematics', '100L', 'First'),
    ('MTH105', 'Mathematical Methods I', 'Mathematics', '100L', 'First'),
    ('MTH106', 'Computer Appreciation', 'Mathematics', '100L', 'First'),
    ('GST101', 'Use of English', 'Mathematics', '100L', 'First'),

('MTH107', 'Calculus II', 'Mathematics', '100L', 'Second'),
    ('MTH108', 'Algebra II', 'Mathematics', '100L', 'Second'),
    ('MTH109', 'Vectors and Geometry', 'Mathematics', '100L', 'Second'),
    ('MTH110', 'Intro. to Programming', 'Mathematics', '100L', 'Second'),
    ('MTH111', 'Probability I', 'Mathematics', '100L', 'Second'),
    ('MTH112', 'Mathematical Logic', 'Mathematics', '100L', 'Second'),
    ('GST102', 'Communication in English', 'Mathematics', '100L', 'Second'),

    ('MTH201', 'Linear Algebra I', 'Mathematics', '200L', 'First'),
    ('MTH202', 'Real Analysis I', 'Mathematics', '200L', 'First'),
    ('MTH203', 'Differential Equations I', 'Mathematics', '200L', 'First'),
    ('MTH204', 'Numerical Methods', 'Mathematics', '200L', 'First'),
    ('MTH205', 'Abstract Algebra I', 'Mathematics', '200L', 'First'),
    ('STA201', 'Statistics for Scientists', 'Mathematics', '200L', 'First'),
    ('GST201', 'Entrepreneurship I', 'Mathematics', '200L', 'First'),

('MTH206', 'Linear Algebra II', 'Mathematics', '200L', 'Second'),
    ('MTH207', 'Real Analysis II', 'Mathematics', '200L', 'Second'),
    ('MTH208', 'Differential Equations II', 'Mathematics', '200L', 'Second'),
    ('MTH209', 'Abstract Algebra II', 'Mathematics', '200L', 'Second'),
    ('MTH210', 'Complex Analysis', 'Mathematics', '200L', 'Second'),
    ('MTH211', 'Mathematical Modelling', 'Mathematics', '200L', 'Second'),
    ('GST202', 'Entrepreneurship II', 'Mathematics', '200L', 'Second'),

    ('MTH301', 'Measure Theory', 'Mathematics', '300L', 'First'),
    ('MTH302', 'Linear Programming', 'Mathematics', '300L', 'First'),
    ('MTH303', 'Topology I', 'Mathematics', '300L', 'First'),
    ('MTH304', 'Complex Analysis I', 'Mathematics', '300L', 'First'),
    ('MTH305', 'Real Analysis III', 'Mathematics', '300L', 'First'),
    ('MTH306', 'Abstract Algebra III', 'Mathematics', '300L', 'First'),
    ('GST301', 'Research Methodology', 'Mathematics', '300L', 'First'),

    ('MTH307', 'Numerical Analysis I', 'Mathematics', '300L', 'Second'),
    ('MTH308', 'Functional Analysis I', 'Mathematics', '300L', 'Second'),
    ('MTH309', 'Mathematical Modelling II', 'Mathematics', '300L', 'Second'),
    ('MTH310', 'Topology II', 'Mathematics', '300L', 'Second'),
    ('MTH311', 'Complex Analysis II', 'Mathematics', '300L', 'Second'),
    ('MTH312', 'Advanced Linear Algebra', 'Mathematics', '300L', 'Second'),
    ('GST302', 'Peace and Conflict Resolution', 'Mathematics', '300L', 'Second'),

    ('MTH401', 'Project/Thesis I', 'Mathematics', '400L', 'First'),
    ('MTH402', 'Advanced Calculus I', 'Mathematics', '400L', 'First'),
    ('MTH403', 'Differential Geometry', 'Mathematics', '400L', 'First'),
    ('MTH404', 'Advanced Abstract Algebra', 'Mathematics', '400L', 'First'),
    ('MTH405', 'Mathematical Statistics I', 'Mathematics', '400L', 'First'),
    ('MTH406', 'Integral Equations', 'Mathematics', '400L', 'First'),
    ('GST401', 'Entrepreneurship III', 'Mathematics', '400L', 'First'),

    ('MTH407', 'Project/Thesis II', 'Mathematics', '400L', 'Second'),
    ('MTH408', 'Advanced Calculus II', 'Mathematics', '400L', 'Second'),
    ('MTH409', 'Functional Analysis II', 'Mathematics', '400L', 'Second'),
    ('MTH410', 'Advanced Topology', 'Mathematics', '400L', 'Second'),
    ('MTH411', 'Mathematical Statistics II', 'Mathematics', '400L', 'Second'),
    ('MTH412', 'Research Seminar', 'Mathematics', '400L', 'Second'),
    ('GST402', 'Peace and Conflict II', 'Mathematics', '400L', 'Second'),

    ('PHY101', 'General Physics I', 'Physics', '100L', 'First'),
    ('PHY102', 'Mechanics', 'Physics', '100L', 'First'),
    ('MTH101', 'Calculus I', 'Physics', '100L', 'First'),
    ('CHM101', 'General Chemistry I', 'Physics', '100L', 'First'),
    ('GST101', 'Use of English', 'Physics', '100L', 'First'),
    ('PHY103', 'Practical Physics I', 'Physics', '100L', 'First'),
    ('BIO101', 'General Biology I', 'Physics', '100L', 'First'),

    ('PHY104', 'General Physics II', 'Physics', '100L', 'Second'),
    ('PHY105', 'Heat & Properties of Matter', 'Physics', '100L', 'Second'),
    ('MTH102', 'Calculus II', 'Physics', '100L', 'Second'),
    ('CHM102', 'General Chemistry II', 'Physics', '100L', 'Second'),
    ('GST102', 'Communication in English', 'Physics', '100L', 'Second'),
    ('PHY106', 'Practical Physics II', 'Physics', '100L', 'Second'),
    ('CSP101', 'Intro to Computer Science', 'Physics', '100L', 'Second'),

    ('PHY201', 'Electricity and Magnetism I', 'Physics', '200L', 'First'),
    ('PHY202', 'Thermodynamics', 'Physics', '200L', 'First'),
    ('PHY203', 'Mathematical Methods I', 'Physics', '200L', 'First'),
    ('PHY204', 'Modern Physics I', 'Physics', '200L', 'First'),
    ('MTH201', 'Linear Algebra', 'Physics', '200L', 'First'),
    ('PHY205', 'Practical Physics III', 'Physics', '200L', 'First'),
    ('GST201', 'Nigerian Peoples & Culture', 'Physics', '200L', 'First'),

    ('PHY206', 'Electricity and Magnetism II', 'Physics', '200L', 'Second'),
    ('PHY207', 'Waves and Optics', 'Physics', '200L', 'Second'),
    ('PHY208', 'Mathematical Methods II', 'Physics', '200L', 'Second'),
    ('PHY209', 'Modern Physics II', 'Physics', '200L', 'Second'),
    ('PHY210', 'Practical Physics IV', 'Physics', '200L', 'Second'),
    ('STA201', 'Probability Theory', 'Physics', '200L', 'Second'),
    ('GST202', 'Peace Studies & Conflict Resolution', 'Physics', '200L', 'Second'),

    ('PHY301', 'Quantum Mechanics I', 'Physics', '300L', 'First'),
    ('PHY302', 'Classical Mechanics I', 'Physics', '300L', 'First'),
    ('PHY303', 'Electromagnetic Theory I', 'Physics', '300L', 'First'),
    ('PHY304', 'Solid State Physics I', 'Physics', '300L', 'First'),
    ('PHY305', 'Computational Physics I', 'Physics', '300L', 'First'),
    ('PHY306', 'Laboratory Physics V', 'Physics', '300L', 'First'),
    ('GST301', 'Research Methodology', 'Physics', '300L', 'First'),

    ('PHY307', 'Quantum Mechanics II', 'Physics', '300L', 'Second'),
    ('PHY308', 'Classical Mechanics II', 'Physics', '300L', 'Second'),
    ('PHY309', 'Electromagnetic Theory II', 'Physics', '300L', 'Second'),
    ('PHY310', 'Solid State Physics II', 'Physics', '300L', 'Second'),
    ('PHY311', 'Statistical Physics', 'Physics', '300L', 'Second'),
    ('PHY312', 'Laboratory Physics VI', 'Physics', '300L', 'Second'),
    ('GST302', 'Entrepreneurship II', 'Physics', '300L', 'Second'),

    ('PHY401', 'Nuclear Physics I', 'Physics', '400L', 'First'),
    ('PHY402', 'Advanced Quantum Mechanics', 'Physics', '400L', 'First'),
    ('PHY403', 'Atomic & Molecular Physics', 'Physics', '400L', 'First'),
    ('PHY404', 'Environmental Physics', 'Physics', '400L', 'First'),
    ('PHY405', 'Seminar I', 'Physics', '400L', 'First'),
    ('PHY406', 'Electronics I', 'Physics', '400L', 'First'),
    ('GST401', 'Entrepreneurship III', 'Physics', '400L', 'First'),

    ('PHY407', 'Nuclear Physics II', 'Physics', '400L', 'Second'),
    ('PHY408', 'Space & Radiation Physics', 'Physics', '400L', 'Second'),
    ('PHY409', 'Material Science', 'Physics', '400L', 'Second'),
    ('PHY410', 'Advanced Lab Project', 'Physics', '400L', 'Second'),
    ('PHY411', 'Seminar II', 'Physics', '400L', 'Second'),
    ('PHY412', 'Electronics II', 'Physics', '400L', 'Second'),
    ('GST402', 'Peace and Conflict II', 'Physics', '400L', 'Second'),

    ('BIO101', 'General Biology I', 'Biology', '100L', 'First'),
    ('CHM101', 'General Chemistry I', 'Biology', '100L', 'First'),
    ('PHY101', 'General Physics I', 'Biology', '100L', 'First'),
    ('GST101', 'Use of English I', 'Biology', '100L', 'First'),
    ('MTH101', 'Mathematics for Biology I', 'Biology', '100L', 'First'),
    ('BIO102', 'Botany I', 'Biology', '100L', 'First'),
    ('BIO103', 'Biology Practical I', 'Biology', '100L', 'First'),

    ('BIO104', 'General Biology II', 'Biology', '100L', 'Second'),
    ('CHM102', 'General Chemistry II', 'Biology', '100L', 'Second'),
    ('PHY102', 'General Physics II', 'Biology', '100L', 'Second'),
    ('GST102', 'Communication in English', 'Biology', '100L', 'Second'),
    ('MTH102', 'Mathematics for Biology II', 'Biology', '100L', 'Second'),
    ('BIO105', 'Zoology I', 'Biology', '100L', 'Second'),
    ('BIO106', 'Biology Practical II', 'Biology', '100L', 'Second'),

    ('BIO201', 'Cell Biology', 'Biology', '200L', 'First'),
    ('BIO202', 'Ecology I', 'Biology', '200L', 'First'),
    ('CHM201', 'Organic Chemistry', 'Biology', '200L', 'First'),
    ('BIO203', 'Microbiology I', 'Biology', '200L', 'First'),
    ('GST201', 'Nigerian Peoples and Culture', 'Biology', '200L', 'First'),
    ('BIO204', 'Biological Techniques', 'Biology', '200L', 'First'),
    ('BIO205', 'Practical Biology III', 'Biology', '200L', 'First'),

    ('BIO206', 'Genetics I', 'Biology', '200L', 'Second'),
    ('BIO207', 'Ecology II', 'Biology', '200L', 'Second'),
    ('BIO208', 'Microbiology II', 'Biology', '200L', 'Second'),
    ('CHM202', 'Biochemistry I', 'Biology', '200L', 'Second'),
    ('GST202', 'Peace Studies & Conflict Resolution', 'Biology', '200L', 'Second'),
    ('BIO209', 'Developmental Biology', 'Biology', '200L', 'Second'),
    ('BIO210', 'Practical Biology IV', 'Biology', '200L', 'Second'),

    ('BIO301', 'Genetics II', 'Biology', '300L', 'First'),
    ('BIO302', 'Plant Physiology', 'Biology', '300L', 'First'),
    ('BIO303', 'Animal Physiology', 'Biology', '300L', 'First'),
    ('BIO304', 'Biochemistry II', 'Biology', '300L', 'First'),
    ('BIO305', 'Immunology', 'Biology', '300L', 'First'),
    ('BIO306', 'Research Methods in Biology', 'Biology', '300L', 'First'),
    ('BIO307', 'Biology Practical V', 'Biology', '300L', 'First'),

    ('BIO308', 'Evolution', 'Biology', '300L', 'Second'),
    ('BIO309', 'Entomology', 'Biology', '300L', 'Second'),
    ('BIO310', 'Environmental Biology', 'Biology', '300L', 'Second'),
    ('BIO311', 'Cell & Molecular Biology', 'Biology', '300L', 'Second'),
    ('BIO312', 'Parasitology', 'Biology', '300L', 'Second'),
    ('GST301', 'Entrepreneurship I', 'Biology', '300L', 'Second'),
    ('BIO313', 'Biology Practical VI', 'Biology', '300L', 'Second'),

    ('BIO401', 'Advanced Ecology', 'Biology', '400L', 'First'),
    ('BIO402', 'Biostatistics', 'Biology', '400L', 'First'),
    ('BIO403', 'Advanced Genetics', 'Biology', '400L', 'First'),
    ('BIO404', 'Project I', 'Biology', '400L', 'First'),
    ('BIO405', 'Seminar I', 'Biology', '400L', 'First'),
    ('BIO406', 'Plant Pathology', 'Biology', '400L', 'First'),
    ('GST401', 'Entrepreneurship II', 'Biology', '400L', 'First'),

    ('BIO407', 'Advanced Cell Biology', 'Biology', '400L', 'Second'),
    ('BIO408', 'Industrial Microbiology', 'Biology', '400L', 'Second'),
    ('BIO409', 'Project II', 'Biology', '400L', 'Second'),
    ('BIO410', 'Seminar II', 'Biology', '400L', 'Second'),
    ('BIO411', 'Toxicology', 'Biology', '400L', 'Second'),
    ('BIO412', 'Environmental Toxicology', 'Biology', '400L', 'Second'),
    ('GST402', 'Peace and Conflict II', 'Biology', '400L', 'Second'),

    ('BCH101', 'Introduction to Biochemistry', 'Biochemistry', '100L', 'First'),
    ('CHM101', 'General Chemistry I', 'Biochemistry', '100L', 'First'),
    ('BIO101', 'General Biology I', 'Biochemistry', '100L', 'First'),
    ('GST101', 'Use of English I', 'Biochemistry', '100L', 'First'),
    ('MTH101', 'Basic Mathematics', 'Biochemistry', '100L', 'First'),
    ('PHY101', 'General Physics I', 'Biochemistry', '100L', 'First'),
    ('BCH102', 'Biochemistry Practical I', 'Biochemistry', '100L', 'First'),

    ('BCH103', 'Organic Chemistry', 'Biochemistry', '100L', 'Second'),
    ('CHM102', 'General Chemistry II', 'Biochemistry', '100L', 'Second'),
    ('BIO102', 'General Biology II', 'Biochemistry', '100L', 'Second'),
    ('GST102', 'Communication Skills', 'Biochemistry', '100L', 'Second'),
    ('MTH102', 'Mathematics II', 'Biochemistry', '100L', 'Second'),
    ('PHY102', 'General Physics II', 'Biochemistry', '100L', 'Second'),
    ('BCH104', 'Biochemistry Practical II', 'Biochemistry', '100L', 'Second'),

    ('BCH201', 'Physical Chemistry I', 'Biochemistry', '200L', 'First'),
    ('BCH202', 'Cell Biology', 'Biochemistry', '200L', 'First'),
    ('CHM201', 'Analytical Chemistry', 'Biochemistry', '200L', 'First'),
    ('GST201', 'Nigerian Peoples and Culture', 'Biochemistry', '200L', 'First'),
    ('BCH203', 'Enzymology', 'Biochemistry', '200L', 'First'),
    ('BCH204', 'Biochemistry Practical III', 'Biochemistry', '200L', 'First'),
    ('BIO201', 'Microbiology', 'Biochemistry', '200L', 'First'),

    ('BCH205', 'Organic Chemistry II', 'Biochemistry', '200L', 'Second'),
    ('BCH206', 'Molecular Biology', 'Biochemistry', '200L', 'Second'),
    ('BCH207', 'Metabolism I', 'Biochemistry', '200L', 'Second'),
    ('GST202', 'Peace Studies and Conflict Resolution', 'Biochemistry', '200L', 'Second'),
    ('BCH208', 'Biochemistry Practical IV', 'Biochemistry', '200L', 'Second'),
    ('CHM202', 'Physical Chemistry II', 'Biochemistry', '200L', 'Second'),
    ('BIO202', 'Genetics', 'Biochemistry', '200L', 'Second'),

    ('BCH301', 'Advanced Enzymology', 'Biochemistry', '300L', 'First'),
    ('BCH302', 'Immunology', 'Biochemistry', '300L', 'First'),
    ('BCH303', 'Metabolism II', 'Biochemistry', '300L', 'First'),
    ('BCH304', 'Protein Chemistry', 'Biochemistry', '300L', 'First'),
    ('BCH305', 'Biochemistry Practical V', 'Biochemistry', '300L', 'First'),
    ('GST301', 'Entrepreneurship I', 'Biochemistry', '300L', 'First'),
    ('BIO301', 'Cell Signaling', 'Biochemistry', '300L', 'First'),

    ('BCH306', 'Nucleic Acids', 'Biochemistry', '300L', 'Second'),
    ('BCH307', 'Molecular Genetics', 'Biochemistry', '300L', 'Second'),
    ('BCH308', 'Biotechnology', 'Biochemistry', '300L', 'Second'),
    ('BCH309', 'Biochemical Toxicology', 'Biochemistry', '300L', 'Second'),
    ('GST302', 'Entrepreneurship II', 'Biochemistry', '300L', 'Second'),
    ('BCH310', 'Biochemistry Practical VI', 'Biochemistry', '300L', 'Second'),
    ('BIO302', 'Advanced Microbiology', 'Biochemistry', '300L', 'Second'),

    ('BCH401', 'Advanced Metabolism', 'Biochemistry', '400L', 'First'),
    ('BCH402', 'Clinical Biochemistry', 'Biochemistry', '400L', 'First'),
    ('BCH403', 'Research Project I', 'Biochemistry', '400L', 'First'),
    ('BCH404', 'Seminar I', 'Biochemistry', '400L', 'First'),
    ('BCH405', 'Molecular Biology Techniques', 'Biochemistry', '400L', 'First'),
    ('GST401', 'Entrepreneurship III', 'Biochemistry', '400L', 'First'),
    ('BCH406', 'Biochemistry Practical VII', 'Biochemistry', '400L', 'First'),

    ('BCH407', 'Advanced Clinical Biochemistry', 'Biochemistry', '400L', 'Second'),
    ('BCH408', 'Research Project II', 'Biochemistry', '400L', 'Second'),
    ('BCH409', 'Seminar II', 'Biochemistry', '400L', 'Second'),
    ('BCH410', 'Molecular Pharmacology', 'Biochemistry', '400L', 'Second'),
    ('BCH411', 'Toxicology', 'Biochemistry', '400L', 'Second'),
    ('GST402', 'Peace and Conflict Studies II', 'Biochemistry', '400L', 'Second'),
    ('BCH412', 'Biochemistry Practical VIII', 'Biochemistry', '400L', 'Second'),
]

# Insert all courses (overwrite if needed)
cursor.executemany('''
    INSERT INTO cbt_courses (
        course_code, course_title, department, level, semester
    ) VALUES (?, ?, ?, ?, ?)
''', cbt_courses)

# Tabbatar da cewa teburi ya wanzu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cbt_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT NOT NULL,
        question_text TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        image_path TEXT
    )
''')

# Jerin course codes bisa jere
course_codes = ['BIO101', 'CSC101', 'CHM101', 'GST101', 'MTH101', 'STA101', 'PHY101', 'MATH201']

# Jerin tambayoyi
questions = []

course_code = 'CSC101'

# Tambaya 1
question_text = 'What is the function of an operating system?'
option_a = 'Manages software only'
option_b = 'Manages hardware only'
option_c = 'Manages both hardware and software'
option_d = 'Only displays output'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'Which language is considered the foundation of computer science?'
option_a = 'Python'
option_b = 'C'
option_c = 'Assembly'
option_d = 'Pascal'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'What does CPU stand for?'
option_a = 'Central Process Unit'
option_b = 'Central Processing Unit'
option_c = 'Computer Processing Unit'
option_d = 'Central Programming Unit'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'What is the binary value of decimal 5?'
option_a = '1010'
option_b = '0010'
option_c = '101'
option_d = '111'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'Which of these is an input device?'
option_a = 'Monitor'
option_b = 'Printer'
option_c = 'Mouse'
option_d = 'Speaker'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'What is RAM used for?'
option_a = 'Storing programs permanently'
option_b = 'Executing applications'
option_c = 'Temporary data storage'
option_d = 'Backing up files'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'What is software?'
option_a = 'Physical parts of a computer'
option_b = 'Set of instructions for a computer'
option_c = 'Electric current in the computer'
option_d = 'All computer accessories'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'Which of these is a programming language?'
option_a = 'HTML'
option_b = 'HTTP'
option_c = 'SQL'
option_d = 'Python'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'Which generation of computers used microprocessors?'
option_a = 'First'
option_b = 'Second'
option_c = 'Third'
option_d = 'Fourth'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'What does GUI stand for?'
option_a = 'Graphical User Interface'
option_b = 'General User Information'
option_c = 'Global Unit Interface'
option_d = 'Graphical Use Input'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'Which of these is a storage device?'
option_a = 'Scanner'
option_b = 'Hard disk'
option_c = 'Monitor'
option_d = 'Keyboard'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'Which number system do computers use?'
option_a = 'Decimal'
option_b = 'Octal'
option_c = 'Binary'
option_d = 'Hexadecimal'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What does ALU stand for?'
option_a = 'Arithmetic Logic Unit'
option_b = 'Advanced Logic Unit'
option_c = 'Application Logic Unit'
option_d = 'Arithmetic Local Unit'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'Which is NOT a type of computer software?'
option_a = 'System software'
option_b = 'Application software'
option_c = 'Utility software'
option_d = 'Digital software'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'Which of these is a system software?'
option_a = 'MS Word'
option_b = 'Google Chrome'
option_c = 'Windows OS'
option_d = 'Adobe Reader'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'Which of these is an example of application software?'
option_a = 'BIOS'
option_b = 'Linux Kernel'
option_c = 'MS Excel'
option_d = 'Device Driver'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'A kilobyte (KB) equals how many bytes?'
option_a = '100'
option_b = '512'
option_c = '1024'
option_d = '2048'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'Which company developed the Windows operating system?'
option_a = 'Apple'
option_b = 'Microsoft'
option_c = 'IBM'
option_d = 'Google'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'Which one is NOT an input device?'
option_a = 'Joystick'
option_b = 'Keyboard'
option_c = 'Monitor'
option_d = 'Scanner'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'Which of these languages is used in AI programming?'
option_a = 'C++'
option_b = 'FORTRAN'
option_c = 'Python'
option_d = 'Pascal'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'Which device is used to carry data from one computer to another?'
option_a = 'CD-ROM'
option_b = 'USB Flash Drive'
option_c = 'Monitor'
option_d = 'Printer'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'Which of the following is a search engine?'
option_a = 'Google'
option_b = 'Facebook'
option_c = 'Twitter'
option_d = 'Gmail'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'What does HTTP stand for?'
option_a = 'HyperText Transfer Protocol'
option_b = 'HighText Transfer Protocol'
option_c = 'Hyper Transfer Text Protocol'
option_d = 'HyperType Text Processing'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'What does URL stand for?'
option_a = 'Uniform Resource Locator'
option_b = 'Uniform Request Link'
option_c = 'Universal Resource Link'
option_d = 'Unified Resource Locator'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'Which of the following is NOT an output device?'
option_a = 'Printer'
option_b = 'Monitor'
option_c = 'Speaker'
option_d = 'Scanner'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'Which of the following is an example of a web browser?'
option_a = 'Chrome'
option_b = 'Google'
option_c = 'Bing'
option_d = 'Yahoo'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What does ICT stand for?'
option_a = 'Information Computer Technology'
option_b = 'Information Communication Technology'
option_c = 'Integrated Communication Technology'
option_d = 'Internet and Communication Technology'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'Which of these is NOT a type of computer virus?'
option_a = 'Trojan Horse'
option_b = 'Worm'
option_c = 'Spyware'
option_d = 'Firewall'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'Which of these is used to protect a computer from virus?'
option_a = 'Firewall'
option_b = 'Anti-virus software'
option_c = 'Spam filter'
option_d = 'Scanner'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'What is phishing?'
option_a = 'Collecting fish from river'
option_b = 'Fraudulent attempt to obtain sensitive data'
option_c = 'Sending junk mail'
option_d = 'Downloading from the internet'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'Which of these is a programming concept?'
option_a = 'Loop'
option_b = 'Google'
option_c = 'Yahoo'
option_d = 'Windows'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'Which of these is an email service?'
option_a = 'Gmail'
option_b = 'Chrome'
option_c = 'Photoshop'
option_d = 'Excel'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'Which of these is used to connect computers together?'
option_a = 'Router'
option_b = 'Monitor'
option_c = 'Keyboard'
option_d = 'Speaker'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'Which software is used for typing documents?'
option_a = 'MS Word'
option_b = 'MS Excel'
option_c = 'MS PowerPoint'
option_d = 'MS Access'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'Which shortcut is used to copy?'
option_a = 'Ctrl + V'
option_b = 'Ctrl + X'
option_c = 'Ctrl + C'
option_d = 'Ctrl + P'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'What is the full meaning of USB?'
option_a = 'Universal Serial Bus'
option_b = 'Uniform Serial Bus'
option_c = 'United System Board'
option_d = 'Universal Software Box'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'Which of these is NOT an operating system?'
option_a = 'Linux'
option_b = 'Windows'
option_c = 'DOS'
option_d = 'Google'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'Which key is used to delete characters to the left?'
option_a = 'Delete'
option_b = 'Backspace'
option_c = 'Enter'
option_d = 'Shift'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'What is the full meaning of PDF?'
option_a = 'Portable Document Format'
option_b = 'Printed Document File'
option_c = 'Photo Data Format'
option_d = 'Programmed Data File'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'Which of these is NOT a computer hardware?'
option_a = 'CPU'
option_b = 'RAM'
option_c = 'Operating System'
option_d = 'Motherboard'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'MTH101'

# Tambaya 1
question_text = 'What is the derivative of x²?'
option_a = '2x'
option_b = 'x'
option_c = 'x²'
option_d = '2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'What is the integral of 1/x?'
option_a = 'x'
option_b = 'ln|x|'
option_c = '1/x²'
option_d = 'xlnx'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'What is the limit of (x² - 1)/(x - 1) as x approaches 1?'
option_a = '0'
option_b = '2'
option_c = '1'
option_d = 'Undefined'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'What is the value of sin(90°)?'
option_a = '0'
option_b = '1'
option_c = '0.5'
option_d = 'Undefined'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'What is the square root of 144?'
option_a = '11'
option_b = '14'
option_c = '12'
option_d = '13'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'What is the solution to the equation x² - 4 = 0?'
option_a = '2'
option_b = '-2'
option_c = '±2'
option_d = '0'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'What is the value of cos(0)?'
option_a = '0'
option_b = '1'
option_c = '-1'
option_d = 'Undefined'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'What is the factorial of 5 (5!)?'
option_a = '120'
option_b = '25'
option_c = '60'
option_d = '100'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'Which of the following is a prime number?'
option_a = '9'
option_b = '15'
option_c = '17'
option_d = '21'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'What is the area of a circle with radius 7?'
option_a = '49π'
option_b = '14π'
option_c = '21π'
option_d = '28π'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'What is the slope of the line y = 3x + 5?'
option_a = '5'
option_b = '3'
option_c = '-3'
option_d = '0'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'What is the solution of 2x + 3 = 7?'
option_a = 'x = 1'
option_b = 'x = 2'
option_c = 'x = 3'
option_d = 'x = 4'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What is log₁₀(1000)?'
option_a = '3'
option_b = '2'
option_c = '4'
option_d = '1'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'What is the derivative of sin(x)?'
option_a = 'cos(x)'
option_b = '-sin(x)'
option_c = '-cos(x)'
option_d = 'sec(x)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'What is the volume of a cube of side 3?'
option_a = '6'
option_b = '9'
option_c = '27'
option_d = '18'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What is the quadratic formula?'
option_a = '(-b ± √(b²-4ac)) / 2a'
option_b = '(b ± √(b²+4ac)) / 2a'
option_c = '(a ± √(b²-4ac)) / 2b'
option_d = '(-a ± √(b²-4ac)) / 2b'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'What is the angle sum of a triangle?'
option_a = '180°'
option_b = '90°'
option_c = '360°'
option_d = '270°'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'If f(x) = x + 3, what is f(2)?'
option_a = '5'
option_b = '2'
option_c = '1'
option_d = '6'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'Which of these is a linear equation?'
option_a = 'y = 2x + 3'
option_b = 'y = x² + 1'
option_c = 'y = √x'
option_d = 'y = x³'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'What is the standard form of a quadratic equation?'
option_a = 'ax² + bx + c = 0'
option_b = 'ax + b = 0'
option_c = 'a + b + c = 0'
option_d = 'ax³ + bx² + cx = 0'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'What is the domain of the function f(x) = 1/x?'
option_a = 'x ≠ 0'
option_b = 'x = 0'
option_c = 'All real numbers'
option_d = 'x > 0'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the value of π (pi) approximately?'
option_a = '3.14'
option_b = '2.71'
option_c = '1.41'
option_d = '1.73'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'What is the solution of the inequality x + 3 > 5?'
option_a = 'x > 2'
option_b = 'x < 2'
option_c = 'x = 2'
option_d = 'x = 8'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'Which of the following is an irrational number?'
option_a = '√2'
option_b = '0.25'
option_c = '4'
option_d = '3/5'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'What is the midpoint of (2,4) and (6,8)?'
option_a = '(4,6)'
option_b = '(2,6)'
option_c = '(3,4)'
option_d = '(6,4)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'What is 2⁵?'
option_a = '32'
option_b = '25'
option_c = '16'
option_d = '64'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What is the logarithm of 100 to base 10?'
option_a = '2'
option_b = '10'
option_c = '1'
option_d = '100'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'What is the distance between (0,0) and (3,4)?'
option_a = '5'
option_b = '6'
option_c = '7'
option_d = '4'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'What is the area of a triangle with base 6 and height 4?'
option_a = '12'
option_b = '24'
option_c = '10'
option_d = '8'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'What is the derivative of cos(x)?'
option_a = '-sin(x)'
option_b = 'cos(x)'
option_c = 'sin(x)'
option_d = '-cos(x)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'Which of these is the identity element for addition?'
option_a = '0'
option_b = '1'
option_c = '-1'
option_d = '10'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'If A = {1,2,3} and B = {3,4,5}, what is A ∩ B?'
option_a = '{3}'
option_b = '{1,2}'
option_c = '{1,2,3,4,5}'
option_d = '{}'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'What is the greatest common divisor of 18 and 24?'
option_a = '6'
option_b = '3'
option_c = '12'
option_d = '24'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'If x = 3, what is the value of 2x² - 5x + 1?'
option_a = '4'
option_b = '10'
option_c = '13'
option_d = '6'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'What is the inverse of the function f(x) = x + 4?'
option_a = 'f⁻¹(x) = x - 4'
option_b = 'f⁻¹(x) = x + 4'
option_c = 'f⁻¹(x) = -x + 4'
option_d = 'f⁻¹(x) = 4 - x'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'Which of these is not a function?'
option_a = 'A relation with two outputs for one input'
option_b = 'y = 2x'
option_c = 'y = x²'
option_d = 'y = x + 3'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'Which of the following is a quadratic expression?'
option_a = 'x² + 2x + 1'
option_b = 'x + 2'
option_c = 'x³ + 3'
option_d = 'x⁴ + 1'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'How many degrees are in a straight angle?'
option_a = '180°'
option_b = '90°'
option_c = '360°'
option_d = '45°'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'If sin(x) = 0.5, what is x in degrees (0° < x < 90°)?'
option_a = '30°'
option_b = '60°'
option_c = '45°'
option_d = '90°'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'What is the standard deviation a measure of?'
option_a = 'Spread of data'
option_b = 'Mean value'
option_c = 'Total data'
option_d = 'Difference of numbers'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'PHY101'

# Tambaya 1
question_text = 'What is the formula for calculating velocity?'
option_a = 'v = s/t'
option_b = 'v = t/s'
option_c = 'v = 2s/t'
option_d = 'v = s*t'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'What is the unit of force?'
option_a = 'Newton'
option_b = 'Joule'
option_c = 'Pascal'
option_d = 'Watt'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'What is the gravitational acceleration on Earth?'
option_a = '9.8 m/s^2'
option_b = '10 m/s^2'
option_c = '9.81 m/s^2'
option_d = '10.5 m/s^2'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'What is the formula for work done?'
option_a = 'W = F * d'
option_b = 'W = F / d'
option_c = 'W = F + d'
option_d = 'W = F - d'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'What is the unit of energy?'
option_a = 'Joule'
option_b = 'Newton'
option_c = 'Watt'
option_d = 'Volt'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'What is the unit of power?'
option_a = 'Watt'
option_b = 'Joule'
option_c = 'Newton'
option_d = 'Ampere'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'What is the principle of conservation of energy?'
option_a = 'Energy cannot be created or destroyed'
option_b = 'Energy is always conserved'
option_c = 'Energy can be destroyed but not created'
option_d = 'Energy can be created but not destroyed'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'What is the formula for calculating kinetic energy?'
option_a = 'KE = 1/2 mv^2'
option_b = 'KE = mv^2'
option_c = 'KE = 1/2 m^2v'
option_d = 'KE = mv'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'What is the speed of light in a vacuum?'
option_a = '3 x 10^8 m/s'
option_b = '3 x 10^6 m/s'
option_c = '3 x 10^10 m/s'
option_d = '3 x 10^7 m/s'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'What is the formula for calculating potential energy?'
option_a = 'PE = mgh'
option_b = 'PE = m * v'
option_c = 'PE = v^2 / 2'
option_d = 'PE = F * d'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = "What does Ohm's law state?"
option_a = 'V = IR'
option_b = 'V = I/R'
option_c = 'V = I + R'
option_d = 'V = I * R'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'What is the SI unit of current?'
option_a = 'Ampere'
option_b = 'Volt'
option_c = 'Ohm'
option_d = 'Coulomb'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What is the SI unit of resistance?'
option_a = 'Ohm'
option_b = 'Ampere'
option_c = 'Volt'
option_d = 'Coulomb'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'What is the law of reflection?'
option_a = 'Angle of incidence = Angle of reflection'
option_b = 'Angle of incidence + Angle of reflection = 90 degrees'
option_c = 'Angle of incidence = 90 degrees'
option_d = 'Angle of incidence = 0 degrees'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'What is the frequency of a wave?'
option_a = 'Number of oscillations per second'
option_b = 'Speed of wave'
option_c = 'Wavelength'
option_d = 'Amplitude'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What is the formula for calculating the period of a wave?'
option_a = 'T = 1/f'
option_b = 'T = f / 1'
option_c = 'T = f'
option_d = 'T = f^2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'What is the unit of frequency?'
option_a = 'Hertz'
option_b = 'Watt'
option_c = 'Newton'
option_d = 'Joule'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'What is the speed of sound in air?'
option_a = '343 m/s'
option_b = '300 m/s'
option_c = '340 m/s'
option_d = '400 m/s'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'What is the SI unit of temperature?'
option_a = 'Kelvin'
option_b = 'Celsius'
option_c = 'Fahrenheit'
option_d = 'Rankine'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'What is the formula for calculating force?'
option_a = 'F = ma'
option_b = 'F = mv'
option_c = 'F = m/v'
option_d = 'F = m^2a'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'What is the principle of buoyancy?'
option_a = 'An object immersed in a fluid experiences an upward force'
option_b = 'An object sinks when it displaces more fluid'
option_c = 'An object will float if its weight is more than the fluid displaced'
option_d = 'None of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the energy stored in a spring called?'
option_a = 'Elastic potential energy'
option_b = 'Kinetic energy'
option_c = 'Gravitational potential energy'
option_d = 'Mechanical energy'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'What is the formula for calculating pressure?'
option_a = 'P = F / A'
option_b = 'P = A / F'
option_c = 'P = F * A'
option_d = 'P = A * F'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'What is the unit of pressure?'
option_a = 'Pascal'
option_b = 'Newton'
option_c = 'Joule'
option_d = 'Watt'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'What is the Doppler effect?'
option_a = 'Change in frequency due to motion'
option_b = 'Change in wavelength due to motion'
option_c = 'Change in speed due to motion'
option_d = 'Change in amplitude due to motion'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'What is the formula for the acceleration of an object?'
option_a = 'a = (v - u) / t'
option_b = 'a = v * u * t'
option_c = 'a = v + u / t'
option_d = 'a = u / t'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What is the principle of conservation of momentum?'
option_a = 'Momentum before collision = Momentum after collision'
option_b = 'Momentum before collision > Momentum after collision'
option_c = 'Momentum before collision < Momentum after collision'
option_d = 'Momentum is always zero'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'What is the formula for gravitational force between two objects?'
option_a = 'F = G(m1m2) / r^2'
option_b = 'F = G(m1m2) * r^2'
option_c = 'F = G(m1 + m2) / r^2'
option_d = 'F = G(m1 + m2) * r^2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'What is the concept of inertial mass?'
option_a = 'An object\'s resistance to changes in motion'
option_b = 'An object\'s weight in a gravitational field'
option_c = 'An object\'s volume'
option_d = 'An object\'s density'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'What is the energy required to change the temperature of a substance?'
option_a = 'Heat'
option_b = 'Work'
option_c = 'Power'
option_d = 'Energy'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'What is the law of universal gravitation?'
option_a = 'Every object attracts every other object with a force proportional to their masses and inversely proportional to the square of the distance between them'
option_b = 'Every object attracts every other object with a force proportional to their volume'
option_c = 'Every object repels every other object with a force proportional to their masses'
option_d = 'None of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'What is the wavelength of a wave?'
option_a = 'Distance between two consecutive crests or troughs'
option_b = 'Distance between the wave\'s source and observer'
option_c = 'Distance the wave travels per second'
option_d = 'Distance between any two points on the wave'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'What is the formula for calculating the velocity of a wave?'
option_a = 'v = f * λ'
option_b = 'v = λ / f'
option_c = 'v = f / λ'
option_d = 'v = λ * f'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'What is the formula for calculating impulse?'
option_a = 'Impulse = F * t'
option_b = 'Impulse = F / t'
option_c = 'Impulse = m * v'
option_d = 'Impulse = m * a'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'What is the effect of a balanced force on an object?'
option_a = 'No motion or constant velocity'
option_b = 'Increase in speed'
option_c = 'Increase in acceleration'
option_d = 'Decrease in speed'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'What is the total mechanical energy of an object?'
option_a = 'Sum of kinetic energy and potential energy'
option_b = 'Kinetic energy only'
option_c = 'Potential energy only'
option_d = 'None of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'What is the force required to move an object at constant speed on a horizontal surface?'
option_a = 'Equal to the frictional force'
option_b = 'Greater than the frictional force'
option_c = 'Less than the frictional force'
option_d = 'Zero'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'What is the law of conservation of angular momentum?'
option_a = 'The total angular momentum of a system remains constant if no external torque acts on it'
option_b = 'The angular momentum is always zero'
option_c = 'The angular momentum of a rotating object is always proportional to its velocity'
option_d = 'None of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'What is the unit of work?'
option_a = 'Joule'
option_b = 'Watt'
option_c = 'Newton'
option_d = 'Hertz'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'Which of the following is a vector quantity?'
option_a = 'Velocity'
option_b = 'Speed'
option_c = 'Distance'
option_d = 'Energy'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'CHM101'

# Tambaya 1
question_text = 'What is the chemical symbol for water?'
option_a = 'H2O'
option_b = 'O2'
option_c = 'CO2'
option_d = 'H2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'What is the atomic number of carbon?'
option_a = '6'
option_b = '12'
option_c = '8'
option_d = '14'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'Which of the following is an alkaline earth metal?'
option_a = 'Calcium'
option_b = 'Sodium'
option_c = 'Iron'
option_d = 'Copper'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'What is the molecular formula for methane?'
option_a = 'CH4'
option_b = 'C2H6'
option_c = 'C3H8'
option_d = 'C4H10'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'Which of the following is a noble gas?'
option_a = 'Helium'
option_b = 'Oxygen'
option_c = 'Nitrogen'
option_d = 'Hydrogen'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'What is the pH value of a neutral solution?'
option_a = '7'
option_b = '0'
option_c = '14'
option_d = '3'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'Which element is a halogen?'
option_a = 'Chlorine'
option_b = 'Oxygen'
option_c = 'Nitrogen'
option_d = 'Carbon'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'What is the chemical formula for hydrochloric acid?'
option_a = 'HCl'
option_b = 'H2SO4'
option_c = 'NaOH'
option_d = 'HNO3'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'What is the atomic number of oxygen?'
option_a = '8'
option_b = '16'
option_c = '14'
option_d = '10'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'What is the name of the compound NaCl?'
option_a = 'Sodium chloride'
option_b = 'Sodium sulfate'
option_c = 'Sodium hydroxide'
option_d = 'Sodium nitrate'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'Which of the following is a strong acid?'
option_a = 'HCl'
option_b = 'CH3COOH'
option_c = 'H2CO3'
option_d = 'NH3'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'Which element is essential for the formation of bones in the human body?'
option_a = 'Calcium'
option_b = 'Phosphorus'
option_c = 'Magnesium'
option_d = 'Iron'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What is the chemical symbol for gold?'
option_a = 'Au'
option_b = 'Ag'
option_c = 'Cu'
option_d = 'Pb'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'What is the molecular formula for ammonia?'
option_a = 'NH3'
option_b = 'N2H4'
option_c = 'NH2'
option_d = 'N2H3'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'Which of the following is an example of an ionic bond?'
option_a = 'NaCl'
option_b = 'H2O'
option_c = 'CO2'
option_d = 'O2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What is the process of a solid turning into a liquid called?'
option_a = 'Melting'
option_b = 'Freezing'
option_c = 'Condensation'
option_d = 'Evaporation'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'What is the element with the highest atomic number?'
option_a = 'Oganesson'
option_b = 'Uranium'
option_c = 'Plutonium'
option_d = 'Neptunium'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'Which gas is most commonly used in light bulbs?'
option_a = 'Argon'
option_b = 'Oxygen'
option_c = 'Nitrogen'
option_d = 'Hydrogen'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'Which of the following is a non-metal?'
option_a = 'Sulfur'
option_b = 'Iron'
option_c = 'Magnesium'
option_d = 'Calcium'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'What is the molar mass of water (H2O)?'
option_a = '18 g/mol'
option_b = '20 g/mol'
option_c = '16 g/mol'
option_d = '22 g/mol'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'What type of bond is formed between two hydrogen atoms in H2?'
option_a = 'Covalent bond'
option_b = 'Ionic bond'
option_c = 'Metallic bond'
option_d = 'Hydrogen bond'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the chemical symbol for sodium?'
option_a = 'Na'
option_b = 'K'
option_c = 'Ca'
option_d = 'Mg'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'Which of the following is a liquid at room temperature?'
option_a = 'Water'
option_b = 'Oxygen'
option_c = 'Helium'
option_d = 'Nitrogen'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'Which of the following elements is a metalloid?'
option_a = 'Silicon'
option_b = 'Sulfur'
option_c = 'Oxygen'
option_d = 'Iron'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'Which of the following is a strong base?'
option_a = 'NaOH'
option_b = 'HCl'
option_c = 'H2SO4'
option_d = 'CH3COOH'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'What is the unit of concentration in chemistry?'
option_a = 'Molarity'
option_b = 'Density'
option_c = 'Mass'
option_d = 'Volume'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What is the common name for dihydrogen monoxide?'
option_a = 'Water'
option_b = 'Hydrogen peroxide'
option_c = 'Ammonia'
option_d = 'Methane'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'Which of the following is a property of acids?'
option_a = 'Sour taste'
option_b = 'Bitter taste'
option_c = 'Slippery'
option_d = 'None of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'What is the atomic number of hydrogen?'
option_a = '1'
option_b = '2'
option_c = '3'
option_d = '0'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'Which of the following elements is most reactive?'
option_a = 'Francium'
option_b = 'Helium'
option_c = 'Oxygen'
option_d = 'Neon'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'What is the name of the acid found in stomachs?'
option_a = 'Hydrochloric acid'
option_b = 'Sulfuric acid'
option_c = 'Acetic acid'
option_d = 'Citric acid'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'What is the formula for calcium chloride?'
option_a = 'CaCl2'
option_b = 'NaCl'
option_c = 'MgCl2'
option_d = 'KCl'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'Which element has the highest electronegativity?'
option_a = 'Fluorine'
option_b = 'Oxygen'
option_c = 'Chlorine'
option_d = 'Nitrogen'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'What is the color of copper sulfate crystals?'
option_a = 'Blue'
option_b = 'Green'
option_c = 'Red'
option_d = 'Yellow'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'Which of the following is a common oxidation state of iron?'
option_a = 'Fe2+'
option_b = 'Fe3+'
option_c = 'Fe1+'
option_d = 'Fe4+'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'What is the atomic mass of carbon?'
option_a = '12.01 u'
option_b = '14.01 u'
option_c = '16.00 u'
option_d = '18.01 u'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'Which of the following is a characteristic of an exothermic reaction?'
option_a = 'Releases energy'
option_b = 'Absorbs energy'
option_c = 'Does not involve energy'
option_d = 'All of the above'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'Which gas is produced when an acid reacts with a metal?'
option_a = 'Hydrogen'
option_b = 'Oxygen'
option_c = 'Nitrogen'
option_d = 'Carbon dioxide'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'What is the process of a gas turning into a liquid called?'
option_a = 'Condensation'
option_b = 'Evaporation'
option_c = 'Melting'
option_d = 'Sublimation'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'Which of the following is an example of a saturated hydrocarbon?'
option_a = 'Methane'
option_b = 'Ethene'
option_c = 'Ethyne'
option_d = 'Acetylene'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'BIO101'

# Tambaya 1
question_text = 'What is the basic unit of life?'
option_a = 'Tissue'
option_b = 'Organ'
option_c = 'Cell'
option_d = 'Organ system'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'Which of these is a prokaryotic organism?'
option_a = 'Bacteria'
option_b = 'Fungi'
option_c = 'Algae'
option_d = 'Protozoa'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'Which organelle is responsible for energy production?'
option_a = 'Nucleus'
option_b = 'Ribosome'
option_c = 'Mitochondrion'
option_d = 'Lysosome'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'DNA is mainly found in which part of the cell?'
option_a = 'Cytoplasm'
option_b = 'Cell membrane'
option_c = 'Nucleus'
option_d = 'Mitochondria'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'Which of these is NOT a type of tissue in animals?'
option_a = 'Epithelial'
option_b = 'Connective'
option_c = 'Muscle'
option_d = 'Xylem'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'Which gas is used by plants for photosynthesis?'
option_a = 'Oxygen'
option_b = 'Carbon dioxide'
option_c = 'Hydrogen'
option_d = 'Nitrogen'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'The green pigment in plants is called:'
option_a = 'Haemoglobin'
option_b = 'Chlorophyll'
option_c = 'Melanin'
option_d = 'Xanthophyll'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'Which kingdom does mushroom belong to?'
option_a = 'Animalia'
option_b = 'Plantae'
option_c = 'Fungi'
option_d = 'Protista'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'Which part of the plant absorbs water?'
option_a = 'Leaves'
option_b = 'Stem'
option_c = 'Roots'
option_d = 'Flower'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'Which blood cells help fight infection?'
option_a = 'Red blood cells'
option_b = 'White blood cells'
option_c = 'Platelets'
option_d = 'Plasma'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'What is the function of red blood cells?'
option_a = 'Fight bacteria'
option_b = 'Clot blood'
option_c = 'Carry oxygen'
option_d = 'Store fat'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'Which organ pumps blood in the human body?'
option_a = 'Liver'
option_b = 'Lungs'
option_c = 'Heart'
option_d = 'Brain'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What is the largest organ in the human body?'
option_a = 'Liver'
option_b = 'Skin'
option_c = 'Lungs'
option_d = 'Brain'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'The process of cell division is called:'
option_a = 'Photosynthesis'
option_b = 'Respiration'
option_c = 'Mitosis'
option_d = 'Fermentation'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'Which part of the brain controls breathing?'
option_a = 'Cerebrum'
option_b = 'Cerebellum'
option_c = 'Medulla'
option_d = 'Hypothalamus'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What do enzymes do in the body?'
option_a = 'Speed up chemical reactions'
option_b = 'Transport oxygen'
option_c = 'Carry messages'
option_d = 'Store energy'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'Which of the following is a vertebrate?'
option_a = 'Earthworm'
option_b = 'Mosquito'
option_c = 'Frog'
option_d = 'Snail'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'Which blood vessel carries blood away from the heart?'
option_a = 'Veins'
option_b = 'Capillaries'
option_c = 'Arteries'
option_d = 'Lymph'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'Which is the powerhouse of the cell?'
option_a = 'Ribosome'
option_b = 'Mitochondria'
option_c = 'Nucleus'
option_d = 'Chloroplast'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'Which macromolecule contains genetic information?'
option_a = 'Protein'
option_b = 'Lipids'
option_c = 'DNA'
option_d = 'Carbohydrates'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'Which process converts glucose into energy?'
option_a = 'Photosynthesis'
option_b = 'Fermentation'
option_c = 'Respiration'
option_d = 'Transpiration'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the function of chloroplasts?'
option_a = 'Digest food'
option_b = 'Photosynthesis'
option_c = 'Produce hormones'
option_d = 'Store waste'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'What is the male reproductive part of a flower?'
option_a = 'Pistil'
option_b = 'Ovary'
option_c = 'Stamen'
option_d = 'Petal'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'Which vitamin is produced by the skin in sunlight?'
option_a = 'Vitamin A'
option_b = 'Vitamin B'
option_c = 'Vitamin C'
option_d = 'Vitamin D'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'Which organ helps in detoxification?'
option_a = 'Kidney'
option_b = 'Liver'
option_c = 'Heart'
option_d = 'Lungs'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'Which of these is part of the respiratory system?'
option_a = 'Trachea'
option_b = 'Esophagus'
option_c = 'Intestine'
option_d = 'Pancreas'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'Where does digestion begin?'
option_a = 'Stomach'
option_b = 'Mouth'
option_c = 'Small intestine'
option_d = 'Liver'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'What is the function of the kidney?'
option_a = 'Pump blood'
option_b = 'Filter blood'
option_c = 'Digest fat'
option_d = 'Store oxygen'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'What type of blood cell helps in clotting?'
option_a = 'Red blood cells'
option_b = 'White blood cells'
option_c = 'Platelets'
option_d = 'Plasma'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'Which organ is part of the central nervous system?'
option_a = 'Heart'
option_b = 'Spinal cord'
option_c = 'Lung'
option_d = 'Stomach'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'Which of these is a hereditary material?'
option_a = 'Enzyme'
option_b = 'RNA'
option_c = 'Protein'
option_d = 'DNA'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'Which of these is a non-communicable disease?'
option_a = 'Tuberculosis'
option_b = 'Diabetes'
option_c = 'Flu'
option_d = 'Malaria'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'Which gas do we inhale from the air?'
option_a = 'Nitrogen'
option_b = 'Oxygen'
option_c = 'Carbon dioxide'
option_d = 'Hydrogen'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'Which of these carries nerve impulses?'
option_a = 'Arteries'
option_b = 'Neurons'
option_c = 'Veins'
option_d = 'Capillaries'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'The process of breathing out is called:'
option_a = 'Inhalation'
option_b = 'Respiration'
option_c = 'Exhalation'
option_d = 'Osmosis'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'Which of these is a plant hormone?'
option_a = 'Testosterone'
option_b = 'Adrenaline'
option_c = 'Auxin'
option_d = 'Insulin'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'Which part of the ear helps with balance?'
option_a = 'Eardrum'
option_b = 'Cochlea'
option_c = 'Semicircular canals'
option_d = 'Pinna'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'Which vitamin prevents night blindness?'
option_a = 'Vitamin A'
option_b = 'Vitamin C'
option_c = 'Vitamin D'
option_d = 'Vitamin E'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'Which organ system controls the body?'
option_a = 'Nervous system'
option_b = 'Digestive system'
option_c = 'Respiratory system'
option_d = 'Circulatory system'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'Which of these is a function of the skeleton?'
option_a = 'Transport nutrients'
option_b = 'Pump blood'
option_c = 'Support the body'
option_d = 'Filter waste'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'MATH201'

# Tambaya 1
question_text = 'What is the derivative of x²?'
option_a = 'x'
option_b = '2x'
option_c = 'x²'
option_d = '2'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'What is the integral of 2x?'
option_a = 'x² + C'
option_b = '2x + C'
option_c = 'x + C'
option_d = '4x + C'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'What is the limit of (1/x) as x approaches infinity?'
option_a = '0'
option_b = '1'
option_c = 'Infinity'
option_d = 'Undefined'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'Which of these is a trigonometric identity?'
option_a = 'sin²x + cos²x = 1'
option_b = 'tanx + cotx = 1'
option_c = 'cosx = sinx'
option_d = 'sinx = tanx'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'What is the derivative of sinx?'
option_a = '-cosx'
option_b = 'cosx'
option_c = '-sinx'
option_d = 'sinx'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'Evaluate the determinant of matrix [[1,2],[3,4]]'
option_a = '10'
option_b = '-2'
option_c = '2'
option_d = '0'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'What is the slope of the line y = 3x + 7?'
option_a = '3'
option_b = '7'
option_c = '10'
option_d = '1'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'What is the value of sin(90°)?'
option_a = '0'
option_b = '1'
option_c = '0.5'
option_d = '-1'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'Which of these is a quadratic equation?'
option_a = 'x + 2 = 0'
option_b = 'x² + 3x + 2 = 0'
option_c = '2x + 5 = 0'
option_d = 'x³ + 2x + 1 = 0'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'What is the domain of the function f(x) = 1/x?'
option_a = 'All real numbers'
option_b = 'x ≠ 0'
option_c = 'x > 0'
option_d = 'x < 0'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'What is the value of cos(0°)?'
option_a = '0'
option_b = '1'
option_c = '-1'
option_d = 'Undefined'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'Which function represents exponential growth?'
option_a = 'y = x²'
option_b = 'y = 2^x'
option_c = 'y = log(x)'
option_d = 'y = √x'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'What is the logarithm base 10 of 100?'
option_a = '1'
option_b = '2'
option_c = '10'
option_d = '100'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'If f(x) = 3x, what is f⁻¹(x)?'
option_a = 'x/3'
option_b = '3x'
option_c = 'x²'
option_d = '1/x'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'Which function is odd?'
option_a = 'y = x²'
option_b = 'y = cos(x)'
option_c = 'y = sin(x)'
option_d = 'y = |x|'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What is the second derivative of x³?'
option_a = '3x'
option_b = '6x'
option_c = '6'
option_d = '3x²'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'Which of these is not a conic section?'
option_a = 'Parabola'
option_b = 'Ellipse'
option_c = 'Line'
option_d = 'Hyperbola'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'What is the range of f(x) = x²?'
option_a = 'All real numbers'
option_b = 'x ≥ 0'
option_c = 'x > 0'
option_d = 'x ≤ 0'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'What is the value of logₑ(e)?'
option_a = '0'
option_b = 'e'
option_c = '1'
option_d = 'Undefined'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'What is the inverse of y = x + 5?'
option_a = 'y = x - 5'
option_b = 'y = x + 5'
option_c = 'y = 5x'
option_d = 'y = 1/x'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'What is the derivative of ln(x)?'
option_a = '1/x'
option_b = 'ln(x)'
option_c = 'x'
option_d = 'xln(x)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the value of cos(180°)?'
option_a = '0'
option_b = '-1'
option_c = '1'
option_d = 'Undefined'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'Which of the following is not continuous at x = 0?'
option_a = 'f(x) = x'
option_b = 'f(x) = |x|'
option_c = 'f(x) = 1/x'
option_d = 'f(x) = x²'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'If y = e^x, what is dy/dx?'
option_a = 'e^x'
option_b = 'x'
option_c = '1'
option_d = 'ln(x)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'What is the antiderivative of 1/x?'
option_a = 'ln|x| + C'
option_b = '1/x² + C'
option_c = 'x + C'
option_d = 'e^x + C'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = 'Which is the correct formula for distance in 2D space?'
option_a = '√[(x₂-x₁)² + (y₂-y₁)²]'
option_b = 'x₂ - x₁'
option_c = 'x² + y²'
option_d = 'x + y'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What is the derivative of tan(x)?'
option_a = 'sec²(x)'
option_b = 'cos(x)'
option_c = 'sin(x)'
option_d = 'cot(x)'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'What is the result of sin(π/2)?'
option_a = '0'
option_b = '1'
option_c = '-1'
option_d = 'π'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'Which of the following is not a function?'
option_a = 'y = x²'
option_b = 'y = √x'
option_c = 'x² + y² = 1'
option_d = 'y = 2x + 3'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'What is the value of the determinant of identity matrix of order 2?'
option_a = '1'
option_b = '0'
option_c = '2'
option_d = '-1'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'What is the inverse of matrix [[1,0],[0,1]]?'
option_a = 'Same matrix'
option_b = 'Negative of matrix'
option_c = 'Transpose of matrix'
option_d = 'Undefined'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'Which of the following is the Laplace transform of 1?'
option_a = '1/s'
option_b = 's'
option_c = '0'
option_d = '1'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'What does "∫" symbolize in calculus?'
option_a = 'Differentiation'
option_b = 'Limit'
option_c = 'Integration'
option_d = 'Multiplication'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'Which of these is a solution to the equation x² - 4 = 0?'
option_a = 'x = 4'
option_b = 'x = -2'
option_c = 'x = 0'
option_d = 'x = 1'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'What is the degree of the polynomial x³ + 2x² + x + 1?'
option_a = '1'
option_b = '2'
option_c = '3'
option_d = '4'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'What is the value of factorial 5 (i.e., 5!)?'
option_a = '120'
option_b = '60'
option_c = '25'
option_d = '720'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'What type of function is y = |x|?'
option_a = 'Linear'
option_b = 'Absolute value'
option_c = 'Exponential'
option_d = 'Logarithmic'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'What is the area under the curve y = x from x=0 to x=2?'
option_a = '2'
option_b = '4'
option_c = '1'
option_d = '2'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'What is the Laplace transform of e^(at)?'
option_a = '1/(s - a)'
option_b = '1/(s + a)'
option_c = 's/(s - a)'
option_d = 'a/s'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'If f(x) = x², then f\'(2) = ?'
option_a = '2'
option_b = '4'
option_c = '8'
option_d = '1'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

course_code = 'GST101'

# Tambaya 1
question_text = 'What does GST stand for in university curriculum?'
option_a = 'General Science and Technology'
option_b = 'General Studies'
option_c = 'Graduate Studies Training'
option_d = 'General Social Topics'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 2
question_text = 'Which of the following is a key purpose of GST courses?'
option_a = 'To promote academic laziness'
option_b = 'To delay graduation'
option_c = 'To broaden students’ knowledge'
option_d = 'To make students fail'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 3
question_text = 'Which of the following GST courses focuses on the English language?'
option_a = 'GST101'
option_b = 'GST105'
option_c = 'GST203'
option_d = 'GST302'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 4
question_text = 'Which type of writing is mostly taught in GST101?'
option_a = 'Technical writing'
option_b = 'Letter writing'
option_c = 'Essay and comprehension writing'
option_d = 'Drama writing'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 5
question_text = 'What is a synonym of “important”?'
option_a = 'Useless'
option_b = 'Necessary'
option_c = 'Late'
option_d = 'Quick'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 6
question_text = 'Which of the following is a punctuation mark?'
option_a = 'Comma'
option_b = 'Number'
option_c = 'Alphabet'
option_d = 'Symbol'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 7
question_text = 'Which sentence is grammatically correct?'
option_a = 'He go to school every day.'
option_b = 'He goes to school every day.'
option_c = 'He going school every day.'
option_d = 'He gone to school every day.'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 8
question_text = 'What is the opposite of “difficult”?'
option_a = 'Hard'
option_b = 'Simple'
option_c = 'Tough'
option_d = 'Complicated'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 9
question_text = 'A paragraph should have how many main ideas?'
option_a = 'Two'
option_b = 'Three'
option_c = 'One'
option_d = 'None'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 10
question_text = 'Which part of speech is the word “quickly”?'
option_a = 'Noun'
option_b = 'Verb'
option_c = 'Adjective'
option_d = 'Adverb'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 11
question_text = 'What is the plural of “child”?'
option_a = 'Childs'
option_b = 'Children'
option_c = 'Childes'
option_d = 'Childrens'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 12
question_text = 'Which of the following is not a vowel letter?'
option_a = 'A'
option_b = 'E'
option_c = 'I'
option_d = 'B'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 13
question_text = 'How many syllables are in the word “education”?'
option_a = '2'
option_b = '3'
option_c = '4'
option_d = '5'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 14
question_text = 'Which sentence uses punctuation correctly?'
option_a = 'He is tall, strong and fast.'
option_b = 'He is tall strong, and fast.'
option_c = 'He is tall, strong, and fast.'
option_d = 'He is, tall strong and fast.'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 15
question_text = 'Which is a declarative sentence?'
option_a = 'Where is the class?'
option_b = 'Come here!'
option_c = 'He likes rice.'
option_d = 'Don’t shout!'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 16
question_text = 'What does “etc.” stand for?'
option_a = 'Every time close'
option_b = 'Et cetera'
option_c = 'End to class'
option_d = 'English terminology course'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 17
question_text = 'Which of these is not a punctuation mark?'
option_a = 'Full stop'
option_b = 'Comma'
option_c = 'Question mark'
option_d = 'Letter A'
correct_option = 'D'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 18
question_text = 'Which is the correct spelling?'
option_a = 'Acomodation'
option_b = 'Accommodation'
option_c = 'Accomodation'
option_d = 'Acommadation'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 19
question_text = 'Which of the following is a formal expression?'
option_a = 'What’s up?'
option_b = 'Hey buddy!'
option_c = 'Good morning, Sir.'
option_d = 'Yo!'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 20
question_text = 'What is the past tense of “run”?'
option_a = 'Runned'
option_b = 'Running'
option_c = 'Ran'
option_d = 'Run'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 21
question_text = 'Which of the following is an example of a preposition?'
option_a = 'Quickly'
option_b = 'Under'
option_c = 'Happy'
option_d = 'And'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 22
question_text = 'What is the correct order of writing an essay?'
option_a = 'Conclusion, Body, Introduction'
option_b = 'Introduction, Conclusion, Body'
option_c = 'Introduction, Body, Conclusion'
option_d = 'Body, Conclusion, Introduction'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 23
question_text = 'What does “communication” mean?'
option_a = 'Keeping quiet'
option_b = 'Sharing ideas and information'
option_c = 'Talking to yourself'
option_d = 'Hearing voices'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 24
question_text = 'Which of these is a skill of listening?'
option_a = 'Interrupting'
option_b = 'Yawning'
option_c = 'Nodding'
option_d = 'Turning away'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 25
question_text = 'Which type of sentence gives a command?'
option_a = 'Interrogative'
option_b = 'Declarative'
option_c = 'Imperative'
option_d = 'Exclamatory'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 26
question_text = '“They are going to the market.” – What is the subject?'
option_a = 'Going'
option_b = 'They'
option_c = 'Market'
option_d = 'To the'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 27
question_text = 'What is the synonym of “fast”?'
option_a = 'Quick'
option_b = 'Late'
option_c = 'Slow'
option_d = 'Short'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 28
question_text = 'What is the meaning of “comprehension”?'
option_a = 'Laughing loudly'
option_b = 'Understanding written text'
option_c = 'Reading silently'
option_d = 'Memorizing facts'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 29
question_text = 'Which one is a correct sentence?'
option_a = 'She don’t like rice.'
option_b = 'She doesn’t likes rice.'
option_c = 'She doesn’t like rice.'
option_d = 'She didn’t likes rice.'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 30
question_text = 'What is the function of an article in a sentence?'
option_a = 'It connects phrases'
option_b = 'It describes action'
option_c = 'It modifies a noun'
option_d = 'It replaces a noun'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 31
question_text = 'Which one is a demonstrative pronoun?'
option_a = 'They'
option_b = 'Them'
option_c = 'This'
option_d = 'Who'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 32
question_text = 'What does the suffix “-ment” in “development” mean?'
option_a = 'A state or condition'
option_b = 'A person who does'
option_c = 'A place'
option_d = 'A negative action'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 33
question_text = 'Which part of speech is “beautiful”?'
option_a = 'Verb'
option_b = 'Noun'
option_c = 'Adjective'
option_d = 'Adverb'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 34
question_text = 'Which is the correct question form?'
option_a = 'He is your friend?'
option_b = 'Is he your friend?'
option_c = 'Your friend is he?'
option_d = 'Friend he is?'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 35
question_text = 'What is an antonym of “cheap”?'
option_a = 'Affordable'
option_b = 'Costly'
option_c = 'Buy'
option_d = 'Price'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 36
question_text = 'Which sentence is in the past tense?'
option_a = 'She eats rice'
option_b = 'She is eating rice'
option_c = 'She ate rice'
option_d = 'She will eat rice'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 37
question_text = 'Which is not a type of sentence?'
option_a = 'Interrogative'
option_b = 'Declarative'
option_c = 'Responsive'
option_d = 'Exclamatory'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 38
question_text = 'What is the plural form of “goose”?'
option_a = 'Gooses'
option_b = 'Geese'
option_c = 'Goos'
option_d = 'Goosen'
correct_option = 'B'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 39
question_text = 'What does the prefix “un-” in “unhappy” mean?'
option_a = 'Very'
option_b = 'Again'
option_c = 'Not'
option_d = 'Small'
correct_option = 'C'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

# Tambaya 40
question_text = 'Which of these is a compound word?'
option_a = 'Notebook'
option_b = 'Happy'
option_c = 'Table'
option_d = 'Strong'
correct_option = 'A'
questions.append((course_code, question_text, option_a, option_b, option_c, option_d, correct_option, 'none'))

cursor.execute("SELECT course_code FROM cbt_courses")
courses = [course[0] for course in cursor.fetchall()]

# Sabuwar list don insertion
questions_to_insert = []

# Duba kowanne course bisa jere
for course in course_codes:
    for question in questions:
        course_code_from_question = question[0]
        if course_code_from_question == course and course_code_from_question in courses:
            questions_to_insert.append(question)

cursor.executemany('''
    INSERT INTO cbt_questions (
        course_code, question_text, option_a, option_b, option_c, option_d, correct_option, image_path
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', questions_to_insert)

# --- Teburin Student Submissions ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_number TEXT NOT NULL,
    course_code TEXT NOT NULL,
    score INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    percentage REAL NOT NULL,
    grade TEXT NOT NULL,
    gpa REAL NOT NULL,
    date_taken TEXT NOT NULL,
    result_status TEXT DEFAULT 'Pending',
    FOREIGN KEY (admission_number) REFERENCES students(admission_number)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cbt_taken (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_number TEXT NOT NULL,
    course_code TEXT NOT NULL,
    date_taken TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_selected_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_number TEXT NOT NULL,
    course_code TEXT NOT NULL
)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cbt_admin_result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        admission_number TEXT NOT NULL,
        course_code TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        date_taken TEXT NOT NULL
    )
''')

# --- CBT Courses (Optional student-based link) ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cbt_courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT NOT NULL,
        course_title TEXT NOT NULL,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
''')

# --- Exam Settings ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exam_settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        duration_minutes INTEGER DEFAULT 60,
        total_questions INTEGER DEFAULT 60
    )
''')

cursor.execute("SELECT COUNT(*) FROM exam_settings")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO exam_settings (duration_minutes, total_questions) VALUES (?, ?)", (60, 60))

# Finalize
conn.commit()
conn.close()

print("CBT database created successfully with 10 courses and 60 questions each.")