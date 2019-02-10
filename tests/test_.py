from functions import __parser__
import app
import pytest


phrasetest = 'je vis à Montpellier'


@pytest.mark.parser
def test_parser():
    assert __parser__(phrasetest) == 'jevisàMontpellier'


@pytest.mark.type
def test_type_parser():
    x = __parser__(phrasetest)
    assert isinstance(x, str)

