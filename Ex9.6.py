# Automatic stream redirection
import sys
temp = sys.stdout                                # save for restoring later
sys.stdout = open('log2.txt','a')                 # redirect print to a file

print('spam')                                    # print go to file, not here

print(1, 2, 3)
sys.stdout.close()                               # flush output to disk
sys.stdout = temp                                # restore original stream

print('back here')                               # print show up here again 

print(open('log2.txt').read())                    # result of earlier prints

x = 'spam'
y = 99
z = ['eggs']

a = 56
b = 'ham'
c = 7

log = open('log2.txt','a')
print(x, y, z, file=log)                         # print to a file like object
print(a, b, c)                                   # print to original stdout

log = open('log2.txt','w')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()

print(7, 8, 9)

print(open('log2.txt').read())

import sys
sys.stderr.write(('Bad!' * 8) + '\n')

print('Bad!' * 8, file=sys.stderr)

X = 1; Y = 2                                     # print: the easy way
print(X, Y)

import sys
sys.stdout.write(str(X) +  ' ' + str(Y) + '\n')  # print: the hard way

print(X, Y, file=open('temp1','w'))                        # send text to file 

open('temp2','w').write(str(X) +  ' ' + str(Y) +'\n')      # send to file manually 

print(open('temp1','rb').read())                           # binary mode for bytes

print(open('temp2','rb').read())

# version neutral printing

print('spam')

print('spam', 'ham', 'eggs')                               # there are multiple arguments

print('%s %s %s' % ('spam', 'ham', 'eggs'))

print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))