# print(2/0) this will throw an exception --division by zero

a = []
# print(a[0]) # IndexError: list index out of range

tup = (1, 2, 3)
# tup[0] = 4 # TypeError: 'tuple' object does not support item assignment

# we can handle the exception using try and except
file = input("Enter the file name: ")
try:
    # try to open the file
    f = open(file, 'r') 
    # an error may occur here!
except IOError:
    print("Cannot open", file)
finally:
    print("Done") # this will always be executed


# raise you own exception:
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

# raise ValueError("{0} is not a valid age".format(age))