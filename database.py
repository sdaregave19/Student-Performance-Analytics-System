import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sangamesh19",
    database="student_analytics"
)

print(conn)
cursor = conn.cursor()

# creating tables:-
def tables():
    #students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT  PRIMARY KEY,
        name VARCHAR(100),
        student_class VARCHAR(20),
        section VARCHAR(10)
    )
    """)

    # subjects table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INT  PRIMARY KEY,
        subject_name VARCHAR(50)
    )
    """)

    # marks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        student_id INT,
        subject_id INT,
        semester INT,
        marks INT,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    )
    """)

    # attendance table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        student_id INT,
        attendance_percentage FLOAT,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
    """)

    conn.commit()
    # print("✅ Tables created successfully")


def addsub():# Adding subjects :-
    subjects = [
        ("Mathematics",),
        ("Physics",),
        ("Chemistry",),
        ("Computer Science",)
    ]

    cursor.executemany(
        "INSERT INTO subjects (subject_name) VALUES (%s)",
        subjects
    )

    conn.commit()
    # print("✅ 4 subjects inserted successfully")



# 1️⃣ Student & Marks Management
def add_student(student_id,name,student_class,section):
    sql="INSERT INTO students(student_id,name,student_class,section) VALUES(%s,%s,%s,%s);"
    val=(student_id,name,student_class,section)
    cursor.execute(sql,val)
    conn.commit()
    print("Student added  successfully!")
    print("row affected : ",cursor.rowcount)

def view_student(): # ✅ commit only after data-modifying queries
    cursor.execute("SELECT * FROM students")
    # use fetchall
    rows=cursor.fetchall()
    for row in rows:
        # print(row)
        return row # for stramlit
    
def enter_marks(student_id,subject_id,semester,marks):
    sql="INSERT INTO marks(student_id,subject_id,semester,marks) VALUES(%s,%s,%s,%s)"
    val=(student_id,subject_id,semester,marks)
    cursor.execute(sql,val)
    conn.commit()
    print("marks added successfully!")
    print("row affected :",cursor.rowcount)









