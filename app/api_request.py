import requests
from mediawiki import MediaWiki
import googlemaps
from flask import request
import os
from temp.parser import PlaceExtractor


class Research:

    def __init__(self, user_input):
        try:
            # Get input from user : change it to get by the parser
            # user_input = request.args.get("proglang", type=str)
            self.query = PlaceExtractor.extract(user_input)
            print("self.query : ", self.query)

            # googlemaps initialisation
            self.gmaps = googlemaps.Client(key=os.getenv("KEY"))

            self.search_json = self.get_geocode()

            # Wikipedia initialisation
            self.wikipedia = MediaWiki()
            lat = self.get_latitude()
            lng = self.get_longitude()
            self.article = self.wikipedia.geosearch(latitude=lat, longitude=lng)[0]
            self.page = self.wikipedia.page(self.article)
            self.summary = self.page.summarize(chars=140)
            self.title = self.page.title
            self.url = self.page.url


        except Exception as e:
            print(e)

    def get_wiki(self):
        # Wiki answer
        try:
            result = '{}<p>Mais on y trouve aussi.... {} [<a href="{}"> Lien wiki </a>]' \
                     '</p></br>'.format(self.title, self.summary, self.url)
            return result

        except:
            return '<p>"{}"ne donne rien</p>'.format(self.query)

    def get_latitude(self):
        # latitude
        try:
            lat = self.search_json[0]["geometry"]["location"]["lat"]
            return lat
        except:
            return 'Nothing Found for Latitude'

    def get_longitude(self):
        # longitude
        try:
            lng = self.search_json[0]["geometry"]["location"]["lng"]
            return lng
        except:
            return 'Nothing found for Longitude'

    def get_formatted_name(self):
        # Name only
        try:
            name = self.search_json[0]["formatted_address"]
            return name
        except:
            return "Name not found"

    def get_geocode(self):

        geocode_result = self.gmaps.geocode(self.query)
        print(geocode_result)
        return geocode_result


def main():
    response = Research("Ou se trouve Montpellier ? ")
    wikipediaresult = response.get_wiki()
    print("wikipediaresult : ", wikipediaresult)
    lat = response.get_latitude()
    print("lat : ", lat)
    lng = response.get_longitude()
    print("long : ", lng)
    name_r = response.get_formatted_name()
    print("name : ", name_r)
    geo_result = response.get_geocode()
    print("geo_result : ", geo_result)


if __name__ == "__main__":
    main()
