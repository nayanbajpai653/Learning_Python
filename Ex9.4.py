# Augmented Assignments
x = 1 
x = x + 1                                        # Traditional
print(x)

x += 1                                           # Augmented
print(x)

s = 'spam'                                        
s += 'SPAM'                                      # implied concatenation 
print(s)

L = [1, 2]
L = L + [3]                                      # concatenate: slower
print(L)

L.append(4)                                      # faster, but in-place
print(L)

L = L + [5, 6]                                   # concatenate: slower
print(L)

L.extend([7, 8])                                 # faster, but in place
print(L)

L += [9, 10]                                     # mapped to L.extend([9, 10])
print(L)

# augmented assingnment and shared references 

L = [1, 2]
M = L                                            # L and M references the same object
L = L + [3, 4]                                   # concatenation makes a new object
print(L, M)                                      # Change L but not M

L = [1, 2]
M = L
L += [3, 4]                                      # but += really means extend
print(L, M)                                      # M see the in-place change too!

# expression statements and in-place changes 
L = [1, 2]
L.append(3)                                      # append is an in-place change
print(L)

L = L.append(4)                                  # but append returns none, not L
print(L)