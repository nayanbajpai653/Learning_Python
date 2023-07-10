# ASSIGNMENT , EXPRESSIONS AND PRINTS #  
# Sequence Assignment 
nudge = 1
wink = 2
A, B = nudge, wink 
print(A, B)                                         # Tuple assignment # Like A = nudge; B = wink

[C, D] = [nudge, wink]                              # list assignment
print(C, D)

nudge = 1
wink = 2
nudge, wink = wink, nudge                           # Tuple: swapa values to list of names
print(nudge, wink)                                  # like T = nudge; nudge = wink; wink = T  

[a, b, c] = (1, 2, 3)                               # assign tuple of value to list of names 
print(a, b)

(a, b, c) = "ABC"                                   # assign string of characters to tuple 
print(a, c)

# advanced sequence assignment patterns
string = 'spam'
a, b, c, d = string                                 # same number on both sides 
print(a, d)

# a, b, c = string                                  # error if not

a, b, c = string[0], string[1], string[2:]          # index and slice    
print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]           # slice and concatenate
print(a, b, c)

a, b = string[:2]                                   # same, but simpler
c = string[2:]
print(a, b, c)

(a, b), c = string[:2], string[2:]                  # nested sequences
print(a, b, c)

((a, b), c) = ('SP','AM')                           # paired by shape and position
print(a, b, c)

red, green, blue = range(3)
print(red, blue)

print(range(3))                                     # use list(range(3))

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]   
    print(front, L)