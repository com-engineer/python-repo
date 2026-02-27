# Numbers are the group of Object that has wide variety like sets are also included in the number
# Basic Arithematic Operayions +,-*,/,//,% etc
# we use paranthesis to avoid the confusion in case of multiple arithmetic operations in single expression
# operator overloading is common in every language where it automatically checks the data types of operands


# precision
result=1/3.0

repr('chai')
# -->"'chai'"
str('chai')
# -->'chai'
print('chai')
# chai

# comparison==> and, or,>,<,<=,>=,==

1==2<3
# ??ans false,1 is also treated as "true",the question can be written in the form 1==2 and 2<3

# >>> x=2 
# >>> y=3
# >>> z=4
# >>> x
# 2   
# >>> y
# 3   
# >>> z
# 4   
# >>> x,y
# (2, 3)
# >>>

import math

math.floor(3.5) #we get lower closest value...3
math.trunc(2.0) #take me towards 0....2

#python can also handle the imaginary numbers as well
2+1j

# Octal literals 0o20-->16
# Hexa literals 0xFF-->255
# binary literals 0b1000-->8

# to convert the integer into the different form
# oct(64),hex(64),bin(64)..same like int(3.4)=3
# int('64',8)--convert to octal

# bit wise operator
# right shift >> left shift << 

# import random
# random.random()-->gives the random value between 1 and 0
# random.randint(a,b)-->random integer between a and b
# random.choice(list)
# random.shuffle(list)

# Python magic.....How it is happening
# decimal precision is problematic so for that we can import decimal
# >>> 0.1+0.1+0.4
# 0.6000000000000001
# >>> 0.1+0.1+0.1
# 0.30000000000000004
# >>> 0.1+0.1+0.1-0.3
# 5.551115123125783e-17
# >>> (0.1+0.1+0.1)-0.3 
# 5.551115123125783e-17

# >>> from decimal import Decimal 
# >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
# Decimal('0.3')
# >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
# Decimal('0.0')

# similarly we have frractions 
# import fraction
# >>> from fractions import Fraction 
# >>> myFra=Fraction(7,2) 
# >>> myFra
# Fraction(7, 2)

# SET is also the part of the numbers
# >>> setone & {1,2} 
# {1, 2}
# >>> setone | {1,2} 
# {1, 2, 3}
# # >>> setone-{1,2,3}
# >>> setone-{1,2,3} 
# set()
# >>> type({}) 
# <class 'dict'>

# >>> True+5
# 6