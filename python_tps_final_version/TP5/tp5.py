# conding=utf-8
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
from sqlalchemy.orm import relationship
import xml.etree.ElementTree as ET



engine = create_engine('sqlite:///database_tp5.db:', echo=False)
Base = declarative_base()



class Regions(Base):
    __tablename__ = 'regions'
    code_region = Column(Integer, primary_key=True)
    nom_region = Column(String(50))
    nb_arrondi = Column(Integer)
    nb_canton = Column(Integer)
    nb_commune = Column(Integer)
    population_municpale = Column(Integer)
    population_totale = Column(Integer)

    departements = relationship("Departements", back_populates="region")

class Departements(Base):
    __tablename__ = 'departements'
    code_departement = Column(String(50), primary_key=True)
    nom_departement = Column(String(50))
    nb_arrondi = Column(Integer)
    nb_canton = Column(Integer)
    nb_commune = Column(Integer)
    population_municpale = Column(Integer)
    population_totale = Column(Integer)

    code_region = Column(Integer, ForeignKey('regions.code_region'))
    region = relationship("Regions", back_populates="departements")

    communes = relationship("Communes", back_populates="departements")


class Communes(Base):
    __tablename__ = 'communes'
    code_commune = Column(Integer, primary_key=True)
    code_departement = Column(Integer, ForeignKey('departements.code_departement'), primary_key=True)
    nom_commune = Column(String(50))
    population_part = Column(Integer)
    population_municpale = Column(Integer)
    population_totale = Column(Integer)
    departements = relationship("Departements", back_populates="communes")

class NouvellesRegions(Base):
    __tablename__ = 'nouvellesRegions'
    code_region = Column(Integer, primary_key=True)
    nom_region = Column(String(50))
    nb_commune = Column(Integer)
    population_municpale = Column(Integer)
    population_totale = Column(Integer)

    departements = relationship("Departements", back_populates="nouvellesRegions")
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def creatTables():
    with open('data_Base_de_donnees/regions.csv', newline='', encoding = 'ISO-8859-1') as csvfile:
        count = 0;
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            count += 1;
            if count > 8:
                print(row)
                region = Regions()
                region.code_region = row[0]
                region.nom_region = row[1]
                region.nb_arrondi = row[2].replace(' ', '')
                region.nb_canton = row[3].replace(' ', '')
                region.nb_commune = row[4].replace(' ', '')
                region.population_municpale = row[5].replace(' ', '')
                region.population_totale = row[6].replace(' ', '')
                session.add(region)
        session.commit()

    with open('data_Base_de_donnees/departements.csv', newline='', encoding = 'ISO-8859-1') as csvfile:
        count = 0;
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            count += 1;
            if count > 8:
                departement = Departements()
                departement.code_region = row[0]
                departement.code_departement = row[2]
                departement.nom_departement = row[3]
                departement.nb_arrondi = row[4].replace(' ', '')
                departement.nb_canton = row[5].replace(' ', '')
                departement.nb_commune = row[6].replace(' ', '')
                departement.population_municpale = row[7].replace(' ', '')
                departement.population_totale = row[8].replace(' ', '')
                session.add(departement)
        session.commit()

    with open('data_Base_de_donnees/communes.csv', newline='', encoding = 'ISO-8859-1') as csvfile:
        count = 0;
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            count += 1;
            if count > 8:

                commune = Communes()
                commune.code_commune = row[5]
                commune.nom_commune = row[6]
                commune.code_departement = row[2]
                commune.population_municpale = row[7].replace(' ', '')
                commune.population_part = row[8].replace(' ', '')
                commune.population_totale = row[9].replace(' ', '')
                session.add(commune)

        session.commit()

def comparerPopulations():
    for row in session.query(Regions).all():
        totale_region = 0
        for departement_item in row.departements:
            totale_region += departement_item.population_totale
        print(row.nom_region, totale_region)


def trouverMemeNom():
    lstCommunes = session.query(distinct(Communes.nom_commune)).all() #return colonne nom_commune

    for row in lstCommunes:
        print("------------------------------------------")
        # print(row[0]) #print le nom de commune
        lstDepartements = session.query(Communes.nom_commune.label('nom_commune'), Communes.code_departement.label('code_departement')).filter(Communes.nom_commune == row[0]).all()

        for d in lstDepartements:
            print(d[0],"\t\t", d[1])


def database_to_xml(nomFichier):
    # outfile = file(outfileName, 'w')
    with open(nomFichier, "a") as outfile:
    # connection = psycopg.connect(CONNECT_ARGS)
    # cursor = connection.cursor()
        rows_regions = session.query(Regions).all()
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<mydata>\n')
        for row in rows_regions:
            outfile.write('  <row>\n')
            outfile.write('    <code_region>%s</code_region>\n' % row.code_region)
            outfile.write('    <nom_region>%s</nom_region>\n' % row.nom_region)
            outfile.write('    <nb_arrondi>%s</nb_arrondi>\n' % row.nb_arrondi)
            outfile.write('    <nb_canton>%s</nb_canton>\n' % row.nb_canton)
            outfile.write('    <nb_commune>%s</nb_commune>\n' % row.nb_commune)
            outfile.write('    <population_municpale>%s</population_municpale>\n' % row.population_municpale)
            outfile.write('    <population_totale>%s</population_totale>\n' % row.population_totale)

            outfile.write('  </row>\n')
        outfile.write('</mydata>\n')

def xml_to_database():
    tree = ET.parse('Regions.xml')
    root = tree.getroot()
    # print('root-tag:',root.tag,',root-attrib:',root.attrib,',root-text:',root.text)
    for child in root:
        region = Regions()
        region.code_region = child.find('code_region').text
        region.nom_region = child.find('nom_region').text
        region.nb_arrondi = child.find('nb_arrondi').text
        region.nb_canton = child.find('nb_canton').text
        region.nb_commune = child.find('nb_commune').text
        region.population_municpale = child.find('population_municpale').text
        region.population_totale = child.find('population_totale').text
        session.add(region)
    session.commit()


def addNouvellesRegions():


    # with open('data_Base_de_donnees/regions.csv', newline='', encoding = 'ISO-8859-1') as csvfile:
        # count = 0;
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            count += 1;
            if count > 8:
                print(row)
                region = Regions()
                region.code_region = row[0]
                region.nom_region = row[1]
                region.nb_arrondi = row[2].replace(' ', '')
                region.nb_canton = row[3].replace(' ', '')
                region.nb_commune = row[4].replace(' ', '')
                region.population_municpale = row[5].replace(' ', '')
                region.population_totale = row[6].replace(' ', '')
                session.add(region)
        session.commit()

# xml_to_database()
# trouverMemeNom()
# comparerPopulations()

# session.add(ed_user)
#
# with open(ndata_Base_de_donnees/omFichier, "r") as fic:
#     print(fic.read())
