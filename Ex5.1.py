##### Numeric Type #####

a = 3  #name created
b = 4 
print(a + 1) #adding 3+1

print(a - 1) #subtract 3-1

print(b * 3) #multiplaction 4x3

print(b / 2) #division 4/2

print(a % 2) #remainder 

print(b ** 2) #power 4^2

print(a + 4.0) #mixed type conversions
print(2.0 ** b) 

print(b / 2 + a) #same as ((4/2)+3)

print(b / (2.0 + a)) #same as (4/(2.0+3))

print(b / (2.0 + a)) #same as (4/(2.0+3))

num = 1 / 3.0 #print rounds
print(num)

print('%4.2f' % num) #string formatting expretion

print('{0:4.2f}'.format(num)) 

# Comparisons:Normal and Chained 
print(1<2) #less then

print(2.0 >= 1) #greater than or equal

print(2.0 == 2.0) #equal value

print(2.0 != 2.0) #not equal value

x = 2
y = 4
z = 6
print(x<y<z) #chained comparisons 
print(x<y and y<z)

print(x<y>z)
print(x<y and y>z)

print(1<2<3.0<4)
print(1>2>3.0>4)

print(1==2<3) #same as: 1 == 2 and 2<3

# Division: Classic , Floor and True
print(10/4) #keeps remainder

print(10//2) #truncates remainder

print(10/4.0) #keeps remainder

print(10//4.0) #truncates to floor

import math
print(math.floor(2.5))

print(math.floor(-2.5))

print(math.trunc(-2.5))

print(math.trunc(2.5))

print(math.trunc(5/-2)) #truncates instead of floor

print(5/2 , 5/-2)

print(5//2 , 5//-2) #truncates to floor:rounds to first lower integer

print(5/2.0 , 5/-2.0)

print(5//2.0 , 5//-2.0) #ditto for floats, through result is float too

print(5/float(-2))

print(math.trunc(5/float(-2)))