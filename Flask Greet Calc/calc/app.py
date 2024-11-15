# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
import unittest
app = Flask(__name__)

calc = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b
}

@app.route('/<whatMath>')
def math(whatMath):
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    typeMath = calc[whatMath](a, b)
    return str(typeMath)

@app.route("/math/<oper>")
def do_math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    typeMath = calc[oper](a, b)
    return str(typeMath)


