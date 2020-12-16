import turtle
from   turtle import Screen

tl = turtle.Turtle()
Screen().setup(height=1.0,width=1.0)


def flocon(n,l):
    if n == 0:
        tl.forward(l)
        return
    l /=3
    flocon(n-1,l)
    tl.left(60)
    flocon(n-1,l)
    tl.right(120)
    flocon(n-1,l)
    tl.left(60)
    flocon(n-1,l)
def lancer():
    for i in range(3):
        flocon(4,500)
        tl.right(120)
lancer()
tl.mainloop()
