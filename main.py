import database as db
import streamlit as st
import Attendance_Records as AR
import pandas as pd
from datetime import datetime
while True:
    print('''-----------\n1️⃣  Student & Marks Management\n2️⃣  Attendance Tracking\n3️⃣  Performance Analytics\n4️⃣  Attendance vs Marks Analysis\n---------- ''')
    
    option=int(input("Select option -> "))
    
    if option==1:#Student & Marks Management
        print('''---------\n1.Add student\n2.View student list\n3.Enter marks\n4.show marks\n----------''')
        
        option1=int(input("Select option -> "))
        
        if option1==1:
            student_id=int(input("enter student id -> "))
            name=input("enter student name -> ")
            student_class=input("enter student_class -> ")
            section=input("enter section -> ")
            db.smm.add_student(student_id,name,student_class,section)
        elif option1==2:
            db.smm.view_student()
        elif option1==3:
            student_id=int(input("enter student id -> "))
            subject_id=int(input("enter subject id -> "))
            semester=int(input("enter semerter(I)"))
            marks=int(input("enter marks /80 -> "))
            db.smm.enter_marks(student_id,subject_id,semester,marks)
        elif option1==4:
            db.smm.view_marks()
        else:
            print("enter vaild option")   
    elif option==2:
        print('''---------\n1.Store attendance percentage\n2.show_attendance\n3.low attendance students\n----------''')
        option2=int(input("Select option -> "))
        if option2==1:
            AR.at.Store_attendance_percentage()
        elif option2==2:
            AR.at.show_attendance()
        else:
            AR.at.low_attendance_students()
    elif option==3:
        pass
    else:
        pass
            
            
            
            
            
            
            
            


            
            
            
            
            
# 
# st.title("Student Performance Analytics System")
# 
# Sidebar for main menu
# menu = ["Student & Marks Management", "Attendance Tracking", "Performance Analytics", "Attendance vs Marks Analysis"]
# choice = st.sidebar.selectbox("Select Feature", menu)
# 
# -------------------------
# 1️⃣ Student & Marks Management
# -------------------------
# if choice == "Student & Marks Management":
    # st.subheader("Student & Marks Management")
# 
    # sub_menu = ["Add Student", "View Student List", "Enter Marks"]
    # sub_choice = st.radio("Choose Action", sub_menu)
# 
    # if sub_choice == "Add Student":
        # st.write("Add a new student")
        # student_id = st.number_input("Student ID", min_value=1, step=1)
        # name = st.text_input("Name")
        # student_class = st.text_input("Class")
        # section = st.text_input("Section")
        # if st.button("Add Student"):
            # db.add_student(student_id, name, student_class, section)
            # st.success(f"Student {name} added successfully!")
# 
    # elif sub_choice == "View Student List":
        # st.write("Student List")
        # students = db.view_student()  # Make sure this returns a list of rows
        # for s in students:
            # st.write(s)
# 
    # elif sub_choice == "Enter Marks":
        # st.write("Enter Marks for a Student")
        # student_id = st.number_input("Student ID", min_value=1, step=1, key="marks_student")
        # subject_id = st.number_input("Subject ID", min_value=1, step=1)
        # semester = st.number_input("Semester", min_value=1, step=1)
        # marks = st.number_input("Marks (/80)", min_value=0, max_value=80, step=1)
        # if st.button("Submit Marks"):
            # db.enter_marks(student_id, subject_id, semester, marks)
            # st.success("Marks entered successfully!")