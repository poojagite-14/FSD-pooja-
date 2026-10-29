from flask import Flask

app = Flask(__name__)

@app.route('/course/<course_name>')
def course(course_name):
    return "Course Name: " + course_name + "<br>Course Information: This course provides knowledge and skills."

if __name__ == '__main__':
    app.run(debug=True)