from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        return "Student Name: " + name

    return '''
    <h1>Student Name</h1>
    <h3>Name: Pooja Gite</h3>

    <form method="post">
        Student Name:
        <input name="name">
        <br><br>

        <input type="submit" value="Submit">
    </form>
    '''

app.run(debug=True)