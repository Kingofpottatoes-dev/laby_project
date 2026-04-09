"programme principal"
from parcoursRecursif import *
from module_graph import *
from module_pile_file import *
from module_turtle import *
def BFS(g,source):
    p=File()
    vus={source}
    lst=[]
    p.enfiler(source)
    while not p.est_vide():
        u=p.defiler()
        lst.append(u)
        print(u)
        for v in g.voisins(u):
            if v not in vus:
                p.enfiler(v)
                vus.add(v)
    return lst
def PlusCourtChemin(g,u,s,vus=None):
    if vus is None:#si c le depart
        vus=set()
    if u==s:#si c la sortie
        return [u]
    vus.add(u)
    min_chemin=None
    for v in g.voisins(u):
        if v not in vus:
            chemin_v=PlusCourtChemin(g,v,s,vus)
            if chemin_v:
                chemin_v+=[v]
                if min_chemin:
                    if len(chemin_v)<len(min_chemin):
                        min_chemin=chemin_v
                else:
                    min_chemin=chemin_v
    return min_chemin
def showParcours(laby, vus, cote, nli, ncol):
    showLabyrinthe(laby, cote, nli, ncol)
    t.color("red")
    t.penup()
    for (i, j) in vus:
        t.goto(j*cote-100-cote/2,-i*cote+100+cote/2)
        t.dot(12)
    t.done()
laby=labyrinthe
print(BFS(laby,(1,1)))

showParcours(laby,PlusCourtChemin(laby,(1,1),(2,6)),50,4,8)