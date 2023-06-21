## Fraction Type ##
from fractions import Fraction 
x = Fraction(1, 3) #numerator , denominator
y = Fraction(4, 6) #simplified to 2,3 by gcd

print(x)
print(y)

print(x + y)
print(x - y)  #result are exart: numerator , denominator 
print(x * y)

print(Fraction('0.25'))
print(Fraction('1.25'))
print(Fraction('0.25') + Fraction('1.25'))

# numeric accuracy
a = 1/3.0  # only as accuate as floating-point hardware 
print(a)   

b = 4/6.0 #can lose precision over calculations 
print(b)

print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3) #this should be zero (close but not exact)

from fractions import Fraction
print(Fraction(0.1) + Fraction(0.1) + Fraction(0.1) - Fraction(0.3))

print(Fraction(6, 12)) # automatically simplified
print(Fraction(1, 3))
print(Fraction(1, 3) + Fraction(6, 12))

print(1000/123456790)
print(Fraction(1000, 1234567890))

print((2.5).as_integer_ratio()) #float onject method

f = 2.5  # conver float -> fraction: two args
z = Fraction(*f.as_integer_ratio())  # same as Fraction(5, 2) 

print(x + z) # x from prior intrection # 5/2 + 1/13 = 15/6 + 2/6 = 17/6

print(float(x)) #convert fraction -> float
print(float(z)) 

print(x + z)
print(17/6)

print(Fraction.from_float(1.75)) # convert float -> fraction: other way
print(*(1.75).as_integer_ratio())

print(x + 2) # Fraction + int -> Fraction

print(x + 2.0) # Fradction + float -> float

print(x + (1./3)) # Fraction + float -> float

print(x + (4./3))

print(x + Fraction(4, 3)) # Fraction + Fraction -> Fraction 

print(4.0 / 3) 

print((4.0 / 3).as_integer_ratio()) # precision loss from float

a = x + Fraction(*(4.0 / 3).as_integer_ratio()) # 5/3 (or close to it!)
print(a)

print(22517998136852479 / 13510798882111488) # 5/3 (or close to it)

print(a.limit_denominator(10)) #simplify to closest fraction 