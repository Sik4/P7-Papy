# from functions import parser
import temp.parser
import app
import pytest


def test_remove_accent():
    assert PlaceExtractor._remove_accents("je vis à Montpellier") == "je vis a Montpellier"


"""
phrasetest = 'je vis à Montpellier'


@pytest.mark.parser
def test_parser():
    assert parser(phrasetest) == 'jevisàMontpellier'


@pytest.mark.type
def test_type_parser():
    x = parser(phrasetest)
    assert isinstance(x, str)

"""



