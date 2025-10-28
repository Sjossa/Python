def salaire_mensuel(salaire_annuel):

    salaire_mensuel = salaire_annuel / 12

    return salaire_mensuel


def salaire_hebdomadaire(salaire_mensuel):

    salaire_hebdomadaire = salaire_mensuel / 4

    return salaire_hebdomadaire


def salaire_horaire(salaire_hebdomadaire, heure_travaillees):
    salaire_horaire = salaire_hebdomadaire / heure_travaillees

    return salaire_horaire


user_anuel = input("saisisez votre salaire anuel \n")
user_heure = input("saisisez le nombre dh'eure travaillez en une semaine ")

user_anuel = float(user_anuel)
user_heure = float(user_heure)

mensuel = salaire_mensuel(user_anuel)

hebdo = salaire_hebdomadaire(mensuel)

horaire = salaire_horaire(hebdo, user_heure)
print(f"votre salaire mensuel est de {mensuel}")


print(f"votre salaire horaire est de {horaire}")
