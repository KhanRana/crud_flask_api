from flask import Flask, render_template, request, redirect, flash
from pymongo import MongoClient

# create a flask app
app = Flask(__name__, template_folder="templates")
app.config.from_pyfile("settings.py")



MONGO_URI = app.config.get("MONGO_URI")
SECRET_KEY = app.config.get("SECRET_KEY")

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
    flash("Product added successfully!", "success")

    return redirect('/')


# update an existing item
@app.route("/update", methods=["POST"])
def update():
    old_name = request.form["old_name"]
    new_name = request.form["new_name"]
    document_to_update = {'name': old_name}
    update_document = {'$set': {'name': new_name}}
    # update the document
    if products.find_one(document_to_update) is None:
        print("No document found with that name")
        flash("No document found with that name", "error")
    else:
        products.update_one(document_to_update, update_document)
        flash("Product updated successfully!", "success")
    
    return redirect('/')


# delete an item
@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]
    try:
        if products.find_one({'name': name}) is None:
            print("No document found with that name")
            flash("No document found with that name", "error")
        else:
            products.delete_one({'name': name})
            print("Deleted document with name:", name)
            flash("Product deleted successfully!", "success")
    except Exception as e:
        print("Error deleting document:", e)
        flash("Error deleting document", "error")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    app.secret_key = SECRET_KEY
    client.close()
