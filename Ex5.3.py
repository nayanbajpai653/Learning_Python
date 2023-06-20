## SET ##
x = set('abcde') 
y = set('dbxyz')
print(x)
print(y)

print('c' in x) #membership

print(x - y) #difference

print(x | y) #union

print(x & y) #intersection

print(x ^ y) #symmetric difference 

print(x > y,x < y) #superset , subset

z = x.intersection(y) #same as x & y
print(z)

z.add('spam') #insert one item
print(z)

z.update(set(['X','Y'])) #merge:in-place union
print(z)

z.remove('b') #delete on item
print(z)

for item in set('abc'): print(item * 3)

s = set([1,2,3])
print(s | set([3,4])) # expresstions required both to be sets  

print(s.union([3,4])) #but methods allow any iterable 

print(s.intersection((1,3,5)))

print(s.issubset(range(-5,5)))

s1 = {1,2,3,4,5,6}
print(s1 & {1,3}) #intersection

print({1,3,5,7} | s1) #union

print(s1 - {1,3,5}) #difference 

print(s1 > {1,3}) #subset

print(s1 - {1,2,3,4}) #empty sets print differently

print(type({})) #because {} is an empty dictionary 

s = set() #initialize an empty set 
s.add(1.23)
print(s)
# print(s.add([1,2,3])) #only mutable abjects work in a set
# print(s.add({'a':1})) #unhabale type: 'list'

s.add((1,2,3)) #no list or dict,but tuple okay
print(s)

print(s | {(4,5,6),(1,2,3)}) #union:same as s.union(..)

print((1,2,3) in s) #membership: by complete values
print((1,4,3) in s) 


print({1,2,3}.union([3,4]))
print({1,2,3}.union({3,4}))
print({1,2,3}.union(set([3,4])))

print({1,2,3}.intersection((1,3,5)))

print({1,2,3}.issubset(range(-5,5)))

print({x ** 2 for x in[1,2,3,4]})

print({x for x in 'spam'}) #same as : set('spam')

print({c * 4 for c in 'spam'}) #set of collected expression results

s = {c * 4 for c in 'sapm'}
print(s | {'mmmm','xxxx'})

l = [1,2,1,3,2,4,5]
print(l)
L = list(set(l)) #remove duplicates
print(L)

engineers = {'bob','sue','ann','vic'}
managers = {'tom','sue'}

print('bob' in engineers) #is bob an engineer ?

print(engineers & managers) #who is engineer and manager ?

print(engineers | managers) #all proples either category

print(engineers - managers) #engineers who are not managers

print(managers - engineers) #managers who are not engineers

print(engineers > managers) #are all managers are engineers? (super set)

print({'bob','sue'} < engineers) #are both engineers?

print((managers|engineers) > managers) #all people is a super set of managers

print(managers^engineers) #who is in one but not both ?

print((managers|engineers) - (managers^engineers)) #intersection!