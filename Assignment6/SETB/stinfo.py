from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_info():
    student = {
        "name": "pooja gite",
        "rollno": "202",
        "age" : 20,
        "class" : "BSC(IT)"
    }

    return f"""
    <h2>Student Information</h2>
    Name: {student['name']}<br>
    Roll Number: {student['rollno']}<br>
    Age: {student['age']}<br>
    Class: {student['class']}<br>
   
    """

if __name__ == "__main__":
    app.run(debug=True)