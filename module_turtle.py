import turtle as t

def showLabyrinthe(labyrinthe,cote,nli,ncol):
    """fonction qui trace le labyrinthe"""
    t.speed(20)
    cadre(nli,ncol,cote)
    paroiesVerticales(labyrinthe,nli,ncol,cote)
    paroiesHorizontales(labyrinthe,nli,ncol,cote)
    t.hideturtle()
    t.done()

def cadre(nli,ncol,cote):
    """ fonction qui trace les parois externes"""
    t.up()
    t.goto(-100,100)
    t.down()
    #dessin parois extérieures

    for _ in range(2):
        for i in range(ncol):
            t.forward(cote)
        t.right(90)
        for i in range(nli):
            t.forward(cote)
        t.right(90)

def paroiesVerticales(labyrinthe,nli,ncol,dist):
    """ fonction qui trace les parois internes verticales"""

    for i in range(1,nli+1):
        for j in range(1,ncol) :
            dess=(i,j+1) not in labyrinthe.adj[(i,j)]
            if dess :
                t.up()
                t.forward(dist)
                t.down()
                t.right(90)
                t.forward(dist)
                t.backward(dist)
                t.left(90)
            else :
                t.up()
                t.forward(dist)

        t.up()
        t.goto(-100,100)
        t.right(90)
        t.forward(dist*i)
        t.left(90)
        
        
def paroiesHorizontales(labyrinthe,nli,ncol,cote):
    """ fonction qui trace les parois internes horizontales"""
    t.up()
    t.goto(-100,100-cote)
    for i in range(1,nli):
        for j in range(1,ncol) :
            dess=(i+1,j) not in labyrinthe.adj[(i,j)]
            if dess :
                t.down()
                t.forward(cote)
            else :
                t.up()
                t.forward(cote)

        t.up()
        t.goto(-100,100-cote*(i+1))
