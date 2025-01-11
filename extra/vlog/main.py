from flask import Flask,redirect,url_for,session, request, render_template
import settings

app = Flask(__name__, template_folder=settings.TEMPLATES_URL, static_folder=settings.STATIC_URL)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/post/category")
def post_category():
    return "c"


@app.route("/post/view")
def post_view():
    return "v"


@app.route("/about")
def about():
    return "a"


app.config["SECRET_KEY"] = "GGG"

if __name__ == '__main__':
    app.run(debug=True)
