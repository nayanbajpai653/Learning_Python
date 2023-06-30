# Changing lists in-place
# index and slicing assignments 
l = ['spam','spam','SPAM!']
l[1] = 'eggs'  # index assignment
print(l)

l[0:2] = 'eat','more'  # slice assignment: delete + insert
print(l)  # replace items 0,1

# list method calls
l.append('please')  # append method call: add item at end
print(l)

l.sort()  # sort list items ('S'<'e')
print(l)

l = ['abc','ABD','abe']  # sort with mixed case
l.sort()
print(l) 

l = ['abc','ABC','aBe']  # Normalise to lowercase
l.sort(key=str.lower)
print(l)

l = ['abc','ABC','aBe']
l.sort(key=str.lower, reverse=True)  # change sort order
print(l)

l = ['abc','ABC','aBe']
sorted(l, key=str.lower, reverse=True)  # sorting built-in
print(l)

l = [1, 2]
l.extend([3, 4, 5])  # add many items at end
print(l)

l.pop  # delete and return  last item
(print(l))

l.reverse()  # in-place reversal method
print(l)

list(reversed(l))  # reverse built-in with a result
print(l)

l = []
l.append(1)  # push in with a result
l.append(2)

l.pop()  # pop off stack
print(l)

l = ['spam','eggs','ham']
l.index('eggs')            # index of an object
print(l)

l.insert(1, 'tost') 
print(l)             # insert at position

l.remove('eggs')
print(l)          # delete by value 

l.pop(1)
print(l)  # delete by position

# other common list operations
del l[0]
print(l)  # delete one item

del l[1:]
print(l)  # delete entire section

l = ['already','got','one']
l[1:] = []
print(l)

l[0] = []
print(l)