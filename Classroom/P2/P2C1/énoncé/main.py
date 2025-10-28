nombre1 = input("entrez un nombre\n")
nombre2 = input("entrez un nombre\n")

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    methode = input("choisisez la methode de calcul entre : (+, -, * ou /)\n")
    match methode:
        case "+":
            resultat = nombre1 + nombre2
            print(f"{resultat}")
        case "-":
            resultat = nombre1 - nombre2
            print(f"{resultat}")
        case "*":
            resultat = nombre1 * nombre2
            print(f"{resultat}")
        case "/":
            if nombre2 == 0:
                print("impossible de diviser par zero ")

            else:
                resultat = nombre1 / nombre2
                print(f"{resultat.__round__()}")
        case _:
            print("vous avez entrer un mauvaus charactere")
else:
    raise ValueError("Les valeurs entrées ne sont pas des nombres")
