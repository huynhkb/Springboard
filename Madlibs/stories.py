"""Madlibs Stories."""
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


stories = Flask(__name__)

stories.config['SECRET_KEY'] = "whatsyourstory"

debug = DebugToolbarExtension(stories) 



@stories.route('/home')
def mad_libs():
    return render_template('home.html')


@stories.route('/story')
def create_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural-noun"]
    return render_template('create_story.html', pl=place, nn=noun, vb=verb, adj=adjective, pn=plural_noun)

# class Story:
#     """Madlibs story.

#     To  make a story, pass a list of prompts, and the text
#     of the template.

#         >>> s = Story(["noun", "verb"],
#         ...     "I love to {verb} a good {noun}.")

#     To generate text from a story, pass in a dictionary-like thing
#     of {prompt: answer, promp:answer):

#         >>> ans = {"verb": "eat", "noun": "mango"}
#         >>> s.generate(ans)
#         'I love to eat a good mango.'
#     """

#     def __init__(self, words, text):
#         """Create story with words and template text."""

#         self.prompts = words
#         self.template = text

#     def generate(self, answers):
#         """Substitute answers into text."""

#         text = self.template

#         for (key, val) in answers.items():
#             text = text.replace("{" + key + "}", val)

#         return text


# # Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
