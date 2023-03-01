#keypress events:

import turtle 

turtle.setup(400,500)				# Determine the window size
wn = turtle.Screen()				# Get a reference to the window
wn.title("Handling keypresses!")	# Change the window title
wn.bgcolor("lightgreen")			# Set the background color
tess = turtle.Turtle()				# Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()	# Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.listen()			# Listen for events
wn.mainloop()

# mouseclick events:

import turtle

turtle.setup(400,500)				# Determine the window size
wn = turtle.Screen()				# Get a reference to the window
wn.title("Handling mouse clicks!")	# Change the window title
wn.bgcolor("lightgreen")			# Set the background color

tess = turtle.Turtle()				# Create two turtles
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
    wn.title("Got click at coords {0}, {1}".format(x, y))
    tess.goto(x, y)

wn.onclick(h1)			# Wire up a click on the window.
wn.mainloop()

# automatic events from timer:

import turtle

turtle.setup(400,500)				# Determine the window size
wn = turtle.Screen()				# Get a reference to the window
wn.title("Handling mouse clicks!")	# Change the window title
wn.bgcolor("lightgreen")			# Set the background color

tess = turtle.Turtle()				# Create two turtles
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)

wn.ontimer(h1, 2000)			# Wire up a timer
wn.mainloop()

