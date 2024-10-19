from flask import Flask,redirect,url_for,session


def index():
    return "Папа"


def test():
    return redirect(url_for("result"))


def result():
    return "бу"


Saut = Flask(__name__)

Saut.add_url_rule('/', 'index', index)
Saut.add_url_rule('/test', 'test', test)
Saut.add_url_rule('/result', 'result', result)






Saut.run()
