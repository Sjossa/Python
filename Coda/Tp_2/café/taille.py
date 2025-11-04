class TailleBoison:
    def __init__(self, taille: str):
        self.taille = taille


class tailleS(TailleBoison):

    def __init__(self, taille):
        super().__init__("S")


class tailleM(TailleBoison):

    def __init__(self, taille):
        super().__init__("M")


class tailleL(TailleBoison):

    def __init__(self, taille):
        super().__init__("L")
