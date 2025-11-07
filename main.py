from pyscript import display, document

def compute(e):
    document.getElementById('output').innerHTML = ""

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    subjects = ["Filipino", "English", "Math", "Science", "Social Studies", "PE"]
    units = (3, 5, 5, 4, 3, 1)

    grades = [
        int(document.getElementById("filipino").value),
        int(document.getElementById("english").value),
        int(document.getElementById("math").value),
        int(document.getElementById("science").value),
        int(document.getElementById("social_studies").value),
        int(document.getElementById("pe").value)
    ]

    total_units = sum(units)
    weighted_sum = 0

    grade_summary = f''
    for subject, grade, unit in zip(subjects, grades, units):
        weighted_sum += grade * unit
        grade_summary += f"{subject}: {grade}"

    gwa = weighted_sum / total_units

    display(f" Name: {fname} {lname}", target='output')
    display(f" Grades : {grade_summary}", target='output')
    display(f" Your General Weighted Average: {gwa:.2f}", target='output')