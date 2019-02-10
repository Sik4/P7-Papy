
def __parser__(self):
    stripped_phrase = self.replace(" ", "").replace("-", "").replace("_", "")
    print(stripped_phrase, type(stripped_phrase))
    return stripped_phrase


