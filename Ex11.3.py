# extended sequence assignment in loops
a, b, c = (1, 2, 3)                              # tuple assignment
print(a, b, c)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:         # used in for loop
    print(a, b, c)

a, *b, c = (1, 2, 3, 4)                          # extended seq assignment
print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

# nested for loops
items = ["aaa", 111, (4, 5), 2.01]               # a set of objects
test = [(4, 5), 3.14]                            # key to search for 

for key in test:                                 # for all keys                            
    for item in items:                          # for all items
        if items == key:                         # check for match
            print(key, "was found")
        else:
            print(key, "not found!")

for key in test:                                 # for all keys
    if key in items:                             # let python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")

seq1 = "spam"
seq2 = "scam"

res = []                                         # start empety 
for x in seq1:                                   # scan first sequence
    if x in seq2:                                # common items?
        res.append(x)

print(res)