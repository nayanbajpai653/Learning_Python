# for Loops
# general formula
for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x
    print(sum)

# other data types
S = "lumberjack"
T = ("and", "I'm", "okey")

for x in S: 
    print(x, end=' ')                            # iterate aver a string

for x in T: 
    print(x, end=' ')                            # iterate over a tuple

# tuple assignment in for loops
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:                                 # tuple assignment at work
    print(a, b)

D = {'a':1, 'b':2, 'c':3}
for key in D:
    print(key, '=>', D[key])                     # use dict keys iterator and index

print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)                      # iterate over both keys and values

for both in T :
    a, b = both
    print(a, b)                                  # manual assignment equivalent

((a, b), c) = ((1, 2), 3)                        # nested sequences work too
print(a, b, c)           

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ['XY', 6]]:
    print(a, b, c)