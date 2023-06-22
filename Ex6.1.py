## STRINGS ##

y = 'shrubbery',"shrubbery"
print(y)

x = 'knigt"s',"knigt's"
print(x)

title = "Meaning" 'of' "Life" # implicit concatenation
print(title)

z = 'knigt\"s',"knigt\'s"
print(z)

s  = 'a\nb\tc' # \n for new line character set and \t for the tab character
print(s)
print(len(s)) # bytes in string

s = '\001','\002','\003'
print(s)

x = "c:\py\code" #keeps\literally
print(x)
print(len(x))

# Strings in action
#Basic opretion
print(len('abc')) # Length:number of times

print('abc' + 'def') # Concatenation: a new string

print('Ni!' * 4) # Repetition: like 'Ni!' + 'Ni!' + ... 4 times

print('-' * 80) # 80 dashes,the easy way

myjob = "hacker"
for c in myjob: print(c, end=' ') # step through items

print("k" in myjob) # print true if present
print("z" in myjob)
print('spam' in 'abcspamdef')

# Indexing and slicing
s = 'spam'
print(s[0]) #indexing from front
print(s[-2]) #indexing from end

print(s[1:3]) #slicing extract a section
print(s[1:])
print(s[:-1])

s = 'abcdefghijklmnop'
print(s[1:10:2])
print(s[::2])
print(s[::-1])
print(s[5:1:-1])

print('spam'[1:3]) # slicing syntax

print('spam'[slice(1,3)]) # slice objects

print('spam'[::-1])

print('spam' [slice(None, None, -1)])