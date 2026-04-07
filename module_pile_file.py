#à vous de choisir les classes piles et files
class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, x):
        self.elements.append(x)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        raise IndexError("Pile vide")

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]
        raise IndexError("Pile vide")

    def est_vide(self):
        return len(self.elements) == 0

    def taille(self):
        return len(self.elements)
class File:
    def __init__(self):
        from collections import deque
        self.elements = deque()

    def enfiler(self, x):
        self.elements.append(x)

    def defiler(self):
        if not self.est_vide():
            return self.elements.popleft()
        raise IndexError("File vide")

    def est_vide(self):
        return len(self.elements) == 0

    def taille(self):
        return len(self.elements)