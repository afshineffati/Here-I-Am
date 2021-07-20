from my_app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")     #"<h1>Hello Earth!</h1> \n <h2>Afi here!!!!</h2>"