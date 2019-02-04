from flask import Flask, request, render_template, jsonify
import json
import wikipedia
import re
from functions import __parser__
from KEY import key


app = Flask(__name__)

# put an ico icon for favicon error
# with open('fr.json', 'r') as fp:
#   town_list = json.load(fp)


@app.route('/')
def index():
    """Function to return the main template"""
    return render_template('base.html')


@app.route('/town_list_process')
def town_list_process():
    with open('fr.json', 'r') as fp:
        town_list = json.load(fp)

    try:
        user_input = request.args.get("proglang", type=str)
        uinput = str(user_input).lower()
        user_question = __parser__(uinput)
        for cities in town_list:
            print(cities["city"])
            handel = __parser__(cities["city"].lower())
            if re.match(r".*" + handel + ".*", user_question):
                latitude = cities["lat"]
                longitude = cities["lng"]
                wikipedia.set_lang("fr")
                ville = cities["city"]  # or lang but wiki is case sensitive for OpenClassrooms
                pageville = wikipedia.WikipediaPage(ville)
                api_key = key
                url = "https://maps.googleapis.com/maps/api/staticmap?center=" + user_question + "&zoom=12&size=400x400" \
                "&maptype=roadmap&markers=color:blue%7C"+ latitude + "," + longitude + "&key=" + api_key
                wikiresult = pageville.summary
                return jsonify(result=("D'ailleurs, savais tu que ", wikiresult, "?"), mapurl=url)
                # return jsonify({'output': render_template('index.html', result="this is a french city", mapurl=url)})

    except:
        print('Error')


