import sys

nomFichier = ''

while True:

    print("-------------Bonjour!--------------")
    print("1. Choisir un nom de fichier!")
    print("2. Ajouter un texte!")
    print("3. Afficher le fichier complet!")
    print("4. Vider le fichier!")
    print("5. Quitter le programme")
    print("-----------------------------------")

    choix = input("Votre choix: ")

    if choix == "1":
        nomFichier = input("Nom de fichier:")
        print(nomFichier)

    elif choix == "2":
        if not nomFichier:
            print("Ce fichier n'exite pas, veuillez vous choisir d'autre.")
        else:
            with open(nomFichier, "a") as fic:
                text = input("Votre texte")
                fic.write(text);

    elif choix == "3":
        with open(nomFichier, "r") as fic:
            print(fic.read())

    elif choix == "4":
        open(nomFichier, "w+")
        # fic.truncate();
    elif choix == "5":
        sys.exit()
    else:
        pass


# with open("fichetu.csv", "r") as fic:
#     print(fic.read())
