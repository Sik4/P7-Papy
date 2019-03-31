from flask import Flask, request, render_template, jsonify
from app.api_request import Research

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

    try:
        # accessing the user input
        user_input = request.args.get("proglang", type=str)
        response = Research(user_input)
        wikipediaresult = response.get_wiki()
        lat = response.get_latitude()
        lng = response.get_longitude()
        name_r = response.get_formatted_name()
        geo_result = response.get_geocode()

        # printing result in console for testing purposes
        print("geo_result : ", geo_result)
        print("wikipediaresult : ", wikipediaresult)
        print("lat : ", lat)
        print("long : ", lng)
        print("name : ", name_r)

        # Returning the result as a dictionary
        dict_result = {"wikipediaresult": wikipediaresult,
                       "lat": lat,
                       "lng": lng,
                       "name_r": name_r,
                       "geo_result": geo_result}

        print("dict_result:", dict_result)

        return jsonify(dict_result)

    except Exception as e:
        # Raising Error and printing it
        print("désolé petit, je ne te comprends pas ", e)


