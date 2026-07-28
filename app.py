from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def form():
    return render_template("resume_form.html")

@app.route("/resume", methods=["POST"])
def resume():
    # personal info
    full_name = request.form["full_name"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    linkedin = request.form["linkedin"]
    github = request.form["github"]

    # education
    university = request.form["university"]
    faculty = request.form["faculty"]
    department = request.form["department"]
    graduation_year = request.form["graduation_year"]
    gpa = request.form["gpa"]

    # skills
    programming_languages = ", ".join(
        request.form.getlist("programming_languages")
    )

    web =", ".join(
        request.form.getlist("web")
    )

    database = ", ".join(
        request.form.getlist("database")
    )

    other_skills=request.form.get("other_skills")
    
    # Languages
    languages = ", ".join(
        request.form.getlist("languages")
    )

    # Projects

    project_1 = request.form["project_1"]
    project_1_description = request.form["project_1_description"]

    project_2 = request.form["project_2"]
    project_2_description = request.form["project_2_description"]

    # About Me
    about_me = request.form["about_me"]

    # Template
    template = request.form.get("template")


    return render_template("resume.html",full_name=full_name,email=email,
                        phone_number=phone_number,address=address,
                        linkedin=linkedin ,github=github,
                        university=university, faculty=faculty,
                        department=department, graduation_year=graduation_year,
                        gpa=gpa, programming_languages=programming_languages,
                        web=web, database=database, other_skills=other_skills,
                        languages=languages, project_1=project_1,
                        project_1_description=project_1_description,
                        project_2=project_2, project_2_description=project_2_description,
                        about_me=about_me, template=template
                        )

if __name__ == "__main__":
    app.run(debug=True)