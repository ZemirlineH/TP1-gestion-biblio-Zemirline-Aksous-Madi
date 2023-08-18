from Adherant import Adherant
import Document as Doc
import os

liste_de_choix = ('1', '2', '3', '4', '5', '6' , '7' , '8' , '9' )

class Biblio:
    __liste_Adherants = []
    def menu():
        loop = True
        while loop == True:
            print("*****************************************")
            print("Bienvenue a votre Bibilothéque")
            print("Faite votre choix")
            print(" 1 - Ajouter un Adhérant ")
            print(" 2 - Supprimer un adhérant ")
            print(" 3 - Afficher tous les adhérants")
            print(" 4 - Ajouter un document")
            print(" 5 - Suprimer un document")
            print(" 6 - Afficher tous les documents")
            print(" 7 - Ajouter un emprunt")
            print(" 8 - Retour d'un emprunt")
            print(" 9 - Afficher tous les emprunts")
            print(" Q - Quitter")
            print("*****************************************")
            choix = input("Choisissez une action: \n")
            if choix == 'Q' or choix == 'q':
                print("Fin du programme")
                break
            else:
                if choix in liste_de_choix:
                    print("choix correct")
                    loop = False
                else:
                    print('\n Saisie incorrect'.format(choix))
                    loop = True
        # executer la methode choisie par l'utilisateur
        if choix == '1':
            Biblio.ajouter_adherant()
        elif choix == '2':
            Biblio.supprimer_adherant()
        elif choix == '3':
            Biblio.afficher_liste_adherants()
            choix = input("Voulez vous retournez au menu principale ?, Taper Y pour revenir au menu principal, ou autre chose pour sortir: \n " )
            if choix == "Y" or choix == "y":
                Biblio.menu()
            else:
                print("Fin du programme")
                exit()
        elif choix == '4':
            Biblio.ajouter_document()
        elif choix == '5':
            Biblio.supprimer_document()
        elif choix == '6':
            Biblio.liste_documets()
        elif choix == '7':
            Emprunt.ajouter_emprunt()
        elif choix == '8':
            Emprunt.retour_emprunt()
        elif choix == '9':
            Emprunt.liste_emprunts()

    def ajouter_adherant():
        liste_Adherants = []
        print("--Ajouter un adhérant --")
        val = 0
        while val == 0:
            nom = input("saisir le nom de l'adhérant: ")
            prenom = input ("Saisir le prenom de l'adhérant: ")
            num_adherant = input ("Saisir le numero de l'adhérant: ")
            nouv_adherant = Adherant(num_adherant, nom, prenom)
            liste_Adherants.append(nouv_adherant)
            #Biblio.__liste_Adherants.append(nouv_adherant)
            print("--------------------------------------")
            check = input("Voulez vous ajouter un autre adhérant ? tapez Y pour ajouter un autre adherant, tapez autre chose pour revenir au menu pricipale\n")
            if check == "Y" or check == "y":
                val = 0
            else:
                val = 1
                try:

                    with  open(os.getcwd() + "\donnee\liste_adherant.txt", "a") as fichier:
                        if len(liste_Adherants) > 0 :
                            for adherent in liste_Adherants:
                                contenu = adherent.get_num_adherant() + ";" + adherent.get_nom_adherant() + ";" + adherent.get_prenom_adherant()
                                fichier.write(contenu)
                                fichier.write("\n")

                except IOError as e:
                    print("erreur lors de l'ecriture dans le fichier:", e)

        Biblio.menu()

    def supprimer_adherant(self):
        print("Supprimer un adhérant:")
        val = "y"
        liste_Adherants = []
        try:
            with open (os.getcwd() + "\donnee\liste_adherant.txt", "r") as fichier:
                for ligne in fichier:
                    liste_Adherants.append(ligne)
        except FileNotFoundError:
            print("Le fichier est introuvable.")



        while val == "y" or val == "Y":
            num = input("Saisir le numero de l'adhérant a supprimer : \n")
            adherant_trouve = False
            for x in self.__liste_Adherants:
                print("ok")
                if Adherant.get_num_adherant() == num:
                    adherant_trouve = True
                    print(f"L'adhérent {Adherant.get_nom_adherant()} {Adherant.get_prenom_adherant()} a été supprimé avec succès.")
                    Biblio.__liste_Adherants.remove(adherant)
                    Biblio.menu()
                if adherant_trouve == False:
                    print("Adhérant non trouvé avec ce numéro")
                    val = input("taper y pour saisir un autre numéro, ou q pour revenir au menu principal : \n")
                    if val == "q" or val == "Q":
                        Biblio.menu()
            print("Nok")

    def afficher_liste_adherants():
        fichier = open(os.getcwd() + "\donnee\liste_adherant.txt", "r")
        contenu = fichier.read()
        print("La liste de tous les Adherants ;\n " +  contenu)
        contenu = fichier.close()
        print("************************************************")

    def ajouter_document():
        liste_journal = []
        liste_de_choix = ('1', '2', '3', '4')
        print("Ajouter un Document:")
        loop = True
        while loop == True:
            print(" 1 - Ajouter un Journal")
            print(" 2 - Ajouter un Livre ")
            print(" 3 - Ajouter un dictionnaire")
            print(" 4 - Ajouter une bande dessinée")
            print("*****************************************")
            choix = input("Choisissez une action: \n")
            if choix in liste_de_choix:
                loop = False
            else:
                print('\n Saisie incorrect'.format(choix))
                loop = True
            if choix == '1':
                code = input("Saisir le code du Journal:\n")
                titre = input("Saisir le titre du journal: ")
                document = Doc(code, titre)
                date = input("Entrer la date: ")
                journal = Doc.Journal(document, date)
                liste_journal.append(journal)
                fichier = open(os.getcwd() + "\donnee\liste_Documents.txt", "a")
                fichier.write(liste_journal)
                fichier.close()

            if choix == '2':
                liste_livres = []
                code = input("Saisir le code du livre:\n")
                titre = input("Entrer le titre du livre: ")
                document = Doc.Document(code, titre)
                auteur = input("Entrer le nom de l'auteur: ")
                volume = Doc.Volume(document, auteur)
                livre = Doc.Livre(volume, True)
                liste_livres.append(livre)
                fichier = open(os.getcwd() + "\donnee\liste_Documents.txt", "a")
                fichier.write(liste_livres)
                fichier.close()

            if choix == '3':
                liste_dictionnaire = []
                code = input("Saisir le code du dictionnaire:\n")
                titre = input("Entrer le titre du dictionnaire:\n ")
                document = Doc.Document(code, titre)
                auteur = input("Entrer le nom de l'auteur: ")
                volume = Doc.Volume(document, auteur)
                dictionnaire = Doc.Dictionnaire(volume)
                liste_dictionnaire.append(dictionnaire)
                fichier = open(os.getcwd() + "\donnee\liste_dictionnaire.txt", "a")
                fichier.write(liste_dictionnaire)
                fichier.close()

            if choix == '4':
                liste_BD = []
                code = input("Saisir le code de la bande dessinée:\n")
                titre = input("Entrer le titre de la bande dessinée:\n ")
                document = Doc.Document (code, titre)
                auteur = input("Entrer le nom de l'auteur: ")
                volume = Doc.Volume(document, auteur)
                BD = Doc.Dictionnaire(volume)
                liste_BD.append(BD)
                fichier = open(os.getcwd() + "\donnee\lliste_BD.txt", "a")
                fichier.write(liste_BD)
                fichier.close()








    def get_liste_adherants(self):
        return self.__liste_Adherants

    def get_liste_livres(self):
        return self.__liste_livres

    def get_liste_emprunts(self):
        return self.__liste_emprunts

    def enlever_adherant(self, adherant):
        pass

    def liste_Adherants(self):
        pass

    def ajouter_document(self, document):
        pass
    def supprimer_document(self, document):
        pass
    def liste_documets(self):
        pass
Biblio.menu()

