from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':
        name = request.form['name']
        result = "Search Result: " + name

    return '''
    <h1>Student Search</h1>
    <h3>Name: Pooja Gite</h3>

    <form method="post">
        Student Name:
        <input name="name">
        <br><br>

        <input type="submit" value="Search">
    </form>

    <h3>{}</h3>
    '''.format(result)

app.run(debug=True)