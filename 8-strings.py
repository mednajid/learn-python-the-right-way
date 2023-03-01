# strings, integers, floats, booleans, lists, integers ... are all types in python
# strings and lists are made up of onother types (characters and elements) -- we call them coumpound types
# we may treat them as a single type or as a collection of types

# working with strings as single thing:
# a string is an object so it has methods and attributes

ss = "hello world"
tt = ss.upper() 
print(tt)

# working with strings as a collection of characters:
fruit = "banana"
m = fruit[0] # here 0 us called index
print(m)

# to see all elements and their indices:
print(list(enumerate(fruit))) # list of pairs

# a single character is a string of length 1

# length -- len() is a function that returns the number of elements in a sequence
print(len(fruit)) # 6

# print the last element:
print(fruit[len(fruit)-1]) # last character or fruit[-1] should work too

#slice -- a segment of a string:
s = "Monty Python"
print(s[0:4]) # 0 to 4 but not including 4

# the same for a list
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # 1 to 3 but not including 3

# another way to slice for the beginning and end of a sequence:
print(t[:4]) # from the beginning to 4 but not including 4
print(t[3:]) # from 3 to the end

print(t[:]) # from the beginning to the end

# strings are immutable -- you can't change an existing string
# you can make a new string that is a variation on the original
fruit = "banana"
# fruit[4] = "o" # this will give an error

# the in and not in operators:
print("n" in fruit) # True
print("m" in fruit) # False

# a string is a part of itself and an empty string is part of any string!!
print(fruit in fruit) # True
print("" in fruit) # True

# eureka traversal?

# optional parameters:
# are just like regular parameters except that they are assigned a default value
# optional value None is used to indicate that a parameter has no default value

# the find method: -- more general and use optional parameters like None maybe

"banana".find("na") # 2


#split: -- split a string into parts

s = "hello world"
print(s.split()) # ['hello', 'world'] -- default is to split on whitespace

# join: -- opposite of split
t = ['hello', 'world']
print(" ".join(t)) # hello world

# cleaning up strings:
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    """Return a str with punctuation chars stripped out"""
    for c in s:
        if c in punctuation:
            s = s.replace(c, "")
    return s


my_story = """
2 Pythons are constrictors, which means that they will 'squeeze' the life
3 out of their prey. They coil themselves around their prey and with
4 each breath the creature takes the snake will squeeze a little tighter
5 until they stop breathing completely. Once the heart stops the prey
6 is swallowed whole. The entire animal is digested in the snake's
7 stomach except for fur or feathers. What do you think happens to the fur,
8 feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
9 you guessed it --- snake POOP! """

print(remove_punctuation(my_story).split())

# the string formal method:

s = "my name is {0} and I am {1} years old".format("Ahmed", 25) # 0 in the index {0:f} for float
print(s)

# there is a lot more in the string formating ... 