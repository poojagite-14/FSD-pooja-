from flask import Flask, request

app = Flask(__name__)

@app.route("/studentt", methods=["GET", "POST"])
def student():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Welcome {name} to the Studentt Page"
    
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)