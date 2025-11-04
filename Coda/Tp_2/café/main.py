from user import *
from Order import *


user = User()
boisson = user.choisir_boisson()
order = Order([])
order.ajouter_boisson(boisson)

