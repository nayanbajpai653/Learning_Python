# Special cases
L = ["Good",
     "Bad",
     "Ugly"]                                     # open pairs may span lines
print(L)

a = 56
b = 'ef'
c = -1
d = 'han'
e = 'older'
f = 'new'
g = 0

if a == b and c == d and  \
   d == e and f == g:                                                    
   print('older')                                # backslashes allow continutions....

if (a == b and c == d and 
    d == e and e == f):
    print('new')                                 # but parentheses usually do too

x = 1 + 2 + 3  \
+4                                               # omitting the \ makes this different
print(x)

x = 1; y = 2; print(x)                           # more then one single statement 

S = """
aaaa
bbbb
ccc"""
print(S)

S = ('aaa'
     'bbb'
     'ccc')                                      # comments here are ignored
print(S)

if 1: print('hello')                             # simple statement on header line 

# Truth test 
print(2 < 3, 3 < 2)                              # less-than: return true or false (1 or 0)

print(2 or 3, 3 or 2)                            # return left operand if true else, return right operand (true or false)
print([] or 3)
print([] or {})

print(2 and 3, 3 and 2)                          # returns left operand if false else, return right operand (true or false)
print([] and {})
print(3 and [])

# the if/else ternary expression
# if X:
#     A = Y
# else:
#     A = Z
# A = Y if X else Z

A = 't' if 'spam' else 'f'                       # nonempty is true
print(A)

A = 't' if '' else 'f'
print(A)

print(['f','t'][bool('')])

print(['f','t'][bool('spam')])