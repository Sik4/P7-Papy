from functions import parser
import app
import pytest


phrasetest = 'je vis à Montpellier'


@pytest.mark.parser
def test_parser():
    assert parser(phrasetest) == 'jevisàMontpellier'


@pytest.mark.type
def test_type_parser():
    x = parser(phrasetest)
    assert isinstance(x, str)



