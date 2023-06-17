#### TUPLES ####
T = (1,2,3,4) #4-items in tuple
print(len(T)) #length

print(T + (5,6)) #concatenation

print(T[0]) #index slicing 

print(T.index(4)) #tuple methods: 4appends at offset 3

print(T.count(4)) #4 appends once 

# T[0] = 2 #tuples are immutable
# print(T)

# T.append(4) #tuple object has no attribute append
# print(T)

f = open("myfile.txt","w") #make a new file in output mode 
f.write('hello\n') # write string bite to it
print(f)

print(f.write('world\n')) 

print(f.close())

F = open('myfile.txt') 
text = F.read() #read entire file into a string 
print(text) #print interprets control characters

print(text.split()) #file content is alwais a string

## other core type ##
X = set('spam')
Y = {'h','a','m'}
print(X,Y)

print(X & Y)

print(X|Y)

print(X-Y)

print({x ** 2 for x in [1,2,3,4]})

print(1/3)

import decimal 
decimal.getcontext
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction
f = Fraction(2,3)
print(f + 1)

a = 1>2 , 1<2
print(a)

print(bool('spam'))

x = ['yug',556]
print(type(x))

if type(x) == list:
    print('yes')

if type(x) == type([]):
    print('yes') 

if isinstance(x, list):
    print('yes')

class worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay  
    def lastname(self):
        return self.name.split()[-1]    
    def giverise(self, percent):
        self.pay *= (1.0 + percent)    

Bob = worker('Bob Smith', 50000)        
Sue = worker('Sue Jones', 60000)
 
print(Bob.lastname()) 
print(Sue.lastname())
Sue.giverise(0.10)

print(int(3.1415)) #truncates float into integer

print(float(3)) #convert integer into float





