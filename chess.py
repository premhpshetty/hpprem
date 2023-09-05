import turtle
p=turtle.Turtle()
def sqr():
    for i in range(4):
        p.forward(40)
        p.right(90)
    p.forward(40)

for i in range(8):
    p.penup()
    p.goto(0, 40*i)
    p.pendown()

    for j in range(8):
        if (i+j) % 2 == 0:
            color = "black"
        else:
            color = "white"

        p.fillcolor(color)
        p.begin_fill()
        sqr()
        p.end_fill()        