# Parallel Traversals: Zip and map 
L1 = [1,2,3,4]
L2 = [5,6,7,8]

print(zip(L1, L2))

print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)

print(T3)

print(list(zip(T1, T2, T3)))

S1 = 'abc'
S2 = 'xyz123'

print(list(zip(S1, S2)))

# Dictionary construction with zip
D1 = {'Spam':1, 'eggs':3, 'toast':5}
print(D1)

D1 = {}
D1['spam'] = 1
D1['eggs'] = 3
D1['toast'] = 5

keys = ['spam', 'eggs', 'toast']
value = [1, 3, 5]

print(list(zip(keys, value)))

D2 = {}
for (k, v) in zip(keys, value): 
    D2[k] = v
    print(D2)

keys = ['spam', 'eggs', 'toast']
value = [1,3,5]

D3 = dict(zip(keys, value))

# Generating both offsets and items: enumerate 

S = 'spam'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1

S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

E = enumerate(S)
print(E)

print(next(E))

print(next(E))

print(next(E))

print([c * i for (i, c) in enumerate(S)])