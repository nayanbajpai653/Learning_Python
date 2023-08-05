# list comprehentions: A first look and basics
L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10
    print(L)

L = [x + 10 for x in L]
print(L)
 
res = [] 
for x in L:
    res.append(x + 10)
    print(res)

print(zip('abc', 'zyx'))

print(zip('abc', 'xyz'))

# the range iterator
R = range(10)                                    # range returns an iterator , not a list
print(R)

I = iter(R)                                      # make a iterator from the range
print(next(I))                                   # advance to next result

print(next(I))

print(next(I))

print(list(range(10)))                           # to force a list if required 

print(len(R))                                    # range also does len and indexing but no others

print(R[0])

print(R[-1])

print(next(I))                                   # continue taking from iterator , where left off

print(I.__next__())                              

# the map, zip, and filter iterators 
M = map(abs, (-1, 0, 1))                         # map returns a iterator not a list
print(M)

print(next(M))                                   # use iterator manually: exhausts results

print(next(M))

print(next(M))                                   # stopiteration

for x in M:
    print(x)                                     # map iterator is now empty: one pass only

M = map(abs, (-1, 0, 1))                         # make a new to scan again
for x in M:
    print(x)                                     # iteration ccontexts auto call next()

print(list(map(abs, (-1, 0, 1))))                # can force a real list if needed

Z = zip((1, 2, 3), (10, 20, 30))                 # zip is the same: a one-pass iteratior
print(Z)

print(list(Z))

for pair in Z:
    print(pair)                                  # exhausted after one pass

Z = zip((1, 2, 3), (10, 20, 30))
for pair in Z:
    print(pair)                                  # iterator used automatically or manully 

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))

print(next(Z))

print(filter(bool, ['spam', '', 'ni']))

print(list(filter(bool, ['spam', '', 'ni'])))