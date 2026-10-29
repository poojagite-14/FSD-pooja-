from flask import Flask

app = Flask(__name__)

@app.route("/")
def employee_list():

    employees = [
        ("pooja gite", "IT", 45000),
        ("Priya avhad", "ITI", 40000),
        ("Aman mule", "DATA ENTRY", 50000),
        ("Sneha raut", "Marketing", 42000),
        ("Vikram chaudhry", "teacher", 55000)
    ]

    employee_details = ""

    for name, department, salary in employees:
        employee_details += f"""
        <p>
            Name: {name}<br>
            Department: {department}<br>
            Salary: ₹{salary}
        </p>
        <hr>
        """

    return f"""
    <h2>List of Employees</h2>
    {employee_details}
    """

if __name__ == "__main__":
    app.run(debug=True)