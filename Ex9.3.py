# a useful convenience
seq = [1, 2, 3, 4]

a, *b = seq                                      # fisrt, rest
print(a, b)

a, b = seq[0], seq[1:]                           # first, rest: traditional
print(a, b)

*a, b = seq                                      # rest, last 
print(a, b)

a, b = seq[:-1], seq[-1]                         # rest, last: traditional
print(a, b)

# application for loop
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

a, *b, c = (1, 2, 3, 4)                          # d get [2, 3] 
print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:  # a, b, c = (1, 2, 3) 
    print(a, b, c,)

for all in[(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)


# multiple-target assignments
a = b = c = 'spam'
print(a, b, c)

c = 'spam' 
b = c
a = b
print(c)

# multiple-target assignments and shared references 
a = b = 0 
b =  b + 1
print(a, b)

a = b = []
b.append(42)
print(a, b)

a = []
b = []
b.append(42)
print(a ,b)