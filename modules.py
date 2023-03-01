# a module is a file containing Python definitions and statements.

# exemple the random module
import random
rng = random.Random()
dice_throw = rng.randint(1, 7) # 1 <= dice_throw <= 6 uniformly
delay_in_seconds = rng.random() * 5.0
r_odd = rng.randrange(1, 100, 2) # 1 <= r_odd <= 99, odd
print(dice_throw, delay_in_seconds, r_odd) 

# how to shuffle a list -- 
# cards = rng.shuffle(range(10)) # shuffle the list in place
# print(cards)-- lazy promise does not support the shuffle method
cards = list(range(10))
rng.shuffle(cards)
print(cards)

# repeatability and testing:
# --random numbers are predictable -- in fact they are psuedo-random
# each time you ask for a random number you get one based on the seed value

drng = random.Random(123) # seed the random number generator
print(drng.random())

# picking balls from a bags

import random

def make_random_ints(num, lower_bound, upper_bound):
    """ generate a list of num random integers in the range"""
    rng = random.Random()
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

print(make_random_ints(5, 1, 13))

# if we don't wnat duplicates we can shuffle the list of range(a, b) and take the first n elements

# the time module: -- to calc the time of a process
import time
def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000 # 10 million elements
testdata = range(sz)

t0 = time.process_time()
my_result = do_my_sum(testdata)
t1 = time.process_time()
print("my_result = {0} (time taken = {1:.2f} seconds)".format(my_result, t1 - t0))

t2 = time.process_time()
their_result = sum(testdata)
t3 = time.process_time()
print("their_result = {0} (time taken = {1:.2f} seconds)".format(their_result, t3 - t2))

# the math module:
import math
print(math.pi) # the constant pi
print(math.sqrt(2.0)) # the square root of 2

# creating our own modules:
# -- they must have the .py extension

def remove_at(pos, seq):
    return seq[:pos] + seq[pos + 1:]
# save it as seqtools.py
# and import it as a module
# import seqtools
# seqtools.remove_at(2, [1, 2, 3, 4, 5])


# namespaces:
# a namespace is a collection of names that belong to a module or a function ...

#Module1.py
question = "What is the meaning of life?"
answer = 42

#Module2.py
question = "what is your quest?"
answer = "To seek the holy grail"

# to import them:
# import Module1
# import Module2
# print(Module1.question, Module1.answer)
# print(Module2.question, Module2.answer)

# the name of the namespace is the name of the module and the name of the file
# math.py is the name of the file and math is the name of the module

# scope and lookup:
# the scope is an identifier's region of visibility

# there are 3 important scopes in python:
# -- the global scope -- the scope of a module or file
# -- the local scope -- the scope of a function
# -- the built-in scope -- like range, len, print, etc who are used whitout inporting a module

# if the same identifier in diffrent scopes
# local scope overrides global scope and global scope overrides built-in scope

# exemple of range:
def range(n): # global scope
    return 123*n
print(range(10)) # 1230

# more complex example:
n = 10
m = 3
def f(n):
    m = 7
    return 2*n + m
print(f(5), n, m) # 17

# attributes and the dot operator:

# variable inside a module are called attributes
# objescts have __doc__ attribute
# function have __annotations__ attribute

# attributes are accessed using the dot operator (.)

#when we access a dotted name like math.pi we call it a fully qualified name

# import statement variants:
import math
x = math.sqrt(10)

from math import cos, sin, sqrt  # the names are added directely to the corrent namespace
x = sqrt(10)

from math import * # all names are added to the current namespace

# the first form is the most common and the most explicit
# but we can import them in a shorter way:
import math as m
x = m.sqrt(10)
print(x)

# another case:
def area(r):
    import math
    return math.pi * r * r

x = math.sqrt(10) # error because math is not defined in the current scope

