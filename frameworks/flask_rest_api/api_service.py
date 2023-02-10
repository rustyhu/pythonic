# refer to https://www.hackdeploy.com/creating-you-first-python-rest-api/

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": u"Pampers",
        "balance_on_hand": 10
    },
    {
        "id": 2,
        "title": u"Diapers",
        "balance_on_hand": 5
    },
]


@app.route("/")
def index():
    return "You have reached the default route. Congratulations!"


@app.route("/hello")
def say_hello():
    return "Hello World!"


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({"products": products})


@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):

    p = [p for p in products if str(p["id"]) == str(id)]
    return jsonify({"product": p})


@app.route("/api/product", methods=["POST"])
def post_product():

    # check if request has required attributes and is json data
    if not request.json or not "id" in request.json:
        abort(400)

    # get product attributes passed by dictionary
    productID = int(request.json["id"])  # id is a required field
    # this is not required. if not available get blank string
    product_name = request.json.get("name", "")
    # this is not required. if not available get blank string
    boh = request.json.get("balance_on_hand", 0)

    # create new product
    newProduct = {
        "id": productID,
        "title": product_name,
        "balance_on_hand": boh
    }

    products.append(newProduct)
    return jsonify({"products": products})


@app.route("/filetest")
def file_contents_test():
    """return str read from file, like a json or html"""
    filesrc = "./bookmarks.html"
    contents = ""
    with open(filesrc, "r") as f:
        contents = f.read()
        # print(f"read file get: [\n{contents}\n]")

    return contents


if __name__ == "__main__":
    app.run(port=5000, debug=True)
