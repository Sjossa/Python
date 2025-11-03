# oop
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soustraction(self, autre_vecteur):

        x_resultat = self.x - autre_vecteur.x
        y_resultat = self.y - autre_vecteur.y

        return Vector2D(x_resultat, y_resultat)

    def scalaire(self, autre_vecteur):

        return self.x * autre_vecteur.x + self.y * autre_vecteur.y


class Player:
    def __init__(self, nom, position, direction):

        self.nom = nom
        self.position = position
        self.direction = direction

    def is_visible(self, other):

        vecteur_separe = other.position.soustraction(self.position)

        result = self.direction.scalaire(vecteur_separe)

        return result > 0


pos1 = Vector2D(0, 0)
dir1 = Vector2D(1, 0)
joueur1 = Player("Alice", pos1, dir1)

pos2 = Vector2D(5, 0)
dir2 = Vector2D(-1, 0)
joueur2 = Player("Bob", pos2, dir2)

print(joueur1.is_visible(joueur2))
print(joueur2.is_visible(joueur1))
