# Print Function
print()                                               # display a blank list

x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)                                        # print 3 objects per defaults

print(x, y, z, sep='')

print(x, y, z, sep=', ')                              # custom separator

print(x, y, z, end='')                                # suppress line break

print(x, y, z, end=''); print(x, y, z)                # two prints same output line

print(x, y, z, end='...\n')                           # custom line end 

print(x, y, z, sep='...', end='!\n')                  # multiple keywords

print(x, y, z, end='!\n', sep='...')                  # order dosen't matter

print(x, y, z, sep='...', file=open('data.txt','w'))  # print to a file

print(x, y, z)                                        # back to stdout 

print(open('data.txt').read())                        # display file text

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)

print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))

x = 'a'
y = 'b'
print(x, y)

print(x, y);print(x, y)

print(x + y)

print('%s...%s' % (x, y))

# The Python "hello world" program
print('hello world')

import sys                                            # printing hard way
sys.stdout.write('hello world\n')

# manual stream redirection
import sys 
print(sys.stdout.write(str(x) + ' ' + str(y) + '\n'))
 
sys.stdout = open('log.txt','a')                      # redirects prints to a file

print(x, y, z)