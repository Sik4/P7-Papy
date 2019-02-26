import requests
import wikipedia
import googlemaps
from flask import request
from app.key import KEY
from temp.parser import PlaceExtractor


class Research:

    def __init__(self):
        try:
            # Get input from user : change it to get by the parser
            user_input = request.args.get("proglang", type=str)
            self.query = PlaceExtractor.extract(user_input)
            print("self.query : ", self.query)

            # googlemaps initialisation
            self.gmaps = googlemaps.Client(key=KEY)

            self.search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
            self.search_payload = {'key': KEY, 'query': self.query}
            self.search_req = requests.get(self.search_url, params=self.search_payload)
            self.search_json = self.search_req.json()

            # Wikipedia initialisation
            wikipedia.set_lang('fr')
            self.research = wikipedia.page(self.query)
            self.title = self.research.title
            self.url = self.research.url
            self.resume = wikipedia.summary(self.query,
                                            sentences=3,
                                            chars=0,
                                            auto_suggest=True,
                                            redirect=True)

        except:
            print(Exception)

    def get_wiki(self):
        # Wiki answer
        try:
            result = '{}<p>Mais on y trouve aussi.... {} [<a href="{}"> Lien wiki </a>]' \
                     '</p></br>'.format(self.title, self.resume, self.url)
            return result

        except:
            return '<p>"{}"ne donne rien</p>'.format(self.query)

    def get_latitude(self):
        # latitude
        try:
            lat = self.search_json["results"][0]["geometry"]["location"]["lat"]
            return lat
        except:
            return 'Nothing Found for Latitude'

    def get_longitude(self):
        # longitude
        try:
            long = self.search_json["results"][0]["geometry"]["location"]["lng"]
            return long
        except:
            return 'Nothing found for Longitude'

    def get_formatted_name(self):
        # Name only
        try:
            name = self.search_json["results"][0]["formatted_address"]
            return name
        except:
            return "Name not found"

    def get_geocode(self):
        try:
            geocode_result = self.gmaps.geocode("" + self.query + "")
            print(geocode_result)
            return geocode_result
        except:
            return "Place not Found"
