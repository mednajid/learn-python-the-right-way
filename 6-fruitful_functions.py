# to make more complex programs: incremental development wich avoid long debugging sessions and helps to find bugs more quickly

# if nothing is returned, the function returns None

# debbuging with print

# composition: calling one function from within another

# the coding style: python enhancement proposal (PEP) 8

# testing -- unit testing

import sys

def absolute_value(x):
    if x < 0:
        return 1
    else:
        return x

def test(did_pass):
    """ Print the result of a unit test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite() # Here is the call to run the tests


# we could use assert instead of test