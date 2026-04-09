from parcoursRecursif import *
from module_graph import *
from module_pile_file import *
from module_turtle import *
def load_txt_as_graph(filename):
    G = Graphe()

    with open(filename) as f:
        lignes = f.read().splitlines()
    for i in range(len(lignes)):
        for j in range(len(lignes[0])):
            if lignes[i][j] != 'X':
                G.adds((i, j))
                if lignes[i][j] == 'E':
                    source = (i, j)
                if lignes[i][j] == 'S':
                    destination = (i, j)
    for i in range(len(lignes)):
        for j in range(len(lignes[0])):
            if lignes[i][j] == 'X':
                continue
            # haut
            if i > 0 and lignes[i-1][j] != 'X':
                G.adda((i, j), (i-1, j))
            # bas
            if i < len(lignes)-1 and lignes[i+1][j] != 'X':
                G.adda((i, j), (i+1, j))
            # gauche
            if j > 0 and lignes[i][j-1] != 'X':
                G.adda((i, j), (i, j-1))
            # droite
            if j < len(lignes[0])-1 and lignes[i][j+1] != 'X':
                G.adda((i, j), (i, j+1))
    return G, source, destination
labyrinthe, depart, arrivee = load_txt_as_graph("laby2.txt")
showLabyrinthe(labyrinthe, 20, 10, 26)