# String formation method call #
# The Basics
template = '{0} , {1} and {2}'  # by position
print(template.format('sapm', 'ham', 'eggs'))

template = '{motto} , {pork} and {food}'  # by keyword
print(template.format(motto='spam' , pork='ham' , food='eggs'))

template = '{0} , {pork} and {food}'  # by both
print(template.format('spam' , pork='ham' , food='eggs'))

print('{motto} ,  {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

x = '{motto} ,  {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(x)

print(x.split(' and '))

y = x.replace('and' , 'but under no circumstances')
print(y)

# Adding keys, attributes and offsets
import sys
print('My {1[spam]} run {0.platform}'.format(sys, {'spam':'laptop'}))

print('My {config[spam]} run {sys.platform}'.format(sys=sys,
                                                     config={'spam':'laptop'}))

somelist = list('SPAM')
print(somelist)

print('first={0[0]}, third={0[2]}'.format(somelist))

print('first={0}, last={1}.formate(somelist[0], somelist[-1])')  # [-1] fails in fmt

parts = somelist[0], somelist[-1], somelist[1:3]  # [1:3] fails in fmt
print('first={0}, last={1}, middle={2}'.format(*parts))

print('{0:10} = {1:10}'.format('spam', 123.4567))

print('{0:>10} = {1:>10}'.format('spam', 123.4567))

print('{0.platform:>10} = {1[item]:<10}'.format(sys, dict(item='laptop')))

print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))

print('{0:x}, {1:0}, {2:b}'.format(255, 255, 255))  # hex,octal,binary

print(bin(255), int('11111111', 2), 0b111111111)  # other to/form binary

print(hex(255), int('FF',16), 0xff)  # other to/from hex

print(oct(255), int('377',8), 0o377)  # other to/from octal 

print('{0:.2f}'.format(1 / 3.0))  # parameters hardcoded

print('%.2f' % (1 / 3.0))

print('0:.{1}f'.format(1 / 3.0, 4))  # take value from arguments

print('%.*f' % (4, 1 / 3.0))  # ditto for expression

print('{0:.2f}'.format(1.2345))  # string method

print(format(1.2345, '.2f'))  # built in function

print('%.2f' % 1.2345)  # expression