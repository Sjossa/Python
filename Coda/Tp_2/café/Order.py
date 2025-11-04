class Order:
    def __init__(self, multipleboisson):
        self.multipleboisson = []

    def ajouter_boisson(self, boisson):
        self.multipleboisson.append(boisson)

        if len(self.multipleboisson) == 1:


