class Voiture:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        self.option = []

    def ajout(self, option):
        self.option.append(option)

    def prix_total(self):
        prix_total = self.prix
        for opt in self.option:
            prix_total += opt.get_prix(self.prix)
        return prix_total


class Option:
    def __init__(self, nom: str):
        self.nom = nom

    def get_nom(self) -> str:
        return self.nom

    def get_prix(self, prix_base) -> float:
        return 0.0


class ABS(Option):
    def __init__(self):
        super().__init__("ABS")

    def get_prix(self, prix_base: float) -> float:
        return 3000.0


class BoiteAuto(Option):
    def __init__(self):
        super().__init__("Boîte automatique")

    def get_prix(self, prix_base: float) -> float:
        return prix_base * 0.10


class ToitOuvrant(Option):
    def __init__(self):
        super().__init__("Toit ouvrant")

    def get_prix(self, prix_base: float) -> float:
        return (prix_base * 0.10) + 5000


option = [ToitOuvrant, ABS, BoiteAuto]


class utulisateur:
    def __init__(self):

        nom_voiture = input("veuillez ecrire le nom de votre voiture\n")
        prix_voiture = input("maintenant sont prix \n")
        prix_voiture = float(prix_voiture)

        self.voiture = Voiture(nom_voiture, prix_voiture)

        choix = input("voulez-vous des option ? (oui/non)\n")
        i = 0
        if choix.lower() == "oui":
            while i < len(option):
                nom_option = option[i]().get_nom()
                reponse = input(f"Voulez-vous {nom_option} ? (oui/non\n) ")
                if reponse.lower() == "oui":
                    self.voiture.ajout(option[i]())

                i += 1
        print(f"Prix total : {self.voiture.prix_total()} €")


utulisateur()
