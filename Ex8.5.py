# The none object 
L = ['None'] * 100
print(L)

print(type(None))

str =  ""
print(str == None)

print(None == False)                             # comparing none with false
print(None == True)                              # comparing none with true

# The bool type
print(bool(1))

print(bool('spam'))

print(bool({}))

# type objects 
type([1]) == type([])                            # type of another list
type([1]) == list                                # list type name
isinstance([1], list)                            # list or customisation thereof

import types
def f(): pass
print(type(f) == types.FunctionType)

# other types 
# assignment creates references, not copies 
L = [1, 2, 3]
M = ['X', L, 'Y']                                # embed a references to L
print(M)

L[1] = 0                                         # change M too
print(L)

L = [1, 2, 3]
M = ['X', L[:], 'Y']                             # embed a copy L, not M
L[1] = 0                                         # changes only L not M
print(L)

print(M)

# repetition adds one level deep
L = [4, 5, 6]
X = L * 4                                        # Like [4,5,6]+[4,5,6]+.....
Y = [L] * 4                                      # [L]+[L]+.....=[L,L,...]

print(X)

print(Y)

L[1] = 0                                         # impacts Y but not X
print(X)

print(Y)

# beaware of cyclic data structures
L = ['grail']                                    # append reference to same object
L.append(L)                                      # generates cycle in object: [...]
print(L)

# immuable type can't be changed in place
T = (1, 2, 3)

T[2] = 4                                         # error! 

T = T[:2] + (4,)                                 # ok: (1,2,4)

print(T)