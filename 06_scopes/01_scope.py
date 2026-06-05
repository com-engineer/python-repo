# username="gaurav"

# {}-->define the scope generally but in python there is no {} braces so we deal with indentation which represent the scope

# definig scope means like building home 

# variable define in the scope can't be access outside but vice versa is possible

# def func():
#     username="chai"

# func()
# print(username)

x=99

# def func1():
#     # global x #--->we do not have to use this. it is just for demonstration of like we can make update global variable like this 
#     #without the global it would have printed the original value only outside the scope
#     #we should never update the global variable we just access it
#     x=12

# func1()
# print(x)

# def func2():
#     x=88
#     def f2():
#         print(x)#-->what would be the output 99 or 88??
#         #-->it print 88 so it follows the climbing of ladder with respect to scope
#     # f2()
#     return f2#--returning complte definition of the function

# result=func2()
# result()#--it still print the 88 why? it was suppose to be something else 
#-->This is happening because of closure
# "closure" -- along with the definition the reference associated with the variables is also returned....so its like packing the definition in the bag along with the reference of the variables associated with...also used as factory functions


def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f=chaicoder(2)
g=chaicoder(3)

print(f(2))
print(g(3))

