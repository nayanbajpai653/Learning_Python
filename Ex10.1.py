# If Test And Syntax Rules
# Basic examples
if 1:
    print(True)

if not 1:
    print(True)
else:
    print(False)

# Multiway branching
x = 'killer rabbit'
if x == 'roger':
    print("how's jessica")
elif x == 'bugs':
    print("what's up doc?")
else:
    print("run away!, run away!")

choice = 'ham'
print({'spam': 1.25,                                       # a dictionary based 'switch'
       'ham': 1.99,                                        # use has_key or get for default
       'eggs': 0.99,
       'bacon': 1.10}[choice])

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}

print(branch.get('spam','Bad choice'))

print(branch.get('bacon','Bad choice'))

choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')