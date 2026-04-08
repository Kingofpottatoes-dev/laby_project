"programme principal"
from parcoursRecursif import *
from module_graph import *
from module_pile_file import *
from module_turtle import *
def BFS(g,source):
    p=Pile()
    vus=set()
    p.empiler(source)
    while not p.est_vide():
        u=p.depiler(p)
        print(u)
        for v in g.voisins(u):
            if v not in vus:
                p.empiler(v)
                v.add(v)

laby=labyrinthe


showLabyrinthe(laby,50,4,8)