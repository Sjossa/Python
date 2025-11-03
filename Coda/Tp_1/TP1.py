# import random

# numbers = [1, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]


# somme = 0
# i = 0
# paire = []
# impaire = []
# multiplication = []
# while i < len(numbers):
#     somme = somme + numbers[i]

#     if numbers[i] % 2 == 0:
#         paire.append(numbers[i])
#     else:
#         impaire.append(numbers[i])

#     multiplication.append(numbers[i] * 2)

#     i += 1


# chiffre = list(range(0, 101))

# aleatoire = []

# aleatoire.append(random.sample(range(1, 100), 10))


# print(somme)
# print(paire)
# print(multiplication)


# print(chiffre)
# print(aleatoire)


# # sets

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}

# a.add(8)
# a.remove(2)

# if 3 in a:
#     print(a)
# else:
#     print("il n'y a pas trois ")


# if a != b:
#     print("erreur")


# numbers2 = [1, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

# set_numbers = set()

# i = 0

# while i < len(numbers2):

#     doublon = numbers2[i]

#     if doublon not in set_numbers:
#         set_numbers.add(doublon)
#     i += 1

# print(set_numbers)


# # dictionaire

# prices = {"apple": 1.5, "banana": 1.2, "orange": 2.0}

# print(f"{prices}")


# prices["rose"] = 3.5
# print(prices)


# print(sum(prices.values()))

# prices2 = {"apple": 1.5, "banana": 1.2, "orange": 2.0}
# cart = {"apple": 2, "banana": 3, "orange": 1}

# total = sum(prices2.values()) + sum(cart.values())

# print(total)

# sentence = "apple banana apple orange banana apple"

# mots = sentence.lower().split()
# occurrences = {}
# for mot in mots:
#     mot = mot.strip('.,!?";')
#     if mot in occurrences:
#         occurrences[mot] += 1
#     else:
#         occurrences[mot] = 1

# print(occurrences)


# # fonction


# def palindrome(mot):
#     mot = mot.lower()
#     if mot == mot[::-1]:
#         print(mot, " palindrome")
#     else:
#         print(mot, " palindrome")


# palindrome("axa")


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b


# fibonacci(100)



