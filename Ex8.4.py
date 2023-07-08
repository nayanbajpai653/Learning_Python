# References Versus Copies
X = [1, 2, 3]
L = ['a', X, 'b']                                  # embed references to X's object
D = {'x':X, 'y':2}

print(X)

print(L)

print(D)

X[1] = 'surprise'                                  # changes all three rferences!
print(X)

print(L)

print(D)

L = [1,2,3]
D = {'a':1, 'b':2}

A = L[:]                                           # instead of A = L (or list(L))
B = D.copy()                                       # Instead of B = D (ditto for sets)

A[1] = 'Ni'
B['c'] = 'spam'

print(L)
print(D)

print(A)
print(B)

X = [1, 2, 3]
L = ['a', X[:], 'b']                               # Embed copies of X's object 
D = {'x':X[:], 'y':2}

print(X)
print(L)
print(D)

# comparisons , equality and truth 
L1 = [1, ('a', 3)]                                 # same value , unique objects 
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)                          # Equivalent? same object?

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)

S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)                  # Less, equal, greater, tuple of results

D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
print(D1 == D2)

print(list(D1.items()))

print(sorted(D1.items()))

print(sorted(D1.items()) < sorted(D2.items()))

print(sorted(D1.items()) > sorted(D2.items()))