from user import User
from Order import Order
from Payement import Payement


user = User()
boisson = user.choisir_boisson()
order = Order([])
order.ajouter_boisson(boisson)
ajouter_boison = input("voulez-vous ajoutez une boison ?")


while ajouter_boison == "oui":
    boisson = user.choisir_boisson()
    order.ajouter_boisson(boisson)
    ajouter_boison = input("voulez-vous ajoutez une boison ?")

ajout_toping = input("voulez-vous rajouter des topping ?")

while ajout_toping == "oui":
    toping = user.choisir_topping()
    order.ajouter_boisson(toping)
    ajout_toping = input("voulez-vous rajouter des topping ?")


paiement = Payement(order)
total = paiement.calculer_solo()
print(f"Le total de votre commande est de : {total} €")
