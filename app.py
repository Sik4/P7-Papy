from flask import Flask, request, render_template, jsonify
import json
from utilz import grandpy
import wikipedia
import re
from utilz import parser
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
    """with open('fr.json', 'r') as fp:
        town_list = json.load(fp)
    """

    try:
        user_input = request.args.get("proglang", type=str)
        wikiresult = grandpy(user_input)
        print(wikiresult)
        return jsonify(result=("D'ailleurs, savais tu que " + wikiresult + "?"))  # , mapurl=url)

    except:
        print('Error')


