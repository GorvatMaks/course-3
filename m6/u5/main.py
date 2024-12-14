from flask import Flask,redirect,url_for,session, request, render_template
from random import randint
from db import getQuestion, getQuizs, checkAnswer
import os 

folder = os.getcwd()
folder_templates = os.path.join(folder,"m6\\u5\\templates")
print("GGGGGG",folder)
print(folder_templates)



def startQuiz(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session["rezTrue"] = 0  
    session["total"] = 0 

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
    QuestionId = Question[0]
    QuestionName = Question[1]
    Answers = Question[2:]


    return render_template("test.html", id=QuestionId, name = QuestionName, ans = Answers)


def test():
    if int(session.get("quiz", 0)) <= 0:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        save_answers()

    Question = getQuestion(session['last_question'], session['quiz'])

    if Question == None or len(Question) == 0:
        return redirect(url_for("result"))
    
    return questionForm(Question)

def save_answers():
    ques_id = request.form.get("q_id")
    a_text = request.form.get("ans_text")
    session['last_question'] = ques_id                
    if checkAnswer(question_id=ques_id,answer_text=a_text) ==  True:
        session["rezTrue"] += 1             
    session["total"] += 1                    
                     
                     
def result():
    return render_template("rezult.html", total=session["total"], rezTrue=session["rezTrue"])


Saut = Flask(__name__, template_folder=folder_templates, static_folder=folder_templates)

Saut.config["SECRET_KEY"] = "GGG"

Saut.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
Saut.add_url_rule('/test', 'test', test,  methods=['POST', 'GET'])
Saut.add_url_rule('/result', 'result', result)





Saut.run(debug=True)
