from flask import Flask

# create a flask app
app =  Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()