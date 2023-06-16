#### LIST ####
l = ['spam',123,12.3]

print(len(l)) # number of items in list 

print(l[0]) # indexing by position

print(l[:-1]) # string slicing

print(l + [4,5,6]) # adding items in list 

l.append('il') # add object at the end of list
print(l)

print(l.pop(2)) # delete an item in lsit

# print(l[99]) #show error when list index is out of range

m = ['bb','aa','cc']
m.sort()  
print(m)
m.reverse()
print(m) 

#### NESTING ####
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(M) #print matrix in list form

print(M[1]) #print's second row

print(M[1][2]) #print's the value of third row third column

col = [row[1] for row in M ] #print's the value in second column
print(col) 

print([row[1] + 1 for row in M]) #adds 1 in second column

print([row[1] for row in M if row[1] % 2 == 0]) #filter out add num

print([M[i][i] for i in [0,1,2]]) #print digonal in matrix 

print([a * 2 for a in 'sdss' ]) #print two times a value in string

print({i:sum(M[i]) for i in range(3)}) # creating key value for lsit

print({sum(row) for row in M}) #create a set of row sum

print(list(map(sum,M))) #map sum over in items in m

#### DICTIONARIES ####
D = {'Food':'Spam','quantity':4,'color':'pink'}
print(D)

print(D['Food']) #fetch value of key food

D['quantity'] += 1  #add 1 to quantity value
print(D['quantity'])

d = {}
d['name'] = 'Bob'  #creates key by assignment
d['job'] = 'dev'
d['age'] = 40
print(d)

print(d['name'])

rec = { 'name':{'first':'Bob' , 'last':'Smith'},
      'job':['dev','mgr'],
       'age':40.5
}
print(rec['name']['last']) #Index the nested dictionary

print(rec['job'][0]) #index the nested list 

rec['job'].append('janitor') #expend bob's job decription in-place 
print(rec)

a = {'B':1 ,'C':2 ,'A':3 }
ks = list(a.keys()) #unorderd key list 
ks.sort() #sorted key list 
print(ks)

for key in ks:  #iterate through short keys list 
    print(key, '=>', a[key])

for key in sorted(a): #
    print(key, '=>', a[key])

for c in 'spam':
    print(c.upper())   

x = 4
while x > 0:    
    print('spam!' * x )
    x -= 1

squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)

squares = []
for x in [1,2,3,4,5]: #this is what list comprehantion does 
    squares.append(x ** 2) #both run the itration protocall internally 
    print(squares)

x = {'a':1, 'b':2, 'c':3}
x['e'] = 4
print(x)

if not 'f' in x:
    print('missing')











