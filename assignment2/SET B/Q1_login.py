from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return "Welcome " + username

    return '''
    <h1>Login Form</h1>
    <h3>Name: Pooja Gite</h3>

    <form method="post">
        Username: <input name="username">
        <br><br>

        Password: <input type="password" name="password">
        <br><br>

        <input type="submit" value="Login">
    </form>
    '''

app.run(debug=True)