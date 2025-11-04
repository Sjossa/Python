from taille import tailleL, tailleM, tailleS
from Boisson import Cafe, ChocolaChaud, The, Mocha
from Topping import Caramel, CoulisChocolat, Mocha2

taille_mapping = {"S": tailleS("S"), "M": tailleM("M"), "L": tailleL("L")}


class User:
    def __init__(self):
        pass

    def choisir_boisson(self):
        choix_boisson = input(
            "Choisissez votre boisson entre : café, thé, mocha, chocolat chaud\n"
        ).lower()

        choix_taille = input("Quelle taille voulez-vous ? (S, M, L) : ").upper()

        if choix_taille not in taille_mapping:
            print("Taille invalide !")
            return None

        objet_taille = taille_mapping[choix_taille]

        if choix_boisson == "café":
            return Cafe(objet_taille)
        elif choix_boisson == "thé":
            return The(objet_taille)
        elif choix_boisson == "mocha":
            return Mocha(objet_taille)
        elif choix_boisson == "chocolat chaud":
            return ChocolaChaud(objet_taille)
        else:
            print("Boisson invalide !")
            return None

    def choisir_topping(self):
        choix_utilisateur = input(
            "Choisissez votre topping entre : caramel, Coulis_Chocolat, mocha,Chantily\n"
        ).lower()
        return ToppingFactory.choix(choix_utilisateur)


class ToppingFactory:
    @staticmethod
    def choix(type):
        if type == "caramel":
            return Caramel()
        elif type == "coulis chocolat":
            return CoulisChocolat()
        elif type == "mocha":
            return Mocha2()
        # elif type == "chantilly":
        #     return Chantilly()
