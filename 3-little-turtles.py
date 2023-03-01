# ======================= draw half a rectangle:
import turtle

wn = turtle.Screen() # the screen where the turtles will run
alex = turtle.Turtle() # create a turtle named alex

alex.forward(50) # tell alex to move forward by 50 units
alex.left(90) # turn by 90 degrees
alex.forward(30)  # complete the second side of a rectangle

wn.mainloop()   # wait for a user click on the canvas

# ========================= add some attributes:

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen") # set the window background color
wn.title("Hello, Tess!") # set the window title

tess = turtle.Turtle()
tess.color("blue") # tell tess to change her color
tess.pensize(3) # tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()

# ========================= instances - many turtles:

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("tess & alex")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()

# ========================= for loop - draw a square:

for i in range(4):
    tess.forward(80)
    tess.left(90)


# ========================= for loop - multi color square:

colors = ["yellow", "red", "purple", "blue"]
for color in colors:
    tess.color(color)
    tess.forward(50)
    tess.left(90)

# ========================= move the turtle without a line:

alex.penup()
alex.forward(50)
alex.pendown()

# ========================= change the shape of the turtle:
alex.shape("turtle")

# ========================= change the speed of the turtle:
alex.speed(1) # 0 means turn off the animation

# ========================= turtle stamp:

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("tess & alex")

tess = turtle.Turtle()

tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20

for i in range(30):
  tess.stamp()
  size += 3
  tess.forward(size)
  tess.right(24)

wn.mainloop()