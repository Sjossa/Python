fruits = {}
fruits["pomme"] = "rouge"
fruits["banane"] = "jaune"
fruits["orange"] = "orange"
fruits["kiwi"] = "vert"

print (f"{fruits}")

couleur_banane =  fruits.get("banane")

print (f"{couleur_banane}")

fruits["pomme"] = "vert"

print (f"{fruits}")

fruits.pop("banane")
print (f"{fruits}")

print(fruits.keys())





