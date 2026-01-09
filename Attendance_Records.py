import mysql.connector 

import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sangamesh19",
    database="student_analytics"
)

# print(conn)
cursor = conn.cursor()
# !2️⃣ Attendance Tracking 

class Attendance_Tracking:
    
    def __init__(self,conn,cursor):
        self.conn=conn
        self.cursor=cursor
        
    def Store_attendance_percentage(self):
        try:
            student_id=int(input("enter student id -> "))
            Days_present=int(input("enter no of days present -> "))
            percentage=round((Days_present/190)*100,2)
        
            query='''INSERT INTO attendance (student_id,attendance_percentage) VALUES (%s,%s)'''
            val=(student_id,percentage)
            self.cursor.execute(query,val)
            self.conn.commit()
            print("Attendance added successfully!")
            print("row affected:", self.cursor.rowcount)
        except Exception as e:
            self.conn.rollback()
            print("ERROR - ",e)
    
    def show_attendance(self):
        self.cursor.execute(''' SELECT * FROM attendance''')
        rows=self.cursor.fetchall()
        column=[X[0] for X in self.cursor.description]
        df=pd.DataFrame(rows,columns=column)
        print(df)
    def low_attendance_students(self):
        self.cursor.execute(''' SELECT * FROM attendance 
                                WHERE attendance_percentage < 75 ''')
        rows=self.cursor.fetchall()
        column=[X[0] for X in self.cursor.description]
        df=pd.DataFrame(rows,columns=column)
        print(df)
    

at=Attendance_Tracking(conn,cursor)