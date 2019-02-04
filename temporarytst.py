target = __import__("functions.py")
parser = target.__parser__


def test_parser(self, monkeypatch):
    """Test if get_latitude() return is a float"""

    def mockreturn():
        return "la vie est belle a montpellier"

    monkeypatch.setattr('parser', mockreturn)
    assert isinstance(x, str)

