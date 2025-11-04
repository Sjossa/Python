class Coffe:
    def __init__(self, name: str, prix: int):
        self.name = name
        self.prix = prix


class Boisson:
    def __init__(self, nom: str, Taille_Boison):
        self.nom = nom
        self.taille = Taille_Boison

    def get_nom(self) -> str:
        return self.nom

    def get_prix(self, prix_base) -> float:
        return 0.0


class Cafe(Boisson):
    prix_par_taille = {"S": 1.0, "M": 1.50, "L": 2.0}

    def __init__(self, Taille_Boison):
        super().__init__("café", Taille_Boison)

    def get_prix(self, prix_base: float) -> float:
        prix = self.prix_par_taille[self.taille.taille]

        return prix


class The(Boisson):

    prix_par_taille = {"S": 2.0, "M": 2.50, "L": 3.0}

    def __init__(self, Taille_Boison):
        super().__init__("the", Taille_Boison)

    def get_prix(self, prix_base: float) -> float:
        prix = self.prix_par_taille[self.taille.taille]

        return prix


class Mocha(Boisson):

    prix_par_taille = {"S": 5, "M": 6.50, "L": 7.50}

    def __init__(self, Taille_Boison):
        super().__init__("mocha", Taille_Boison)

    def get_prix(self, prix_base):
        prix = self.prix_par_taille[self.taille.taille]

        return prix


class ChocolaChaud(Boisson):
    prix_par_taille = {"S": 3, "M": 4, "L": 5}

    def __init__(self, Taille_Boison):
        super().__init__("chocolat_chaud", Taille_Boison)

    def get_prix(self, prix_base):

        prix = self.prix_par_taille[self.taille.taille]

        return prix
