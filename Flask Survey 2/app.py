from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app) 


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


@app.route('/start', methods=["POST"])
def start():
    """Changing from GET to POST and start the survey. Basically making it a state-changing action."""
    session["responses"] = []  # initialize an empty responses list in the session
    return redirect(url_for("questions", question_id=0))


@app.route('/questions/<int:question_id>', methods=["GET", "POST"])
def questions(question_id):
    responses = session.get("responses", [])              # fetch responses from session

    if len(responses) >= len(questions_list):               # if the id reponses equal or greater than the length of the list, then stop (in case user clicks "back" and reanswer more questions)
         return redirect(url_for('thank_you'))
    if question_id >= len(questions_list) or question_id != len(responses):     # and len(responses) != 0:   check if user is accessing outside of question order
        flash("You're trying to access a question out of order. Redirecting to the correct question.")
        return redirect(url_for('questions', question_id=len(responses))) 
    question = questions_list[question_id]               # otherwise, the question will be used to populate questions.html
    return render_template("questions.html", question=question, question_id=question_id)

@app.route('/questions/answer', methods=["POST"])
def add_answer():
    """For each answer, the responses list grows"""
    response = request.form["response"]
    responses = session.get("responses", [])              # fetch responses from session
    responses.append(response)                               # add response to the responses list
    session["responses"] = responses                         # save the updated list back to the session
    next_question_id = len(responses)                        # next question index equals to the current length of the responses list. Adds 1 to index basically
    if next_question_id < len(questions_list):               # if finished with the questions_list, then say thank you, or move to next question
        return redirect(url_for('questions', question_id=next_question_id))       
    else:
        return render_template("thank_you.html")


@app.route('/questions/answers')
def answers():
    """Display the answers from the survey""" 
    responses = session.get("responses", [])       # using [] to ensure responses is always a list
    return render_template("answers.html", responses=responses)


@app.route('/thank_you')
def thank_you():
    """Display the thank you page after completing survey"""
    return render_template("thank_you.html")

