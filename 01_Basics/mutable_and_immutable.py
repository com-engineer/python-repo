# refer to the image of immutable and mutable

# String is immutable but below example shouws that string is changed  how???

# >>> username="gaurav"
# >>> username
# 'gaurav'
# >>> username="deepu"
# >>> username
# 'deepu'

# to understand the above let us see one example--->
# >>> x=10
# >>> x
# 10
# >>> y=x
# >>> y
# 10
# >>> x=15
# >>> x
# 15
# >>> y
# 10--->expected was 15 but we got 10 

# python internally store the reference of the value not the variable name

# Cannot change after creation

#Simple Rule
# Immutable
# int
# float
# string
# tuple

# → changes create NEW object

# Mutable
# list
# dict
# set

# → same object can be modified internally

# so vale remain as it is in the memory only the refernce of the value is changes  means now the username is pointing to "deepu" and y to "10" -->thisis the meaning of mutabl and immutable...where the value is not changed...and since there is no variable refering to the old value the garbage collector go and remove the value from memory
