# Dictionary views and sets
K = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(K | {'x':4})        # keys (and some items) views and set like  

# print(v & {'x':4}) # unsupported operand type

# print(k & {'x':4}.values())  # unsupported operand type

D = {'a':1, 'b':2, 'c':3}
print(D.keys() & D.keys()) # Insert keys views

print(D.keys() & {'b'})  # Insert keys and set

print(D.keys() & {'b':1})  # Insert keys and dict

print(D.keys() | {'b', 'c', 'd'})  # Union keys and set

D = {'a':1}
print(list(D.items()))  # Item set like if hasable

print(D.items() | D.keys())  # Union view and view 

print(D.items() | D)  # dict treated some as its keys 

print(D.items() | {('c',3), ('d',4)})  # set of key/value pairs

print(dict(D.items() | {('c',3), ('d',4)}))  # dict accepts iterable sets too

# Sorting dictionary keys
D = {'a':1, 'b':2, 'c':3}
print(D)

ks = D.keys()
# ks.sort()     # Sorting a view object doesn't work!

ks = list(ks)   # Force it to be a list and then sort 
ks.sort()
for k in ks :
    print(k, D[k])

ks = D.keys()        # or you can use sorted() on the keys
for k in sorted(ks):  print(k, D[k])  # sorted () accepts any iterable # sorted () returns its result

for k in sorted(D): print(k, D[k])  # Better yet sort the dict directly # dict iterators return keys

print('c' in D)

print('x' in D)

if 'c' in D: print('present', D['c'])

print(D.get('c'))

print(D.get('x'))

if D.get('c') != None: print('present', D['c']) 