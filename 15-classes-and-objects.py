# creating a class -- point:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self):
        """ create a new point at the origin """
        self.x = 0
        self.y = 0
    
# create a new point
p = Point() # the constructor is called -- instantiate an object
print(p.x, p.y)

p.x = 7 # set the x coordinate of p to 7
p.y = 6 # set the y coordinate of p to 6

print("x={0}, y={1}".format(p.x, p.y))

# improving the initializer method:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self, x=0, y=0): # make x and y optional
        """ create a new point at the origin """
        self.x = x
        self.y = y

p = Point(7, 6) 
q = Point()
print(p.x, p.y)
print(q.x, q.y)

# adding more methods to the class:

class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self, x=0, y=0): # make x and y optional
        """ create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(7, 6)
print(p.distance_from_origin())

# improving the point class:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self, x=0, y=0): # make x and y optional
        """ create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def print_point(self):
        """ return a string representation of my point """
        return "({0}, {1})".format(self.x, self.y)

p = Point(7, 6)
print("p is {0}".format(p.print_point()))

print(str(p)) # this will call p.__str__()

# adding a __str__ method to the class:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self, x=0, y=0): # make x and y optional
        """ create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
    # python will use this when ever it needs a string representation of an object
    def __str__(self):
        """ return a string representation of my point """
        return "({0}, {1})".format(self.x, self.y)

p = Point(7, 6)
print(str(p))
print(p)

# instances as return values:
def midpoint(p1, p2):
    """ return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my) # return a new point

p1 = Point(3, 4)
p2 = Point(5, 12)
p3 = midpoint(p1, p2)
print(f"the midpoint is : {p3}")

# let's add this as a method to the class:
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    # the initializer method -- initial state/values
    def __init__(self, x=0, y=0): # make x and y optional
        """ create a new point at the origin """
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """ compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
    # python will use this when ever it needs a string representation of an object
    def __str__(self):
        """ return a string representation of my point """
        return "({0}, {1})".format(self.x, self.y)
    
    def midpoint(self, other):
        """ return the midpoint of points p1 and p2 """
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my) # return a new point

p1 = Point(3, 4)
p2 = Point(5, 12)
p3 = p1.midpoint(p2)
print(f"the midpoint is : {p3}")

# objects can have state -- attributes
# objects can have behavior -- methods