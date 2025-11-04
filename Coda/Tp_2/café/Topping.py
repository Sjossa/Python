class Topping:

    def __init__(self, name: str, prix: float):
        self.name = name
        self.prix = prix

    def get_prix(self, prix_base=0):
        return self.prix


class Caramel(Topping):
    def __init__(self):
        super().__init__("caramel", 0.5)


class CoulisChocolat(Topping):
    def __init__(self):
        super().__init__("Coulis_Chocolat", 1)


class Mocha2(Topping):

    def __init__(self):
        super().__init__("Mocha", 1)


class Chantilly(Topping):
    prix_par_taille = {"S": 0.5, "M": 1.5, "L": 1.5}

    def __init__(self, taille: str):
        prix = self.prix_par_taille[taille]
        super().__init__("chantilly", prix)

