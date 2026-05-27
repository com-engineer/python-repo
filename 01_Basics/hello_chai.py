print("Hello world")

# declaring function
def chai(n):
    print(n)

chai(4);

one="Good Morning"
two="Good evening"
three="Good night"
# if above all are written after importing the original file and then we try to access it wi wont be able to do  we need to reload it as given below

# reloading inside the python cell
# from importlib import reload 
# >>> reload(hello_chai)

# we can direcyly import the folder 
# import hello_chai 


# making some update in the existance files 
# >>> import os
# >>> os.getcwd()-->method
# >>> import sys
# >>> sys.platform-->Property
# 'win32'

# 'C:\\Users\\Admin\\Desktop\\python-repo\\01_Basics'
# >>> for c in "chai":
# ... print(c)---> this will give us an error because we have not given the proper indentation to the print statement
#   File "<stdin>", line 2
#     print(c)
#     ^^^^^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for c in "chai":
# ...  print(c)
# ... 
# c
# h
# a
# i