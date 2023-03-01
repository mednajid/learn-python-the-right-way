# we could group pair of values like this: ("day" "25")

# the pair is an example of a tuple

# a tuple is a sequence of values separated by commas
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia)
print(julia[2])

# tuples are immutable
# julia[2] = 1968 # this will give an error

# same as a string
julia = julia[:3] + ("Eat Pray Love", 2010, "Actress", "Atlanta, Georgia")
print(julia)

# to create a tuple with a single element, you have to include a comma
ty = (4, )
print(type(ty))

# without the comma, it is just a number
ty = (4)
print(type(ty))

# tuples assignment:
(name, surname, birth, movie, year, profession, place) = julia
print(name)

# tuple assignement is like packing and unpacking

# packing: assigning a tuple to a variable
b = ("bob", 19, "CS")
# unpacking: extracting the values from a tuple
(name, age, major) = b
print(name)

#swap a variable values:
a = 5
b = 10
print(f"a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")

# or swap with tuple assignment:
a = 5
b = 10
print(f"a = {a}, b = {b}")
(a, b) = (b, a)
print(f"a = {a}, b = {b}")

# return multiple values from a function:
def min_max(t):
    return min(t), max(t)

print(min_max([1, 2, 3, 4, 5]))
print(type(min_max([1, 2, 3, 4, 5]))) # tuple

# we can make a tuple with multiple tuples, lists, dictionaries, etc.



