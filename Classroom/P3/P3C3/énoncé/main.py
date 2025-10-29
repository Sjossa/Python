import csv

with open ('/Python/Classroom/P3/P3C3/énoncé/input.csv') as fichier_csv:
  reader = csv.DictReader(fichier_csv, delimiter=',')
  for ligne in reader:
    print(f"{ligne['nom']} travaille {ligne['heures_travaillees']}")


fichier = open("/Python/Classroom/P3/P3C3/énoncé/output.csv", "w")
fichier.write("Hello, world!")
fichier.close()

# if __name__ == "__main__":
#     main()
