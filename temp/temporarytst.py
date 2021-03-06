target = __import__("functions.py")
parser = target.__parser__


def test_parser(self, monkeypatch):
    """Test if get_latitude() return is a float"""

    def mockreturn():
        return "la vie est belle a montpellier"

    monkeypatch.setattr('parser', mockreturn)
    assert isinstance(x, str)



import unittest

from functions import __parser__
import app as script


class TestPapy(unittest.TestCase):
    def test_parser(self):
        """
        Test that it is a string
        """
        data = "la vie est belle à Montpellier"
        result = __parser__(data)
        self.assertEqual(result, "lavieestbelleàMontpellier")
        self.assertIs(result, str)

    def test_input(self):
        """
        Test if input is a string in lower case
        """
        script.user_input = "La vie est belle à Montpellier"
        self.assertEqual(script.user_question, "lavieestbelleàmontpellier")
        self.assertIs(script.user_question, str)


if __name__ == '__main__':
    unittest.main()


