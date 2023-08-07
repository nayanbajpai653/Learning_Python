# Multiple versus single iterators
R = range(3)                                     # range allows multiple iterators 
print(next(R))                                   # range object is not iterator

I1 = iter(R)
print(I1)

print(next(I1))

I2 = iter(R)
next(I2)                                         # Two iterators on one range

print(next(I1))                                  # I1 is at a different spot than I2

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)                                     # Two iterators on one zip
I2 = iter(Z)
print(next(Z))

print(next(I1))

print(next(I2))                                  # I2 is at same spot as I1!

M = map(abs, (-1, 0, 1))                         # ditto for map (and filter)
I1= iter(M)
I2 = iter(M)
print(next(I1), next(I1), next(I1))

print(next(I2))                                  # stop iteration

R = range(3)                                     # but range allows many iterators
I1, I2 = iter(R), iter(R)
print(next(I1), next(I1), next(I1))

print(next(I2))

# dictionary view iterators
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()                                     
print(K)

print(next(K))                                   # view are not iterators themselves

I = iter(K)                                      # view have an iterator,
print(next(I))                                   # which can be used manually but does not support len(), index

print(next(I))

for k in D.keys():                               # all iteration contexts use auto
    print(k, end=' ')