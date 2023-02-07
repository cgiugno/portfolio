from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

application = app
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

@app.route("/about", methods=["GET", "POST"]) 
def about():
    return render_template("about.html")

@app.route("/prose", methods=["GET", "POST"]) 
def prose():
    return render_template("prose.html")

@app.route("/artwork", methods=["GET", "POST"]) 
def artwork():
    return render_template("artwork.html")

@app.route("/wordandimage", methods=["GET","POST"])
def wordandimage():
    return render_template("wordandimage.html")

@app.route("/article", methods=["GET","POST"])
def article():
    return render_template("article.html")