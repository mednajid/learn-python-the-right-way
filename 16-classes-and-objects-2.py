from point import Point

class Rectangle:
    """A class to manufacture rectangle objects"""
    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h
    def __str__ (self): # print the rectangle
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

r = Rectangle(Point(0, 0), 10, 5)
bomb = Rectangle(Point(100, 80), 5, 10)
print(r)
print(bomb)

# bomb.corner.x means the x coordinate of the corner of the bomb

# objects are mutable

bomb.width = bomb.width + 50 # change the width of the bomb

# adding a method to change the position:

class Rectangle:
    """A class to manufacture rectangle objects"""
    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h
    def __str__ (self): # print the rectangle
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def grow(self, delta_width, delta_height):
        """Grow (or shrink) the rectangle by the deltas."""
        self.width += delta_width
        self.height += delta_height

r = Rectangle(Point(0, 0), 10, 5)
print("before growing:", r)
r.grow(10, 20)
print("after growing:", r)

# sameness:

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 is p2) # False
# p1 and p2 have the same coordinates, but they are not the same object

# shallow equality -- compares only the references
p3 = p1
print(p1 is p3) # True

# deep equality -- compares the values of the objects
def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

print(same_coordinates(p1, p2)) # True

# if the two refers to the same object, they are both shallowly equal and deeply equal

p = Point(3, 4)
q = Point(3, 4)
print("== on points returns", p == q) # False
# == by default does a shallow equality check

# for lists == does a deep equality check
a = [1, 2, 3]
b = [1, 2, 3]
print("== on lists returns", a == b) # True

# copying:

# the copy module provides a function called copy that can make a copy of any object
import copy
p1 = Point(3, 4)
p2 = copy.copy(p1)
print(p1 is p2) # False not the same reference
print(same_coordinates(p1, p2)) # True same coordinates

# this is a shallow copy cause the point is simple object
# for a rectangle -- contais a point -- this will create a refrerence to the same point!!

# insteadd use copy.deepcopy
p2 = copy.deepcopy(p1) # copy everything

