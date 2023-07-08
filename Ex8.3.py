# Storing native python objects with pickle
D = {'a' : 1 , 'b' : 2}

F = open('datafile2.pkl','wb')
import pickle 
pickle.dump(D, F)                              # Picle any object to file
print(F)

F.close()
print(F)

F = open('datafile2.pkl' , 'rb')  
E = pickle.load(F)                             # load any object from file
print(E)

print(open('datafile2.pkl').read())

# store and parsing packed binary data files
F = open('data.bin','wb')                      # open binary output file
from struct import *
data = pack('>bhl', 1, 2, 3)             # make packed binary data
print(data)

F.write(data)
F.close()
print(F)

from struct import *
values = unpack('>bhl',data)           # convert to python objects
print(values)

F = open('data.bin','rb')
data = F.read                                  # get packed binary data
print(data)

# object flexibility
L = ['abc', [(1, 2), ([3], 4)], 5]

print(L[1])

print(L[1][1])

print(L[1][1][0])

print(L[1][1][0][0])