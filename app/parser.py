"""
Strategy chosen to extract a place information from an user input

Tools
------
- regular expressions (module re from standard library)
- strings methods (.lower(), .strip()....)

6 steps :
------------------------------
1. Transform the user input to lower case
2. Strip the phrase from all accents
3. Extract the information with a regular expression
4. Strip the phrase from all special characters
5. Strip thz phrase from remanent stopwords using a json file listing the most common ones in french
6. Strip the words of less than 3 words
"""

import re
import unidecode
import json


# regular expression looking for locations

pattern = (
    # detect the beginning of the question related to a location
    r"("
        r"adresse\s+de|"
        r"(quelle|quel|ou).*"
            r"(trouve(r|nt)?|"
                r"situe(r|nt)?|"
                r"localise(r|nt)?|"
                r"positionne(r|nt)?|"
            r"est|sont)|"
        r"(re)?chercher?"  
    r")\s+"
    # extract informations between startword and ponctuation
    r"(?P<place>[^.,;:?!]*)"
)


class PlaceExtractor:

    @classmethod
    def extract(cls, question):
        """Apply the parser's 6 steps """
        question = cls._to_lower(question)
        question = cls._remove_accents(question)
        question = cls._extract_place(question)
        question = cls._remove_special(question)
        question = cls._remove_stopwords(question)
        question = cls._remove_short_words(question)
        return question

    @staticmethod
    def _remove_accents(question):
        """remove all accents"""
        question = unidecode.unidecode(question)
        return question

    @staticmethod
    def _to_lower(question):
        """"turning the user input into lower case"""
        question = question.lower()
        return question

    @staticmethod
    def _extract_place(question):
        """extracting the location information"""
        match = re.search(pattern, question)
        if match:
            return match.group('place')
        return question.strip()

    @staticmethod
    def _remove_special(question):
        """removing all special characters"""
        question = re.sub('[^A-Za-z0-9]+', '', question)
        return question

    @staticmethod
    def _remove_stopwords(question):
        """removing the stop words from the stopwordsfr.json (careful, only the french ones"""

        with open('app/stopwordsfr.json', 'r', errors='ignore') as stopwordsfr:
            stopwords_list = json.load(stopwordsfr)
            question = ' '.join([w for w in question.split() if w not in stopwords_list])

        return question

    @staticmethod
    def _remove_short_words(question):
        """removing the short words (less than 3 characters)"""
        question = ' '.join([w for w in question.split() if len(w) > 3])
        return question


def main():
    """Entry of the test program."""
    while True:
        question = input("Question: ")
        if "quitter" == question.lower().strip():
            break
        print("Parsed:", PlaceExtractor.extract(question))
        user_input = PlaceExtractor.extract(question)
        return str(user_input)


if __name__ == "__main__":
    main()
