#integer addition 
print(123 + 222)

#floating-point multiplication
print(1.5 * 4)

#2 to the power 100
print(2 ** 100)

#how many digits in a big number 
print(len(str(2 ** 1000)))

import math 
print(math.pi) #execute value of pi
print(math.sqrt(144)) #execute square root of 144

import random
print(random.random()) #print random number between 0 to 1
print(random.choice([1, 2, 3, 4])) #print random number that insert 

s = 'spam!'
print(len(s)) #length of s

print(s[0]) #first item in s

print(s[1]) #second item in s

print(s[-1]) #last item in s

print(s[-2]) #last second item in s

print(s[1:3]) #slice string and print 2nd and 3rd item in s 

print(s[0:3]) #everything past the first 

print(s[:3]) #everything but the last 

print(s[:-1]) #everything but the last

print(s[:]) #all of s

print(s + "xyz") #add xzy at end of spam

print(s * 8) #repet spam 8 times

print(s.find('pa')) #find the given value

print(s.replace('sp','px')) #replace occurrences of a substrings with another

print(s.upper()) #upper case conversion 
print(s.lower()) #lower case conversion

line = 'sdds,wefwe,fqwes\n'
print(line.split(',')) #convert into list 
print(line.rstrip(',')) #remove whitespace characters on the right side

# print(dir(s)) #returns a list of all the attributes available for a given object 

x = 'A\nB\tC' #\n end of line , \t is tab
print(x)
print(len(x))

print(ord('\n')) #\n is a byte with binary value 10 in ASCII

y = 'A\oB\oC' #\o is a binary zero byte , does not terminate string
print(y) 
print(len(y))

import re 
match = re.match('hello[ \t]*(.*)world','hello  python world')
print(match.group(1))





