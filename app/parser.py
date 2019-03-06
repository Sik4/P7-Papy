"""Exemple de stratégie à adopter pour extraire une info de lieu d'une phrase
entrée par un utilisateur.
Outils
------
- expression rationnelles à l'aide du module re de la bibliothèque standard
- méthodes de chaines de caractère: lower(). strip(), split(), join() et translate()
6 étapes d'extraction proposée
------------------------------
1. Transformer la phrase en minuscules (TODO: laissé pour exercice DONE)
2. Eliminer les accents de la phrase (TODO: laissé pour exercice DONE)
3. Extraire l'info de lieu avec une expression rationnelle (regex) en utilisant
   le module re de la bibliothèque standard (Exemple donné)
4. Eliminer les caractères spéciaux comme apostrophes, tirets, etc. (TODO: laissé pour exercice DONE)
5. Eliminer les mots présents dans une liste de stop words (TODO: laissé pour exercice DONE)
6. Eliminer les mots courts p.ex. moins de 3 lettres (TODO: laissé pour exercice DONE)
"""

import re
import unidecode
import json


# Liste de patterns permettant d'extraire des lieux
# Pour apprendre à utiliser les expressions rationnelles:https://bit.ly/2SvWv8M

pattern = (
    # détection du début de la question de lieu
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
    # Pattern à extraire: phrase ne contenant pas de ponctuation
    r"(?P<place>[^.,;:?!]*)"
)


class PlaceExtractor:

    @classmethod
    def extract(cls, question):
        """Applique toutes les étapes de nettoyage et d'extraction proposées."""
        question = cls._to_lower(question)
        question = cls._remove_accents(question)
        question = cls._extract_place(question)
        question = cls._remove_special(question)
        question = cls._remove_stopwords(question)
        question = cls._remove_short_words(question)
        return question

    @staticmethod
    def _remove_accents(question):
        """eliminer les accents de question et retourner le resultat."""
        question = unidecode.unidecode(question)
        return question

    @staticmethod
    def _to_lower(question):
        """"transformer question en minuscules."""
        question = question.lower()
        return question

    @staticmethod
    def _extract_place(question):
        """Extrait l'info au sujet du lieu."""
        match = re.search(pattern, question)
        if match:
            return match.group('place')
        return question.strip()

    @staticmethod
    def _remove_special(question):
        """éliminer les caractères spéciaux de question"""
        question = re.sub('\W+', ' ', question)
        return question

    @staticmethod
    def _remove_stopwords(question):
        """éliminer les (mots courants) stop words de question."""

        with open('app/stopwordsfr.json', 'r', errors='ignore') as stopwordsfr:
            stopwords_list = json.load(stopwordsfr)
            question = ' '.join([w for w in question.split() if w not in stopwords_list])

        return question

    @staticmethod
    def _remove_short_words(question):
        """éliminer les mots cours de question."""
        question = ' '.join([w for w in question.split() if len(w) > 3])
        return question


def main():
    """Point d'entrée du programme de test."""
    while True:
        question = input("Question: ")
        if "quitter" == question.lower().strip():
            break
        print("Parsed:", PlaceExtractor.extract(question))
        user_input = PlaceExtractor.extract(question)
        return str(user_input)


if __name__ == "__main__":
    main()
