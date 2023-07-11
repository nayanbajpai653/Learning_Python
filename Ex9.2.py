# Extended Sequence Unpacking
seq = [1, 2, 3, 4]
a, b, c, d = seq 
print(a, b, c, d)

a, b = seq                                     # too many values to unpack       

a, *b = seq
print(a)
print(b)

*a, b = seq
print(a)
print(b)

a, *b, c = seq
print(a)
print(b)
print(c)

a, b, *c = seq
print(a)
print(b)
print(c)

a, *b = 'spam'
print(a, b)

a, *b, c = 'spam' 
print(a, b, c)

S = 'spam'                                       
print(S[0], S[1:])                               # slices are type specific, *assignment always returns a list 

print(S[0], S[1:3], S[3])

L = [1, 2, 3, 4]
while L:
    front, *L = L                                # get first, rest without slicing
    print(front, L)

# boundary cases 
a, b, c, *d = seq
print(a, b, c, d)

a, b, c, d, *e = seq
print(a, b, c, d, e)

a, b, *e, c, d, = seq 
print(a,b, c, d, e)

a, *b, c, *d = seq                             # two starred expression in assignment

a, b = seq                                     # too many values to unpack

*a = seq                                       # starred assignment target must be in a list or tuple 

*a, = seq 
print(a)