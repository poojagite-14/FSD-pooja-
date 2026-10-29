from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 * num2

    return '''
    <h1>Product</h1>

    <form method="post">
        Number 1: <input name="num1"><br><br>
        Number 2: <input name="num2"><br><br>

        <input type="submit" value="Calculate">
    </form>

    <h3>Product = {}</h3>
    '''.format(result)

app.run(debug=True)