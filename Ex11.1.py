# While and For loops
# General Formula 
while True:
    print('type ctrl-c to stop me!')

x = 'spam'
while x:                                         # while x is not empety
    print(x, end=' ')
    x = x[1:]                                    # strip first character off x

a=0; b=10
while a < b:                                     # one way to code counter loops
    print(a, end=' ')
    a += 1                                       # or , a = a + 1

# break, continue, pass and loop else
# Pass
while True: pass                                 # type Ctrl-c to stop!

def func1():
    pass                                         # add real code here later

def func2():
    pass
    
# continue
x = 10
while x:
    x = x-1                                      # or, x-=1
    if x % 2 != 0: continue                      # odd? --skip print
    print(x, end=' ')

x = 10
while x:
    x = x-1
    if x % 2 == 0:
        print(x, end=' ')

# break
while True:
    name = input('Enter name:')
    if name == 'stop':break 
    age = input('Enter age:')
    print('Hello', name, '=>', int(age) ** 2)

# Loop else 
y = -4
x = y // 2                                       # for some y > 1
while x > 1:
    if y % x == 0:                               # remainder
        print(y, 'has factor', x)
        break                                    # skip else
    x -= 1
else:                                            # normal exit
    print(y, 'is prime')                         

found = False
while x and not found:
    if x[0]:                                     # value at front?
        print('Ni')
        found = True
    else:
        x = x[1:]                                # slice off front and repeat
    if not found:
        print('not found')

while x:                                         # exit when x empty
    if x[0]:
        print('Ni')
        break                                    # exit, go around else
    x = x[1:]
else:
    print('not found')                           # only here if exhausted x