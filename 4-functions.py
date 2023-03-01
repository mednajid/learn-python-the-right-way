import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex, 50)

wn.mainloop()


# ========================= docstring:

import turtle

def draw_multicolor_square(t, sz):
    #this is a docstring and it is a comment and very useful in documentation
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

size = 20

for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.mainloop()

# ========================= draw a square using rectangle:
def draw_rectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(t, sz):
    draw_rectangle(t, sz, sz)

# the flow of execution:
# we can define a function inside of another function so that the inner function is only available after calling the outer function

# a function that returns a value is caled fruitful function
# the oposite is called void function / or a procedure

# python always returns a value, if you don't specify a return value, it returns None

#ex: fruitful function - coumpound interest:
def compound_interest(p, r, n, t):
    """ Return the amount of money you have after n years of compound interest."""
    a = p * (1 + r/n) ** (n*t)
    return a

total_invest = float(input("How much money do you want to invest? "))
fnl = compound_interest(total_invest, 0.08, 12, 5)
print("at the end of the period you will have ${0:.2f}".format(fnl))

# local variables:
#if we try to acess a local variable outside of the function, we get an error
# a only exists while the function is running -- lifetime
# the same is true for parameters

# use fruitful functions:

def make_windows(color, ttle):
    """Set up the window with the given background color and title."""
    wn = turtle.Screen()
    wn.bgcolor(color)
    wn.title(ttle)
    return wn

def make_turtle(color, size):
    """Set up a turtle with the given color and pensize."""
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

wn = make_windows("lightgreen", "Tess & Alex")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("blue", 3)


