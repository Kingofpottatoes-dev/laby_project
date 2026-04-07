# à vous de choisir la classe graph
class Graphe:
    def __init__(self):
        self.adj = {}  # dictionnaire : sommet -> liste des voisins

    def adds(self, s):
        if s not in self.adj:
            self.adj[s] = []

    def adda(self, u, v, oriente=False):
        self.adds(u)
        self.adds(v)
        
        self.adj[u].append(v)
        if not oriente:
            self.adj[v].append(u)

    def afficher(self):
        for sommet in self.adj:
            print(sommet, "->", self.adj[sommet])