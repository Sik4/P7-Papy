import googlemaps
from flask import Flask, request, render_template, jsonify
from app.utilz import grandpy
from app.api_request import Research
from app.key import KEY


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
    """
    with open('fr.json', 'r') as fp:
        town_list = json.load(fp)
    """

    try:
        user_input = request.args.get("proglang", type=str)
        wikiresult = grandpy(user_input)
        response = Research()
        wikipediaresult = response.get_wiki()
        lat = response.get_latitude()
        long = response.get_longitude()
        name_r = response.get_formatted_name()
        geo_result = response.get_geocode()
        print("geo_result : ", geo_result)
        print("wikipediaresult : ", wikipediaresult)
        print("lat : ", lat)
        print("long : ", long)
        print("name : ", name_r)

        return jsonify(result=("D'ailleurs, savais tu que " + wikiresult + "?"))  # , mapurl=url)

    except:
        print('Error')


