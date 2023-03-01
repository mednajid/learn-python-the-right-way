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
    
    def __str__(self):
        """ return a string representation of my point """
        return "({0}, {1})".format(self.x, self.y)