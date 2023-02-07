from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

application = app
bootstrap = Bootstrap(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"]) 
def about():
    return render_template("about.html")

@app.route("/prose", methods=["GET", "POST"]) 
def prose():
    return render_template("prose.html")

@app.route("/artwork", methods=["GET", "POST"]) 
def artwork():
    return render_template("artwork.html")

@app.route("/gamedevelopment", methods=["GET","POST"])
def gamedevelopment():
    return render_template("gamedevelopment.html")

@app.route("/article", methods=["GET","POST"])
def article():
    return render_template("article.html")