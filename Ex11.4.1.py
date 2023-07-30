# Loop coding techniques
# Counter loop: while and range
print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))

print(list(range(-5, 5)))

print(range(5, -5, -1))

print(list(range(5, -5, -1)))

for i in range(3):
    print(i, 'pythons')

X = 'spam'
for items in X: 
    print(items, end=' ')                                       # simple iteraion

i = 0
while i < len(X):
    print(X[i], end=' ')                                        # simple iteration
    i += 1

print(len(X))                                                   # print length of string

print(list(range(len(X))))                                      # all length offsets into X

for i in range(len(X)):
    print(X[i], end=' ')

# nonexhaustive traversals: range and slices
for item in X:                                                  # simple iteration  
    print(item)

S = 'abcdefghijk'
print(list(range(0, len(S), 2)))

for i in range(0, len(S), 2):
    print(S[i], end=' ')

S = 'abcdefghijk'
for c in S[::2]:
    print(c, end=' ')

# Changing lists: range
L = [1, 2, 3, 4, 5]

for x in L:
    x += 1

print(L)

print(x)

L = [1, 2, 3, 4, 5]

for i in range(len(L)):                                         # Add one to each item in L
    L[i] += 1                                                   # or L[i] = L[i] + 1
    print(L)

i = 0
while i < len(L):
    L[i] += 1
    i += 1
    print(L)