import datetime
import csv
from dateutil.relativedelta import relativedelta

class Etudiant(object):
    """docstring for class etudiant."""
    def __init__(self):
        self._nom = ''
        self._prenom = ''
        self._age = 0
        self._address = ''

    def _get_nom(self):
        return self._nom
    def _set_nom(self, v):
        self._nom = v
    nom = property(_get_nom, _set_nom)

    def _get_prenom(self):
        return self._prenom
    def _set_prenom(self, v):
        self._prenom = v
    prenom = property(_get_prenom, _set_prenom)

    def _get_age(self):
        return self._age
    def _set_age(self, v):
        self._age = v
    age = property(_get_age, _set_age)


    def adresselec(self):
        self._address = self._prenom + "." + self._nom + "@etu.univ-tours.fr"
        return self._address


    def calcul_age(self, date):
        today = datetime.date.today()
        # formatted_this_year = today.strftime('%Y')

        # birthyear = date.split('/')[2]
        birthyear = datetime.datetime.strptime(date, "%d/%m/%Y").date()

        self._age = relativedelta(today, birthyear).years
        return self._age



if __name__=='__main__':
    list_etudiant = []
    with open('fichetu.csv') as f:
        f_csv = csv.reader(f, delimiter=';')
        headers = next(f_csv)
        for row in f_csv:
            etudiant = Etudiant()
            etudiant.calcul_age(row[2])
            etudiant.nom = row[0]
            etudiant.prenom = row[1]
            list_etudiant.append(etudiant)
    for etu in list_etudiant:
        print("nom: "+etu.nom)
        print("prenom: " + etu.prenom)
        print("age: " + str(etu.age))
        print("--------")
