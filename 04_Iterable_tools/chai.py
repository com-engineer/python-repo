import time

print("Chai is here")

username="Gaurav"

print(username)

# reading this file in the python cell

# >>> f=open("chai.py")
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print("Chai is here")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'username="Gaurav"\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''

# file is also iterable
# >>> for line in open('chai.py'):
# ...  print(line,end='') 
# ... 
# import time
# print("Chai is here")
# username="Gaurav"
# print(username)

# >>> mylist=[1,2,3,4]
# >>> i=iter(mylist)
# >>> i
# <list_iterator object at 0x000001BCE85D05B0>

# >>> i.__next__()
# 1
# >>> i
# <list_iterator object at 0x000001BCE85D05B0> now i still have same value

# >>> f = open('chai.py')
# >>> i=iter(f)we do not have to do explicitly since it has already have done internally unlike 
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True

# unlike list>>> list=[12,2,3,4,5]
# >>> iter(list) is list
# False