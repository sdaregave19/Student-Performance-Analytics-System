import mysql.connector 
import pandas as pd

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



#!1️⃣ Student & Marks Management
class Student_Marks_Management:
    @staticmethod
    def add_student(student_id,name,student_class,section):
        try:
            sql="INSERT INTO students(student_id,name,student_class,section) VALUES(%s,%s,%s,%s);"
            val=(student_id,name,student_class,section)
            cursor.execute(sql,val)
            conn.commit()
            print("Student added  successfully!")
            print("row affected : ",cursor.rowcount)
        except Exception as e:
            conn.rollback()
            print("Student already exisit!!")

    @staticmethod
    def view_student(): # ✅ commit only after data-modifying queries
        cursor.execute("SELECT * FROM students")
        # use fetchall
        rows=cursor.fetchall()
        columns=[col[0] for col in cursor.description]
        df=pd.DataFrame(rows,columns=columns)
        print(df)
        # for row in rows:
            # print(row)
            # return row # for stramlit

    @staticmethod
    def enter_marks(student_id, subject_id, semester, marks):
        try:
            cursor.execute("SELECT 1 FROM students WHERE student_id = %s",(student_id,))
            student=cursor.fetchone()
            if student is not None:
               print("student already present")
               return
            if not (0 <= marks <= 80):
                print("Marks must be between 0 and 80")
                return

            sql = """
            INSERT INTO marks(student_id, subject_id, semester, marks)
            VALUES (%s, %s, %s, %s)
            """
            val = (student_id, subject_id, semester, marks)

            cursor.execute(sql, val)
            conn.commit()

            print("Marks added successfully")
            print("row affected :",cursor.rowcount)
        except Exception as e:
            conn.rollback() # undo changes
            print("Invalid student ID or duplicate entry")
            
    @staticmethod
    def view_marks():
        print('''---------\n1.all table\n2.specific student\n----------''')
        option=int(input("enter option"))
        if option==1:
            cursor.execute("SELECT * FROM marks")
            # use fetchall
            rows=cursor.fetchall()
            columns=[col[0] for col in cursor.description]
            df=pd.DataFrame(rows,columns=columns)
            print(df)
            # for row in rows:
                # print(row)
                # return row # for stramlit
        elif option == 2:
            student_id = int(input("Enter student ID: "))
            cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
            rows = cursor.fetchall()
            if rows:
                columns=[col[0] for col in cursor.description]
                df=pd.DataFrame(rows,columns=columns)
                print(df)
            else:
                print("No marks found for this student")
        else:
            print("Invalid option")

# !2️⃣ Attendance Tracking 





