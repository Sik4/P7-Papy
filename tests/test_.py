# from functions import parser
from app import parser
import json
from app.api_request import Research
import app.papycore
import pytest


def test_remove_accent():
    assert parser.PlaceExtractor._remove_accents("je vis à Montpellier") == "je vis a Montpellier"


def test_to_lower():
    assert parser.PlaceExtractor._to_lower("VIVE LA REPUBLIQUE") == "vive la republique"


def test_remove_special():
    assert parser.PlaceExtractor._remove_special("ça alors !") == "ça alors "


def test_remove_stop_words():
    assert parser.PlaceExtractor._remove_stopwords(
        "Aujourd'hui, je cherche Lyon !") == "Aujourd'hui, cherche Lyon !"


# Open mock for wikipedia


def test_research__init__(monkeypatch):
    """Test get_georesult() return"""

    class Mockgoogleclient:
        def __init__(self, key):
            pass

        def geocode(self, query):
            with open("tests/mockgeoresult", 'r') as f:
                return json.load(f)

    class Mockwikipage:
        title = "London"
        url = 'http://www.wikipedia.org/london'

        def summarize(self, chars):
            return 'Londre est une ville en Angleterre'

    class Mockmediawiki:
        def __init__(self, lang):
            pass

        def geosearch(self, latitude, longitude):
            return ['London']

        def page(self, title):
            return Mockwikipage()

    monkeypatch.setattr('app.api_request.googlemaps.Client', Mockgoogleclient)
    monkeypatch.setattr('app.api_request.MediaWiki', Mockmediawiki)

    research = Research("Je cherche Londre")

    assert research.title == "London"
    assert research.url == 'http://www.wikipedia.org/london'
    assert research.search_json[0]["geometry"]["location"]["lat"] == 51.5073509
    assert research.search_json[0]["geometry"]["location"]["lng"] == -0.1277583


def test_research_get_latitude(monkeypatch):
    """Test get_georesult() return"""

    def mock__init__(self, query):
        with open("tests/mockgeoresult", 'r') as f:
            self.search_json = json.load(f)

    monkeypatch.setattr('app.api_request.Research.__init__', mock__init__)

    research = Research("Je cherche Londre")

    assert research.get_latitude() == 51.5073509






