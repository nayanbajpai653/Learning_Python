# Files
# Files in action 
myfile = open('myfile.txt','w')                  # open for text output: create/empty 

myfile.write('hello text file\n')                # write a line of text: string
print(myfile)

myfile.write('goodbye text file\n')        
print(myfile)

myfile.close()                                   # Flush output buffers to disk
print(myfile)

myfile = open('myfile.txt')                      # open for text input: 'r' is default

print(myfile.readlines())                        # Read the lines back 

print(open('myfile.txt').read())                 # user friendly dicplay

for line in open('myfile.txt'):                  # use file iterators, not reads
    print(line, end='')
 
# storing and parsing python objects in files
X, Y, Z = 43, 44, 45                             # native python objects
S = 'spam'                                       # must be strings to store in file
D = {'a':1, 'b':2}
L = [1, 2, 3]

F = open('datafile.txt','w')                     # create output file
F.write(S + '\n')                                # terminate line with \n
F.write('%s,%s,%s\n' % (X, Y, Z))                # convert numbers into string
F.write(str(L) + '$' + str(D) + '\n')            # convert and separate with $
F.close()
print(F)

chars = open('datafile.txt').read()              # raw string display
print(chars)

F = open('datafile.txt')                         # open again
line = F.readline()                              # read one line 
print(line)

print(line.rstrip())                             # remove end of line 

line = F.readline()                              # next line from file
print(line)                                      # it's a string

parts = line.split(',')                          # split (parse) on commas
print(parts)

print(int(parts[1]))                             # convert from string to int

numbers = [int(P) for P in parts]                # convert all in list at once 
print(numbers)

line = F.readline()
print(line)

parts = line.split('$')                          # split (parse on $)
print(parts)

print(eval(parts[0]))                            # convert to any object type 

objects = [eval(P) for P in parts]               # Do for all in list
print(objects)