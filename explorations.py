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
"""def PlusCourtChemin(g,u,s,vus=None):
    Fonctionne mais pas opti
    if vus is None:#si c le depart
        vus=set()
    if u==s:#si c la sortie
        return [u]
    vus=vus | {u}#evite de bloquer des possiblité aux autres chemins
    min_chemin=None
    for v in g.voisins(u):
        if v not in vus:
            chemin_v=PlusCourtChemin(g,v,s,vus)
            if chemin_v:
                chemin= [u] + chemin_v
                if min_chemin is None or len(chemin)<len(min_chemin):
                    min_chemin=chemin
    return min_chemin"""
def PlusCourtChemin(g,u,s):#parcours en largeur
    p=File()
    vus={u}
    p.enfiler((u,[u]))#on met u et le chemin pour y arriver dans la file
    while not p.est_vide():
        u,chemin=p.defiler()
        if u==s:#si c la sortie
            return chemin
        for v in g.voisins(u):#sinon on explore les voisins
            if v not in vus:
                vus.add(v)
                p.enfiler((v,chemin+[v]))
    return None

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

showParcours(laby,PlusCourtChemin(laby,(1,1),(4,8)),50,4,8)