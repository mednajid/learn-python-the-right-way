# encapsulation and generalization:

# ex: for multipication table:
def print_multiplication_table(n):
    for i in range(1, 7):
        print(n*i, end=' ')

# local variables:
# you are free to use multiple variables with the same name as long as they are not in the same function

# the break statement:
#===> leave the loop immediately
for i in [12, 16, 17, 24, 29]:
    if i % 3 == 0:
        break
    print(i)
print("done")

# for and while do their tests at the start -- pre-test loop

# the continue statement:
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:
        continue
    print(i)
print("done")


# paired data:
year_born = ("paris Hilton", 1981)

# we could put them in a list:
celbs = [("paris Hilton", 1981), ("Britney Spears", 1981), ("Madonna", 1958), ("Miley Cyrus", 1992)]
for name, year in celbs:
    print(name, "was born in", year)



#newtom's method:
def sqrt(n):
    approx = n / 2.0
    while True:
        better = (approx + n/approx) / 2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better
print(sqrt(25))

