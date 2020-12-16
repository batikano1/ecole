import turtle
from   turtle import Screen

tl = turtle.Turtle()
Screen().setup(height=1.0,width=1.0)


def arbre(n,l):
    if n == 0:
        return
    elif n != 0:
        tl.forward(l)
        tl.left(30)
        arbre(n-1,l/1.5)
        tl.right(60)
        arbre(n-1,l/1.5)
        tl.left(30)
        tl.backward(l)
arbre(10,100)
turtle.mainloop()
