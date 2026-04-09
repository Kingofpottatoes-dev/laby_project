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
    def voisins(self,s):
        return self.adj[s]
    def afficher(self):
        for sommet in self.adj:
            print(sommet, "->", self.adj[sommet])
labyrinthe = Graphe()
for i in range(1,5):
    for j in range(1,9):
        labyrinthe.adds((i,j))

labyrinthe.adda((1,1),(2,1))
labyrinthe.adda((2,1),(2,2))
labyrinthe.adda((2,2),(2,3))
labyrinthe.adda((2,2),(3,2))
labyrinthe.adda((3,2),(4,2))
labyrinthe.adda((4,2),(4,3))
labyrinthe.adda((4,3),(4,4))
labyrinthe.adda((2,3),(1,3))
labyrinthe.adda((1,3),(1,4))
labyrinthe.adda((1,4),(1,5))
labyrinthe.adda((1,4),(2,4))
labyrinthe.adda((2,4),(3,4))
labyrinthe.adda((3,4),(3,5))
labyrinthe.adda((1,5),(2,5))
labyrinthe.adda((2,5),(2,6))
labyrinthe.adda((3,5),(3,6))
labyrinthe.adda((4,5),(4,6))
labyrinthe.adda((1,6),(2,6))
labyrinthe.adda((2,6),(3,6))
labyrinthe.adda((3,6),(4,6))
labyrinthe.adda((1,6),(1,7))
labyrinthe.adda((2,6),(2,7))
labyrinthe.adda((3,6),(3,7))
labyrinthe.adda((3,7),(2,7))
labyrinthe.adda((3,7),(4,7))
labyrinthe.adda((1,7),(1,8))
labyrinthe.adda((4,7),(4,8))
labyrinthe.adda((1,8),(2,8))
labyrinthe.adda((3,8),(2,8))
labyrinthe.adda((3,8),(4,8))