print('{0:d}'.format(999999999999))

print('{:,d}'.format(999999999999))
print('{0:,d}'.format(999999999999))

print('{:,d} {:,d}'.format(999999999999, 888888888888))

print('{:,.2f}'.format(296999.2567))

# extra features 
print('{0:b}'.format((2 ** 16) -1))

# print('%b' % ((2 ** 16) -1)) # ValueError

print(bin((2 ** 16) -1))

print('%s' % bin((2 ** 16) -1)[2:])

print('The {0} side {1} {2}'.format('bright', 'of', 'life'))

print('The {} side {} {}'.format('birght', 'of', 'life'))

print('The %s side %s %s '.format('bright', 'of', 'life'))

print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))

print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))

print('%.2f' % 1.2345)

print('%.2f %s' % (1.2345, 99))

print('%s' % 1.23)

print('%s' % (1.23,))

print('%s' % ((1.23,),))

print('{0:.2f}'.format(1.23455))

print('{0:.2f} {1}'.format(1.2345, 99))

print('{0}'.format(1.23))

print('{0}'.format((1.23,)))