from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        feedback = request.form['feedback']
        return "Pooja Gite<br>Thank you for your feedback!"

    return '''
    <h1>Feedback Form</h1>
    <h3>Name: Pooja Gite</h3>

    <form method="post">
        Feedback: <input name="feedback">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    '''

app.run(debug=True)