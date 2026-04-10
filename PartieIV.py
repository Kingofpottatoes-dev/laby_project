from parcoursRecursif import *
from module_graph import *
from module_pile_file import *
from module_turtle import *
from explorations import *
def load_txt_as_graph(filename):
    """charge le txt en graphe"""
    G = Graphe()

    with open(filename) as f:
        lignes = f.read().splitlines()
    for i in range(len(lignes)):
        for j in range(len(lignes[i])):
            G.adds((i,j))#on ajoute le sommet si il existe pas
            if lignes[i][j] == 'X':#pas de lien a mettre si c un mur
                continue
            if lignes[i][j] == 'E':
                source = (i, j)
            if lignes[i][j] == 'S':
                destination = (i, j)
            # haut
            if i > 0 and lignes[i-1][j] != 'X':#si le voisin du haut c pas un mur je le relie
                G.adda((i, j), (i-1, j))
            # bas
            if i < len(lignes)-1 and lignes[i+1][j] != 'X':#ext
                G.adda((i, j), (i+1, j))
            # gauche
            if j > 0 and lignes[i][j-1] != 'X':
                G.adda((i, j), (i, j-1))
            # droite
            if j < len(lignes[0])-1 and lignes[i][j+1] != 'X':
                G.adda((i, j), (i, j+1))

    return G, source, destination
labyrinthe, depart, arrivee = load_txt_as_graph("laby2.txt")
print(PlusCourtChemin(labyrinthe,(depart),(arrivee)))
print(labyrinthe.adj)
showParcours(labyrinthe,PlusCourtChemin(labyrinthe,(depart),(arrivee)), 15, 8, 23)