# Comparison to the % formattion expression
print('%s = %s' % ('spam', 42))  

print('{0} = {1}'.format('spam', 42))

# the basics: with % intsead of format()
template = '%s , %s , %s' 
print(template % ('spam' , 'ham' , 'eggs'))  # by position

template = '%(motto)s , %(pork)s , %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))  # by key

print('%s , %s , and %s' % (3.14 , 42 , [1, 2]))  # arbitrary types

# adding keys , attributes and affsets
import sys
print('My %(spam)s runs %(platform)s' % {'spam': 'laptop' , 'platform': sys.platform})

print('My %(spam)s runs %(platform)s' % dict(spam = 'laptop' , platform = sys.platform))

somelist = list('SPAM')
parts = somelist[0] , somelist[-1] , somelist[1:3]
print('first = %s , last = %s , middle = %s' % parts)

# adding spacific formation
print('%-10s = %10s' % ('spam',123.4567))

print('%10s = %-10s' % ('spam',123.4567))

print('%(plat)10s = %(item)-10s' % dict(plat=sys.platform, item='laptop'))

# floating-point numbers
print('%s, %.3e, %g' % (3.14159, 3.14159, 3.14159))

print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))

# hex and octal, but not binary
print('%x, %o' % (255, 255))

# hardcoded references in both
print('My {1[spam]:<8} runs {0.platform:>8}'.format(sys, {'spam':'laptop'}))

print('My %(spam)-8s runs %(plat)8s' % dict(spam='laptop',plat=sys.platform))

# building data ahead of time in both 
data = dict(platform=sys.platform, spam='laptop')
print(data)

print('My {spam:<8} runs {platform:>8}'.format(**data))

print('My %(spam)-8s runs %(platform)8s' % data)