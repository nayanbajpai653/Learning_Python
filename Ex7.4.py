# A Languages Table 
table = {'python': 'guido van rossum',
         'perl':   'larry wall',
         'tcl':    'john ousterhout'}

language = 'python'
creator = table[language]
print(creator)

for lang in table:                  # Same as: for lang in table.key()
    print(lang, '\t', table[lang])

## Using dictionaries to simulate flexible lists

# l = []
# l[99] = 'spam'  # list assignment index out of the range

D = {}
D[99] = 'spam'
print(D[99])

print(D)

# using dictionaries for sparse data structures
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(5, 6, 7)] = 99

x = 2; y = 3; z = 4    # ;separates statements
print(Matrix[(x, y, z)])

print(Matrix)

# Avoiding missing key errors
if (2,3,6) in Matrix:         # check for key befor fetch
    print(Matrix[(2,3,6)])
else:
    print(0)
    
try:
    print(Matrix[2,3,6])  # try to index
except:                   # catch and recover
    print(0)

print(Matrix.get((2,3,4), 0))  # exists; fetch and return

print(Matrix.get((2,3,6,), 0))  # dosen't exist;use default arg

# using dictionaries as "records"
rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/eriter'

print(rec['name'])

mel = {'name': 'Mark',
       'jobs': ['trainer','writer'],
       'web': 'www.rmi.net/ lutz',
        'home': {'state':'CO','zip':80513}}

print(mel['name'])

print(mel['jobs'])

print(mel['jobs'][1])

print(mel['home']['zip'])