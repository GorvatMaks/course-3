from flask import Flask,redirect,url_for,session, request, render_template
from random import randint
from db import getQuestion, getQuizs
import os 

folder = os.getcwd()
folder_templates = os.path.join(folder,"m6\\u5\\templates")
print("GGGGGG",folder)
print(folder_templates)



def startQuiz(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0

def quizForm():
    quizAll = getQuizs()

    return render_template("start.html", nane=quizAll)


def index():
    if request.method == "GET":
        startQuiz(-1)
        return quizForm()
    else:
        timequiz = request.form.get("quiz")
        startQuiz(timequiz)
        return redirect(url_for("test"))

def questionForm(Question):
   

    return render_template("test.html", ques=Question)


def test():
    if int(session.get("quiz", 0)) <= 0:
        return redirect(url_for("index"))

    Question = getQuestion(session['last_question'], session['quiz'])
    
    if Question == None or len(Question) == 0:
        return redirect(url_for("result"))
    
    return questionForm(Question)


def result():
    return render_template("rezult.html")


Saut = Flask(__name__, template_folder=folder_templates, static_folder=folder_templates)

Saut.config["SECRET_KEY"] = "GGG"

Saut.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
Saut.add_url_rule('/test', 'test', test)
Saut.add_url_rule('/result', 'result', result)





Saut.run(debug=True)
