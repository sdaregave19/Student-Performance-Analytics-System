import Student_and_Marks_Management as db
import streamlit as st
import Attendance_Records as AR
import pandas as pd
import Performance_Analytics as PD
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
        print('''---------\n1.Subject_wise_Average_Marks\n2.Top3persubject\n3.\n----------''')
        option3=int(input("Select option -> "))
        if option3==1:
            PD.analysis.Subject_wise_Average_Marks()
        elif option3==2:
            PD.analysis.Top3persubject()
        else:
            pass
            
            
            
            
        