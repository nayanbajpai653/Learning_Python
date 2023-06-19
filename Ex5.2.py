## Built in numeric tools ##
import math #module
print(math.pi , math.e) #common constants

print(math.sin(2 * math.pi / 180)) #sin,tangent,cosine

print(math.sqrt(144)) #square root
print(144 ** .5) #expression
print(pow(144 , .5)) #built in

print(math.sqrt(1234567890)) #large numbers
print(1234567890 ** .5)
print(pow(1234567890 , .5))

print(pow(2,4) , 2 ** 4) #exponantiation (power)

print(abs(-42.0) , sum((1,2,3,4))) #absolute value , summation

print(min(3,1,2,4) , max(3,1,2,4)) #minimum , maximum

print(math.floor(2.567) , math.floor(-2.567)) #floor (next lower integer)

print(math.trunc(2.567) , math.trunc(-2.567)) #truncate (drope decimal digits)

print(int(2.567) , int(-2.567)) #truncate (integer conversion)

print(round(2.567) , round(2.456) , round(2.567,2)) 

print('%f' % 2.567 , '{0:2f}'.format(2.567)) #round for display

import random
print(random.random()) #print's random number between 0 to 1 
print(random.random())

print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.choice(['Life of a Brain','Holi Grail','Meaning of Life']))
print(random.choice(['Life of a Brain','Holi Grail','Meaning of Life']))

## Decimal Type ##
print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal(1) / decimal.Decimal(7))

print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6.12)))