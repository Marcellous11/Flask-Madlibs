
from flask import Flask, render_template, request
# from requests import request
from stories import Story, story


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/pick')   
def landing_page():
    return render_template('pick.html')



@app.route('/stories')
def your_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    plural_noun = request.args.get("plural_noun")

    # story_type = request.args['story_type']

    content = {"place": place, "verb": verb, "noun": noun, "adjective": adjective, "verb":verb,"plural_noun":plural_noun}


    final_story = story.generate(content)
    return render_template('story.html', story=final_story)