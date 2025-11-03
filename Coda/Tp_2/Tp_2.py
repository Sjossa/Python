class Voiture:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        self.abs = 0
        self.boite_automatique = 0
        self.toi_ouvrant = 0

    def options(self):
        print("Choisissez vos options :")
        choix_abs = input("ABS (oui/non) : ").lower()
        if choix_abs == "oui":
            self.abs = 3000

        choix_boite = input("Boîte automatique (oui/non) : ").lower()
        if choix_boite == "oui":
            self.boite_automatique = 10000

        choix_toit = input("Toit ouvrant (oui/non) : ").lower()
        if choix_toit == "oui":
            self.toi_ouvrant = (self.prix * 0.1) + 5000

    def prix_total(self):
        return self.prix + self.abs + self.boite_automatique + self.toi_ouvrant


choix_voiture = input("veuillez choisir votre voiture")
choix_prix = input("veuillez indiquer son pris de depart")

ma_voiture = Voiture(choix_voiture, choix_prix)
ma_voiture.options()
print(f"Prix total : {ma_voiture.prix_total()} €")
