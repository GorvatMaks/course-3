from flask import Flask,redirect,url_for,session, request, render_template
import settings
from db import *

app = Flask(__name__, template_folder=settings.TEMPLATES_URL, static_folder=settings.STATIC_URL)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/post/category/<category_name>", methods = ['POST','GET'])
def post_category(category_name):
    category_id = getIdByCategory(category_name)
    print(category_id)
    return render_template("post_category.html", category_name=category_id)


@app.route("/post/view")
def post_view():
    return "v"


@app.route("/about")
def about():
    return "a"


app.config["SECRET_KEY"] = "GGG"

if __name__ == '__main__':
    app.run(debug=True)
