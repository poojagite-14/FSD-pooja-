from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/product', methods = ['GET'])
def product_details():
    return jsonify({"msg":"data is display successfully",
                    "name":"Laptop",
                    "Price": 50000,
                    "Category":"Electronic"})

if __name__ == '__main__':
    app.run(debug=True)