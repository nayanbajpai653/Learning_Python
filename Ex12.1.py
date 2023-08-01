# Iterations and Comprehansions, Part 1
# Iterators: a first look
for x in [1, 2, 3, 4]: 
    print(x ** 2, end=' ')

for x in(1, 2, 3, 4):
    print(x ** 3, end='')

for x in 'spam':
    print(x * 2, end=' ')

# Built-in type iterators
D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key, D[key])

I = iter(D)
print(next(I))

print(next(I))

print(next(I))

# print(next(I))                                        # stop iteration

import os
P = os.popen('dir')
print(P.__next__())

print(P.__next__())

R = range(5)
print(R)

I = iter(R)                                           # use iteration protocall to produce results
print(I)

print(next(I))

print(list(range(5)))                                 # or use list to collect al results at once 

E = enumerate('spam')                                 # enumerate is an iterable too
print(E)

I = iter(E)
print(next(I))                                        # generate results with iteration protocol

print(next(I))                                        # or use list to force generation to run 

print(list(enumerate('spam')))