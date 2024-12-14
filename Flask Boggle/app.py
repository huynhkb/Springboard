from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "chickenz"

boggle_game = Boggle()


@app.route("/")
def home():
    """Default page of the board"""

    board = boggle_game.make_board()          # generating a board with make_board function
    session['board'] = board                  # creating session for the board to be used in other pages
    high_score = session.get("high_score", 0)
    times_played = session.get("times_played", 0)

    return render_template("index.html", board = board, high_score = high_score, times_played = times_played)


@app.route("/check")
def check():
    """Check valid word"""
    word = request.args.get("word", "").strip()
    board = session.get("board")
    response = boggle_game.check_valid_word(board, word)
    # print(response)  # Debugging output
    return jsonify({'result': response})


@app.route("/score", methods=["POST"])
def score():
    """Updata score data and times_played"""

    data = request.get_json()
    score = data.get("score", 0)

    high_score = session.get("high_score", 0)
    times_played = session.get("times_played", 0)

    session['times_played'] = times_played + 1
    session['high_score'] = max(score, high_score)

    return jsonify(brokeRecord=score > high_score)
