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

if __name__ == "__main__":
    app.run()
