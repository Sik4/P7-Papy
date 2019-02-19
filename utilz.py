from temp.parser import PlaceExtractor
import wikipedia


def grandpy(user_input):
    print(user_input)
    uinput = PlaceExtractor.extract(user_input)
    print(uinput)
    wikipedia.set_lang("fr")
    wikipage = wikipedia.WikipediaPage(uinput)
    wikiresult = wikipage.summary
    return str(wikiresult)


def main():
    print(grandpy("Montpellier"))






def parser(self):
    stripped_phrase = self.replace(" ", "").replace("-", "").replace("_", "")
    print(stripped_phrase, type(stripped_phrase))
    return stripped_phrase


def grandpy2(user_input, town_list):
    uinput = str(user_input).lower()
    user_question = parser(uinput)
    for cities in town_list:
        print(cities["city"])
        handel = parser(cities["city"].lower())
        if re.match(r".*" + handel + ".*", user_question):
            latitude = cities["lat"]
            longitude = cities["lng"]
            wikipedia.set_lang("fr")
            ville = cities["city"]  # or lang but wiki is case sensitive for OpenClassrooms
            pageville = wikipedia.WikipediaPage(ville)
            api_key = key
            url = "https://maps.googleapis.com/maps/api/staticmap?center=" + user_question + "&zoom=12&size=400x400" \
            "&maptype=roadmap&markers=color:blue%7C" + latitude + "," + longitude + "&key=" + api_key
            wikiresult = pageville.summary
            return wikiresult


if __name__ == "__main__":
    main()



