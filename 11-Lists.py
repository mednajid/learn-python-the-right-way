# list values:
# the simplist way to create a list is to enclose the elements in square brackets
ps = ["Python", "Perl"]
print(ps)

# lists can have elements of different types
zs = ["python", 2.0, 5, [10, 20]]
print(zs)

# a list within another list is nested
print(zs[3])

# an empty list
empty = []
print(empty)

# to access elements is the same as strings
print(zs[0])

# any value that is evaluated to an integer can be used as an index
print(zs[3-1]) # zs[2.0] will throw an error

# an index out of range will also throw an error (IndexError)

# it's commun to use a for loop to iterate over the elements of a list
for p in ps:
    print(p)
#or
for i in range(len(ps)):
    print(ps[i]) # here i is the index

# list length:
print(len(ps))

# list nembership:
print("Python" in ps)
print("Python" not in ps)


# list operations:
# concatenation
print(ps + ["R", "Java"])

# repetition
print(ps * 2)

# slicing:
print(ps[0:1]) # ['Python']

# list are mutable:
# we can change the value of an element
ps[0] = "Python 3"
print(ps)

# we can also change a slice
ps[0:1] = ["Python 2", "Python 3"]
print(ps)


# we can remove elements from a list by assigning an empty list to a slice

# remove the first element
ps[0:1] = []
print(ps)

# we can add elements to a list by assigning a list to an emptu slice
ps[0:0] = ["Python 2", "Python 3"] # add at the beginning
print(ps)

a = [1, 2, 3]
del(a[1]) # delete the second element
print(a)

# we can also use del with slices

# objects and references:
a = "banana"
b = "banana"
# the python interpreter may refer to the same string object for both a and b
# and may refer to different objects with the same value

# to check if two variables refer to the same object, we can use the is operator
print(a is b) # True

# since strings are immutable, python can optimize the memory usage by storing
# this is not the case in the case of lists
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a == b) # True the == operator compares the values of the lists

# so a and b are not the same object, but they have the same value

# aliasing:
a = [1, 2, 3]
b = a
print(a is b) # True
# in this case, a and b refer to the same object

# because the same list have two names, we see that is aliased
b[0] = 17
print(a)

# coloning lists:
# the easiest way to clone a list is to use the slice operator
a = [1, 2, 3]
b = a[:]
print(a is b) # False
# now we have two lists with the same value and we can change them freely

# lists and for loops:

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year:", friend)

# since lists are mutable, it is often useful to iterate through the indices of
xs = [1, 2, 3]
for i in range(len(xs)):
    xs[i] = xs[i] * 2
    print(xs)

# workings with both index and element:
for i, v in enumerate(xs):
    xs[i] = v * 2
print(xs)


# list paramerters:
# passing list as parameter create an alias
def double_stuff(a_list):
    """Overwrite each element in a_list with double the value."""
    for index, val in enumerate(a_list):
        a_list[index] = 2 * val

a = [1, 2, 3]
double_stuff(a)
print(a)

# the list a is shared between two frames __main__ and double_stuff

# list methods:
my_list = [1, 2, 3]
my_list.append(4) # add 4 at the end
print(my_list)

my_list.insert(0, 0) # insert 0 at the beginning
print(my_list)

print(my_list.count(1)) # count the number of occurences of 1

my_list.extend([5, 6, 7]) # add the elements of the list at the end
print(my_list)

print(my_list.index(5)) # return the index of the first occurence of 5

my_list.reverse() # reverse the list
print(my_list) # [7, 6, 5, 4, 3, 2, 1, 0] the list is changed

my_list.sort() # sort the list
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list.remove(3) # remove the first occurence of 3
print(my_list) # [0, 1, 2, 4, 5, 6, 7]

my_list.pop() # remove the last element
print(my_list) # [0, 1, 2, 4, 5, 6]

my_list.pop(0) # remove the first element
print(my_list) # [1, 2, 4, 5, 6]

my_list.pop(3) # remove the fourth element
print(my_list) # [1, 2, 4, 6]

# pure functions and modifiers:

# modifiers:
# function wich modify the list are called modifiers
# the changes are called side effects

# pure functions:
# functions that do not modify the list are called pure functions

def double_stuff(a_list):
    """Return a new list where each element is doubled."""
    new_list = []
    for val in a_list:
        new_list.append(2 * val)
    return new_list

things = [2, 5, 9]
print(double_stuff(things)) # [4, 10, 18]
print(things) # [2, 5, 9]

# it's safe to assign to a variable after passing it to a function

# strings and lists:
song = "the rain in spain"
wds = song.split() # will return a list
print(wds)

print(song.split("ai")) #split is a delimiter

#the reverse is called join
s = ";".join(wds)
print(s)

#list and range:
xs = list("hello world!") #will return a list of char ['h','e'...]
"".join(xs) #return a joined string from the list

#the range function does not compute its values but it give a promise -- only calc a value when it's needed

#nested lists: -- represent matrix
mx = [[1,2,3], [4,5,6], [7,8,9]]
print(mx[1]) #[4, 5, 6]
print(mx[1][2]) #[6]


