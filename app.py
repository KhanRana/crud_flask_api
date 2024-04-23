from flask import Flask, render_template, request, redirect

# create a flask app
app = Flask(__name__)


items = []  # store items in memory list instead a DB


# render the home page
@app.route('/')
def index():
    return render_template("index.html", items=items)


# add item to the list
@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    items.append(name)
    return redirect('/')


# update an existing item
@app.route("/update", methods=["POST"])
def update():
    old_name = request.form["old_name"]
    new_name = request.form["new_name"]
    if old_name in items:
        index = items.index(old_name)
        items[index] = new_name
        return redirect('/')




if __name__ == "__main__":
    app.run()
