# LIST AND DICTIONARIES
# basic list operations
print(len([1, 2, 3]))  # length

print([1, 2, 3] + [4, 5, 6])  # concatenation

print(['NI!'] * 4)  # repetition

print(str([1, 2]) + "34")  # same as "[1, 2]" + "34"

print([1, 2] + list("34"))  # same as [1, 2] + ["3","4"]

# list lteration and comprehensions
print(3 in [1, 2, 3])  # membership

for x in [1, 2, 3]:
    print(x, end=' ')  # iteration

rec = [c * 4 for c in 'spam']  # list comprehensions

rec = []
for c in 'SPAM':
    rec.append(c * 4)  # list comprehensions equivalent
    print(rec)              

print(list(map(abs, [-2, -1, 0, 1, 2])))  # map function acress sequence

# Indexing, Slicing and metrixes
l = ['spam','spam','spam']
print(l[2])  # offsets start at zero

print(l[-2])  # negative count from the right

print(l[1:])  # slicing fetches sections

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matrix[1])

print(matrix[1][1])

print(matrix[2][0])

pmatrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(matrix)