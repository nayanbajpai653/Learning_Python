# String methods #
# Changing strings 
S = 'SPAMMY'
s = S[:3] + 'XX' + S[5:]
print(s)

s = S.replace('MM' , 'XX')
print(s)

print('aa$bb$cc$dd'.replace('$' , 'SAPM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
s = S.find('SAPM')  # Search for position
print(s)  # Occurs at of set 4

s = S[:4] + 'EGGS' + S[8:]
print(s)

print(S.replace('SPAM' , 'EGGS'))  # Replace all
print(S.replace('SPAM' , 'EGGS' , 2))  # Replace one 

s = 'spammy'
l = list(s)
print(s)

l[3] = 'x'  # Works for lists, not strings
l[4] = 'x'
print(l)

s = ''.join(l)
print(s)

print('SAPM'.join(['eggs' , 'sausage' , 'ham' , 'toast']))

# Parsing Text
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)

cols = line.split()
print(cols)

line = 'bob,hacker,40'
print(line.split(','))

line = "i'mSPAMaSPAMlunberjack"
print(line.split("SPAM"))

# other common string method
line = "The knight who say Ni!\n"
print(line.rstrip())

print(line.upper())

print(line.isalpha())

print(line.endswith('Ni!\n'))

print(line.startswith('The'))

print(line.find('Ni') != -1)  # Search via method call or exprassion

print('Ni' in line) 

sub = 'Ni!\n'
print(line.endswith(sub))  # End test via method call or slice

print(line[-len(sub):] == sub)