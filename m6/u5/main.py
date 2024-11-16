from flask import Flask,redirect,url_for,session, request
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
    htmlbequin = '''
        <html>
            <body>
                <h1>Виберіть вікторину</h1>
                <form method="post" action="/">
                <select name="quiz">
    '''

    formSubmit = '''
        <button type="submit">Надіслати</button>
    '''

    htmlend = f'''
                </select>
                {formSubmit}
                </form>
            </body>
        </html>  
    '''

    quizAll = getQuizs()
   
    opts = ""
    for id, name in quizAll:
        opt = f'''
            <option value={id}>
                {name}
            </option>
        '''
        opts += opt
    return htmlbequin + opts + htmlend


def index():
    if request.method == "GET":
        startQuiz(-1)
        return quizForm()
    else:
        timequiz = request.form.get("quiz")
        startQuiz(timequiz)
        return redirect(url_for("test"))

def test():
    if int(session.get("quiz", 0)) <= 0:
        return redirect(url_for("index"))

    Question = getQuestion(session['last_question'], session['quiz'])
    
    print(Question)
    
    if Question == None or len(Question) == 0:
        return redirect(url_for("result"))
    
    html = f"""
    <h1>{Question[1]}</h1>
    <fieldset>
        <legend>Select a maintenance drone:</legend>

    <div>
        <input type="radio" id="huey" name="drone" value="huey" checked />
        <label for="huey">Huey</label>
    </div>

    <div>
        <input type="radio" id="dewey" name="drone" value="dewey" />
        <label for="dewey">Dewey</label>
    </div>

    <div>
        <input type="radio" id="louie" name="drone" value="louie" />
        <label for="louie">Louie</label>
    </div>
    </fieldset>

    """
    
    
    return html


def result():
    return "бу"


Saut = Flask(__name__, template_folder=folder_templates, static_folder=folder_templates)

Saut.config["SECRET_KEY"] = "GGG"

Saut.add_url_rule('/', 'index', index, methods=['POST', 'GET'])
Saut.add_url_rule('/test', 'test', test)
Saut.add_url_rule('/result', 'result', result)





Saut.run(debug=True)
