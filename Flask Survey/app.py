from flask import Flask, request, render_template, redirect, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app) 


responses = []  # store user responses
survey = surveys.surveys["satisfaction"]  # load the selected survey
title = survey.title
instructions = survey.instructions
questions = survey.questions
questions_list = []
for each_question in questions:           # adding each question to questions_list
    questions_list.append(each_question)


@app.route('/')
def start_survey():
    return render_template("home.html", title=title, instructions=instructions, questions=questions)

# @app.route('/questions/0')
# def questions_0():
#     return render_template("questions-0.html", questions_0=questions[0])   #basically it's Questions.surveys["satisfaction"].questions[0].question


@app.route('/questions/<int:question_id>', methods=["GET", "POST"])
def questions(question_id):
    if question_id >= len(questions_list):               # if the id is equal or greater than the length of the list, then stop
        return redirect("thank_you.html")
    question = questions_list[question_id]               # otherwise, the question will be used to populate questions.html
    return render_template("questions.html", question=question, question_id=question_id)

@app.route('/questions/answer', methods=["POST"])
def add_answer():
    response = request.form["response"]
    responses.append(response)                               # add response to the responses list
    next_question_id = len(responses)                        # next question index equals to the current length of the responses list. Adds 1 to index basically
    if next_question_id < len(questions_list):               # if finished with the questions_list, then say thank you, or move to next question
        return redirect(url_for('questions', question_id=next_question_id))       
    else:
        return render_template("thank_you.html")


@app.route('/questions/answers')
def answers():
    return render_template("answers.html", responses=responses)
