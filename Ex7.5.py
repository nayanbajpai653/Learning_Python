# Other way to make Dictionaries
D = {'name':'mel', 'age':45} # traditional litreal expression
print(D)

D = {}  # assign by keys dynamically
D['name'] = 'mel'  
D['age'] = 45
print(D)

print(dict(name='mel' , age=45))  # dict keyword argument from

print(dict[('name','mel'), ('age',45)])  # dict key/value tuples form

print(dict.fromkeys(['a','b'], 0))

# dictionary comprehentions
print(list(zip(['a','b','c'], [1, 2, 3])))  # zip together keys and values

D = dict(zip(['a','b','c'], [1, 2, 3]))  # make a dict comprehension
print(D)

D = {k: v for (k, v) in zip(['a','b','c'], [1, 2, 3])}
print(D)

D = {x: x ** 2 for x in[1, 2, 3, 4]}  # or range(1,5)
print(D)

D = {c: c * 4 for c in 'SPAM'}  # Loop over any iterable
print(D)

D = {c.lower(): c + '!' for c in ['SPAM','EGGS','HAM']}
print(D)

D = dict.fromkeys(['a','b','c'], 0)  # initialize dict from keys 
print(D)

D = {k:0 for k in ['a','b','c']}  # same, but with a comprehension
print(D)

D = dict.fromkeys('spam')  # other iterators, default value
print(D)

D = {K: None for K in 'spam'}
print(D)

# Dictionary views 
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()   
print(K)

print(list(K))

V = D.values()  # Ditto for values and items views
print(V)

print(list(V))

print(list(D.items()))

# print(K[0])  # List operations fail unless converted

print(list(K)[0])

for K in D.keys():  
    print(D)         # iterators used automatically in loops

for key in D:   
    print(K)      # still no need to call keys() to iterate

D = {'a':1, 'b':2, 'c':3}
print(D)

k = D.keys()
V = D.values()
print(list(K))  # views maintain same order as dictionary

print(list(V))

del D['b']   # change the dictionary in-place
print(D)

print(list(V))  # reflected in any current view objects

print(list(V))