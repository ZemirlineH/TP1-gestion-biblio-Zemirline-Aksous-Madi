class Document:
    def __init__(self, titre):
        self.titre = titre


class Livre(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        self.disponible = True
        print(f"Le livre '{self.titre}' a été rendu.")


class BandeDessinee(Document):
    def __init__(self, titre, dessinateur):
        super().__init__(titre)
        self.dessinateur = dessinateur


class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution


class Adherent:
    def __init__(self, nom):
        self.nom = nom


class Bibliotheque:
    def __init__(self):
        self.documents = []
        self.adherents = []

    def ajouter_document(self, document):
        self.documents.append(document)

    def enlever_document(self, document):
        if document in self.documents:
            self.documents.remove(document)

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)

    def emprunter_livre(self, adherent, livre):
        if livre in self.documents and isinstance(livre, Livre) and livre.disponible:
            livre.emprunter()
            print(f"{adherent.nom} a emprunté le livre '{livre.titre}'.")
        else:
            print(f"{adherent.nom} ne peut pas emprunter le livre '{livre.titre}'.")

    def rendre_livre(self, livre):
        if livre in self.documents and isinstance(livre, Livre) and not livre.disponible:
            livre.rendre()
        else:
            print(f"Le livre '{livre.titre}' ne peut pas être rendu.")


# Exemple d'utilisation
bibliotheque = Bibliotheque()

livre1 = Livre("Titre Livre 1", "Auteur 1")
livre2 = Livre("Titre Livre 2", "Auteur 2")
bd1 = BandeDessinee("Titre BD 1", "Dessinateur 1")
journal1 = Journal("Titre Journal 1", "01/08/2023")

bibliotheque.ajouter_document(livre1)
bibliotheque.ajouter_document(livre2)
bibliotheque.ajouter_document(bd1)
bibliotheque.ajouter_document(journal1)

adherent1 = Adherent("Adherent 1")
bibliotheque.ajouter_adherent(adherent1)

bibliotheque.emprunter_livre(adherent1, livre1)
bibliotheque.emprunter_livre(adherent1, bd1)
bibliotheque.rendre_livre(livre1)

