from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':
        book = request.form['book']
        result = "Search Result: " + book

    return '''
    <h1>Library Search</h1>
    <h3>Name: Pooja Gite</h3>

    <form method="post">
        Book Name:
        <input name="book">
        <br><br>

        <input type="submit" value="Search">
    </form>

    <h3>{}</h3>
    '''.format(result)

app.run(debug=True)