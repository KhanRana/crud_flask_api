from flask import (Flask, render_template, request, 
                   redirect, flash, jsonify, abort)
from pymongo import MongoClient

# create a flask app
app = Flask(__name__, template_folder="templates")
app.config.from_pyfile("settings.py")


# 404 Error handler, returns a json response 
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


MONGO_URI = app.config.get("MONGO_URI")
SECRET_KEY = app.config.get("SECRET_KEY")
PORT= app.config.get("PORT", 5500)

# create mongo client on startup
try:
    client = MongoClient(MONGO_URI)
    db = client.flask_db
    products = db.products
    print("Connected to the database!")
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

# products = []  # store products in memory list instead a DB

@app.route('/status')
def status():
    return "The server is working fine!"

# render the home page
@app.route('/')
def index():
    all_products = products.find() 
    return render_template("index.html", products=all_products)

# add item to the list
@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    if products.insert_one({'name': name}):
        print("Inserted document with name:", name)
        # products.append(name)  # add to in-memory list
        flash("Product added successfully!", "success")  # show success message
    else:
        flash("Error adding product", "error")  # show error message
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
        abort(404, description="No document found with that name")
    else:  
        products.update_one(document_to_update, update_document)
        flash("Product updated successfully!", "success")
    
    return redirect('/')


# delete an item
@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]
    
    if products.find_one({'name': name}) is None:
        print("No document found with that name")
        abort(404, description="No document found with that name")
    else:
        products.delete_one({'name': name})
        print("Deleted document with name:", name)
        flash("Product deleted successfully!", "success")

    return redirect('/')


if __name__ == "__main__":
    app.run(port=PORT, host="0.0.0.0")
    app.secret_key = SECRET_KEY
    client.close()
