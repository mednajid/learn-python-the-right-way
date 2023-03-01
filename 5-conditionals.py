if True:
    pass # exec but does nithing
else:
    pass

# chained conditionals:
if True:
    pass
elif True:
    pass
else:
    pass

# each condition is checked but if one is true, the rest are not checked

import turtle

def draw_bare(t, height):
    """ Get turtle t to draw a bare tree of height """
    t.begin_fill() # start filling this shape
    t.left(90)
    t.forward(height)
    t.write("  " + str(height), font=("Arial", 16, "bold"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # stop filling this shape
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("darkgreen", "green")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:
    draw_bare(tess, a)

wn.mainloop()
