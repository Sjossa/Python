class Payement:
    def __init__(self, order):
        self.order = order

    def calculer_solo(self):
        total = 0
        for boison in self.order.multipleboisson:
            total += boison.get_prix(0)
        return total





