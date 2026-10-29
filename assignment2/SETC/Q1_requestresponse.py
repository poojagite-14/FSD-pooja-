from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Pooja, Welcome to Flask!"

app.run(debug=True)