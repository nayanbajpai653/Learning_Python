# Dictionaries
# basic dictionary operations
D = {'spam':2, 'ham':1, 'eggs':3}  # make a dictionary
print(D['spam'])  # fetch a value by key

print(D)

print(len(D))  # Number of entries in dictionary

print('ham' in D)  # Key membership test alternative

print(list(D.keys()))  # create a new list of my keys

# changing dictionaries in place
D['ham'] = ['grill', 'bske', 'fry']  # change entry
print(D)

del D['eggs']  # Delete entry
print(D)

D['brunch'] = 'Bacon'  # new entry
print(D)

# more dictionary methods 
D = {'spam':2, 'ham':1, 'eggs':3}
print(list(D.values()))

print(list(D.items()))

print(D.get('spam'))  # a key that is there
print(D.get('toast'))  # a key that is missing
print(D.get('toast', 88))

D2 = {'toast':4, 'muffin':5}
D.update(D2)
print(D)

# pop a dictionary by key 
D.pop('muffin')
print(D)

D.pop('toast')  # delete and run for key
print(D)

# pop list by position
L = ['aa','bb','cc','dd']
L.pop()                    # delete and return from the end 
print(L)

L.pop(1)  # delete from a specific position
print(L)