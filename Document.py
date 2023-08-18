class Document:
    def __init__(self, code, titre):
        self.__code = code
        self.__titre = titre
    def get_code_document(self):
        return self.__code
    def get_titre_document(self):
        return self.__titre

class Volume(Document):
    def __init__(self, document, auteur):
        super().__init__(document.get_code_document(), Document.get_titre_document())
        self.__auteur = auteur
    def get_auteur(self):
        return self.__auteur

class Journal(Document):
    def __init__(self, document, date_parution):
        super().__init__(document.get_code_document(), document.get_titre())
        self.__date_parution = date_parution
        self.__type = "Journal"
    def get_type(self):
        return self.__type

    def get_date(self):
        return self.__dateParution

class Livre(Volume):
    def __init__(self, titre, auteur, disponible):
        super().__init__(auteur)
        super().__init__(titre)
        self.disponible = disponible(bool)

    def empuntable(self, titre):
        if self.disponible :
            return "[le Livre :" + self.titre + " est empruntable ]"
        else:
            return "[le Livre :" + self.titre + " est non empruntable ]"

class BD(Volume):
    def __init__(self,volume, dessinateur):
        super().__init__(volume, volume.get_auteur())
        self.__dessinateur = dessinateur
        self.__type = "bande_dessinée"

    def get_dessinateur(self):
        return self.__dessinateur
    def get_type(self):
        return self.__type


class Dictionnaire(Volume):
    def __init__(self, volume):
        super().__init__(volume, Volume.get_auteur())
        self.__type = "Dictionnaire"
    def get_type(self):
        return self.__type





