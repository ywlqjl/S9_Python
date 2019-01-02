import datetime

class Etudiant(object):
    """docstring for class etudiant."""
    def __init__(self):
        self._nom = ''
        self._prenom = ''
        self._age = 0
        self._address = ''

    def _get_nom(self):
        print("get nom")
        return self._nom
    def _set_nom(self, v):
        print("set nom")
        self._nom = v
    nom = property(_get_nom, _set_nom)

    def _get_prenom(self):
        print("get prenom")
        return self._prenom
    def _set_prenom(self, v):
        print("set prenom")
        self._prenom = v
    pronom = property(_get_prenom, _set_prenom)

    def _get_age(self):
        print("get age")
        return self._age
    def _set_age(self, v):
        print("set age")
        self._age = v
    age = property(_get_age, _set_age)


    def adresselec(self):
        self._address = self._prenom + "." + self._nom + "@etu.univ-tours.fr"
        return self._address


    def calcul_age(self, date):
        today = datetime.date.today()
        formatted_this_year = today.strftime('%Y')

        birthyear = date.split('/')[2]

        self._age = formatted_this_year - birthyear
        return self._age
