from flask import Flask,redirect,url_for,session, request, render_template

app = Flask(__name__)










app.config["SECRET_KEY"] = "GGG"

if __name__ == '__main__':
    app.run(debug=True)