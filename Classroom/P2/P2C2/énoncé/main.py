nombres = input("Veuillez entrer une liste de nombres séparés par des virgules : ")
liste = nombres.split(",")

liste_entier = []

x = 0
while x < len(liste):
    liste_entier.append(int(liste[x]))
    x += 1


somme = 0
i = 0
while i < len(liste_entier):
    somme = somme + liste_entier[i]
    i += 1

print(somme)

moyenne = somme / len(liste_entier)

print(f"la moyenne est de {moyenne}")


