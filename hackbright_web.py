"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/")
def homepage():

    students = hackbright.get_student_by_github()

@app.route("/student-search")
def get_student_form():

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)

    return html


@app.route("/add-student")
def student_add_form():

    return render_template("student_add_form.html")


@app.route("/add-student", methods=['POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github')
    first = request.form.get('first')
    last = request.form.get('last')

    hackbright.make_new_student(first, last, github)

    return render_template("added_student.html",
                           github=github)


@app.route("/project")
def project():
    """Use project title to get project information. """
    title = request.args.get('title')

    project_title = hackbright.get_project_by_title(title)

    student_grades = hackbright.get_grades_by_title(title)

    return render_template("project_description.html",
                            project_title=project_title,
                            student_grades=student_grades)


if __name__ == "__main__":

    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")