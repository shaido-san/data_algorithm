import turtle

def koch(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch(t, length, level-1)
        t.left(60)
        koch(t, length, level-1)
        t.right(120)
        koch(t, length, level-1)
        t.left(60)
        koch(t, length, level-1)

t = turtle.Turtle()
t.speed(0)
koch(t, 300, 4)
turtle.done()