"programme principal"
from parcoursRecursif import *
from module_graph import *
from module_pile_file import *
from module_turtle import *
laby=import_labyrinthe("laby2.txt")
G=Graphe()
for i in range(len(laby)):
    for j in range(len(laby[i])):
        G.adds((i,j))
        if i > 0 and laby[i-1][j] != 'X':
            G.adda((i,j),(i-1,j))
        if i < len(laby)-1 and laby[i+1][j] != 'X':
            G.adda((i,j),(i+1,j))
        if j > 0 and laby[i][j-1] != 'X':
            G.adda((i,j),(i,j-1))
        if j < len(laby[0])-1 and laby[i][j+1] != 'X':
            G.adda((i,j),(i,j+1))


showLabyrinthe(G,20,6,8)