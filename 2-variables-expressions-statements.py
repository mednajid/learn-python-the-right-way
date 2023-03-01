print(type("hello world")) #str 
print(type(7)) #int
print(type(7.1)) #float
print(type("7")) #str not int

# 2.1 Values and data types:

print("hello world") #can contain single cotes
print('hello world') #can contain double cotes
print('''hello world''') #can contain single and double cotes
print("""hello world""") #can contain single and double cotes

# triple cotes can be used to write multiple lines
message = """hello it's me mohammed
najid and i am a python developer"""
print(message)

# python store them in same way
# but it has to decide which one to use when printing

# 33,2 ==> will be (33, 2) a pair haha

# 2.2 Variables

# a Variable is a name that refers to a value

message = "hello world"
n = 17
pi = 3.14159

n = 3 # a variable can change value or type over time

# 2.3 Variable names and keywords

# a varible name can be as long as you like, but it must start with a letter or underscore
# and can contain only letters, numbers and underscores, and it is case sensitive and can't be a keyword

# 2.4 Statements

# a statement is a unit of code that the python interpreter can execute like a variable assignment, if statement, or function call
# statemets don't return values

# 2.5 expressions:
# an expression is a combination of values, variables, and operators
# ex: 2 + 2 , len("hello world") ...
# the evalution of an expression produces a value

# 2.6 Operators and operands:
# an operator is a special symbol that represents a simple computation like addition, multiplication, or string concatenation
# the values the operator is applied to are called operands
# ex: 2 + 3 ==> 2 and 3 are operands and + is the operator

# 6/4 ==> 1.5
# 6//4 ==> 1

# -6/4 ==> -1.5
# -6//4 ==> -2 ?? round down

# 2.7 type conversion functions: int, float, str

int(41.5) # 41
int("42") # 42
int(1) # 1 not problem!
# int("3apples")  # error

# 2.8 order of operations:

# python follows the same order of operations as mathematics

# 2.9 operations on strings:
# + ==> concatenation , ex: "hello" + "world" ==> "helloworld"
# * ==> repetition , ex: "hello" * 3 ==> "hellohellohello"

# 2.10 input function:
# input() ==> reads a line from user input and converts it to a string

# 2.11 the composition:
# ex: print("the area is", 3.14*(float(input("what's the redius?")))**2)
# but it's better to simplify the code 

# 2.12 modulus:
# % ==> the remainder operator, ex: 7 % 3 ==> 1

