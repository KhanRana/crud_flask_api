from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# create a flask app
app = Flask(__name__, template_folder="templates")
app.config.from_pyfile("settings.py")

MONGO_URI = app.config.get("MONGO_URI")

# create mongo client on startup
try:
    client = MongoClient(MONGO_URI)
    db = client.flask_db
    products = db.products
    print("Connected to the database!")
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
# products = []  # store products in memory list instead a DB


# render the home page
@app.route('/')
def index():
    all_products = products.find() 
    return render_template("index.html", products=all_products)


# add item to the list
@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    products.insert_one({'name': name})

    return redirect('/')


# update an existing item
@app.route("/update", methods=["POST"])
def update():
    old_name = request.form["old_name"]
    new_name = request.form["new_name"]
    if old_name in products:
        index = products.index(old_name)
        products[index] = new_name
        return redirect('/')


# delete an item
@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]
    if name in products:
        products.remove(name)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
