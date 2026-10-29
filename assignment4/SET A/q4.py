from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Home Page!"

@app.route('/student')
def student():
    return "Welcome Students! This is the Student Page."

@app.route('/faculty')
def faculty():
    return "Welcome Faculty! This is the Faculty Page."

if __name__ == '__main__':
    app.run(debug=True)