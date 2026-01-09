from flask import Flask, render_template, request, redirect, url_for
import database as db
import Attendance_Records as AR

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- STUDENT MANAGEMENT ----------
@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student_id = int(request.form["student_id"])
        name = request.form["name"]
        student_class = request.form["student_class"]
        section = request.form["section"]

        db.smm.add_student(student_id, name, student_class, section)
        return redirect(url_for("index"))

    return render_template("add_student.html")


@app.route("/view_students")
def view_students():
    students = db.smm.view_student()   # return DataFrame or rows
    return render_template("view_students.html", students=students)


@app.route("/enter_marks", methods=["GET", "POST"])
def enter_marks():
    if request.method == "POST":
        student_id = int(request.form["student_id"])
        subject_id = int(request.form["subject_id"])
        semester = int(request.form["semester"])
        marks = int(request.form["marks"])

        db.smm.enter_marks(student_id, subject_id, semester, marks)
        return redirect(url_for("index"))

    return render_template("enter_marks.html")


@app.route("/view_marks")
def view_marks():
    marks = db.smm.view_marks()
    return render_template("view_marks.html", marks=marks)


# ---------- ATTENDANCE ----------
@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    if request.method == "POST":
        AR.at.Store_attendance_percentage()
        return redirect(url_for("attendance"))

    data = AR.at.show_attendance()
    return render_template("attendance.html", data=data)


@app.route("/low_attendance")
def low_attendance():
    data = AR.at.low_attendance_students()
    return render_template("attendance.html", data=data)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
