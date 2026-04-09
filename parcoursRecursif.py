def import_labyrinthe(nom_fichier):
    """ fonction qui prend en entrée un fichier txt
    et qui renvoie une liste représentant le labyrinthe"""
    with open(nom_fichier) as f:
        laby=[]
        for ligne in f:
            lst=[]
            for c in ligne:
                if c != '\n':
                    if c == ' ':
                        lst.append('')
                    else:
                        lst.append(c)
            laby.append(lst)#on transforme le labyrinthe en une liste de listes de caractères
    return laby
# test de la fonction
labyrinthe = import_labyrinthe("laby1.txt")
assert labyrinthe == [['X', 'X', 'X', 'X', 'X'],\
                        ['X', '', 'X', '', 'S'],\
                        ['X', '', '', '', 'X'],\
                        ['X', 'E', 'X', '', 'X'],\
                        ['X', '', 'X', '', 'X'],\
                        ['X', 'X', 'X', 'X', 'X']]
def depart(tab) :
    """ fonction qui prend en entrée une liste et
    renvoie les indices i et j du caractère E"""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 'E': #si c le depart on arrete
                return (i,j)
# test de la fonction
i0, j0 = depart(labyrinthe)
assert (i0,j0)== (3,1)
def afficher_labyrinthe(tab):
    """fonction qui prend en entrée une liste
    et l'affiche sur la console"""
    for l in tab:
        for c in l:#on affiche
            if c == '':
                print(' ', end='')
            else:
                print(c, end='')
        print()
def deplacer_vers(i,j, case):
    """fonction récursive d'exploration qui marche pas jsp prk"""
    if i<0 or i>=len(case) or j<0 or j>=len(case[0]) or case[i][j]=="X" or case[i][j]=='.':
        return #si on sort du labyrinthe ou si c un mur ou une case déjà visitée on arrete
    if case[i][j] == 'S':#si c la sortie on affiche
        print("Solution trouvée")
        afficher_labyrinthe(case)
    if case[i][j]=="E" or case[i][j]==" ":
        case[i][j] = '.' # on marque la case comme visitée
        deplacer_vers(i-1, j, case)
        deplacer_vers(i+1, j, case)#et on explore les cases voisines
        deplacer_vers(i, j-1, case)
        deplacer_vers(i, j+1, case)
        case[i][j] = " "#on efface apres l'exploration pour permettre d'autres chemins
# programme principal
deplacer_vers(i0,j0,labyrinthe) # on lance l'exploration à partir de E