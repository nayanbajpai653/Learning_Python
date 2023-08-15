# Function Basics
# A first Example: Definitions and calls
def times(x, y):                                 # create and assign function
    print(x * y)                                 # body executed when called

print(times(2, 4))                               # Arguments in parentheses

x = times(3.14, 4)                               # save the result object
print(x)

print(times('Ni' , 4))                           # functions are "typeless"

# A second Example: Inteersecting Sequences
def intersect(seq1, seq2):
    res = []                                     # start empty
    for x in seq1:                               # scan seq1
        if x in seq2:                            # common item?
            res.append(x)                        # add to end
    print(res)        

s1 = "SPAM"
s2 = "SCAM"
print(intersect(s1, s2))                         # strings

print([x for x in s1 if x in s2])

x = intersect([1, 2, 3], (1, 4))                 # mixed types
print(x)                                         # saved result object


