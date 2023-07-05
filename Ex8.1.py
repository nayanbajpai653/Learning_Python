# TUPLER , FILES AND EVERYTHING ELSE
# Tuples

## Tuples in action ##
print((1, 2) + (3, 4))    # concatenation

print((1, 2)* 4)          # repetition

T = (1, 2, 3, 4)
print(T[0])               # indexing 
print(T[0:3])             # slicing

# Tuple syntax peculiarities: commas and parntheses
x = (40)                  # an integer
print(x)

y = (40,)                 # a tuple containing an integer
print(y)

# conversions , methods and immutability
T = ('cc','aa','dd','bb')
tmp = list(T)             # make a list from a tuple's items
tmp.sort()                # sort the list 
print(tmp)
 
T = tuple(tmp)            # make a tuple from list's items
print(T) 

print(sorted(T))          # or use the sorted built in

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)

T = (1, 2, 3, 2, 4, 2)    
print(T.index(2))         # offset of first appearance after offset 2

print(T.index(2, 2))      # offset of appearance after offset 2

print(T.count(2))         # How many 2s are there?

T = (1, [2, 3], 4)
# T[1] = 'spam'           # this fails: can't change tuple itself

T[1][0] = 'spam'          # this work: can change mutables inside  
print(T)