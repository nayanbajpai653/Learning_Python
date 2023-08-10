# The Documentation Interlude
# The dir function
import sys
print(dir(sys))

print(dir([]))

print(dir(''))

print(dir(str) == dir(''))                       # same result as prior example

print(dir(list) == dir([]))

# Docstrings: ___doc___
""" 
Module documentation
Words Go Here
"""

spam = 40

def square(x):
    """
    function documentation
    can we have your liver then?
    """
    return x ** 2                                # square

class employee:
    "class documentation"
    pass
    
print(square(4))
print(square.__doc__)

# import docstrings
# """
# function documantation 
# can wa have your liver then?"""
# print(docstrings.__doc__)

# built -in docstrings

import sys
print(sys.__doc__)

print(sys.getrefcount.__doc__)

print(int.__doc__)

print(map.__doc__)