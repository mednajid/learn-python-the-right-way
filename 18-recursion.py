# recursion is a function that calls itself
# a human is someone whose mother is a human ...

# drawing Fractals:
# a fractal is a drawing that is self-similar

# Koch fractal -- 0 order is a line:
# ----------------------------------------

# 1st order is a triangle:
# ----------/\-----------


# 2nd order is a triangle with 2 smaller triangles:
# ---/\--/\/\/\--/\--- ...

def koch(t, order, size):
    """Make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order == 0: # the base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

# recursive data structures:

print(sum([1, 2, 3, 4, 5])) # 15 works fine

# print(sum([1, [2, 3], 4, 5])) # TypeError: unsupported operand type(s) for +: 'int' and 'list'

def r_list_sum(lst):
    tot = 0
    for element in lst:
        if type(element) == type([]):
            tot = tot + r_list_sum(element)
        else:
            tot = tot + element
    return tot

print(r_list_sum([1, [2, 3], 4, 5])) # 15

# example with recusive directory and files:
# list all files in a directory tree

import os 

def get_dirlist(path):
    """ return a list of all entries in the directory given by path."""
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix=""):
    if prefix == "":
        print("folder listing for", path)
        prefix = "| "
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")

print_files(".")