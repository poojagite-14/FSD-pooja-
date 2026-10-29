from flask import Flask

app = Flask(__name__)

@app.route("/students")
def students():

    students = [
        ("pranu", 85),
        ("Riya", 45),
        ("Samiii", 75),
        ("niya", 55),
        ("pooja", 95)
    ]

    result = "<h2>Students Scorign more than 60 Marks</h2>"

    for name, marks in students:
        if marks >= 60:
            result += f"{name} - {marks} marks <br>"

    return result

if __name__ == "__main__":
    app.run(debug=True)
    