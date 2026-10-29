from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page!"

@app.route('/contact')
def contact():
    return "This is Contact Page."

@app.route('/services')
def services():
    return "These are Our Services."

if __name__ == '__main__':
    app.run(debug=True)