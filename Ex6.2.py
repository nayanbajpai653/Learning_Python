# String conversion tool
# print("42" + 1) # strings are immutable # string and int objects can't concatenate

print(int("42"), str(42)) # convert from/to string

print(repr(42)) # convert as to-code string

print(str('sapm'), repr('spam'))

S = "42"
I = 1
# print(S + I) # immutable

print(int(S) + I)  # Force addition

print(S + str(I)) # Force concatenation

a = str(3.1415), float("1.5")
print(a)

s = '5'
s = chr(ord(s) + 1)
print(s)

s = chr(ord(s) + 1)
print(s)

print(int('5'))
print(int('5') - ord('o'))

B = '1101' # convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print(int('1101' , 2))

# Changing string
S = 'SPAM'
# S[0] = "x" # immutable 
print(S)

S = S + 'spam!'  # To change a string , make a new one
print(S)

S = S[:4] + 'Burger' + S[-1]
print(S)

S = 'splot'
S = S.replace('pl' , 'pamal') 
print(S)

print('That is %d %s Bird' % (1, 'dead')) # Format expression 