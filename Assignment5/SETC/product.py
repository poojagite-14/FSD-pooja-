from flask import Flask, request

app = Flask(__name__)

@app.route("/product", methods=["GET", "POST"])
def product():

    if request.method == "POST":
        product_name = request.form.get("product_name")
        quantity = request.form.get("quantity")
        price = request.form.get("price")

        return f"""
        <h3>Order Details:</h3>
        <p>
            Product Name: {product_name}<br>
            Quantity: {quantity}<br>
            Price: {price}
        </p>
        """

    return '''
        <form method="post">
            Product Name: <input type="text" name="product_name"><br>
            Quantity: <input type="text" name="quantity"><br>
            Price: <input type="text" name="price"><br>
            <input type="submit" value="Place Order">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)