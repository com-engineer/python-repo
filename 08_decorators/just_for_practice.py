# Write a decorator wish that prints "Good Morning!" before any function runs.
# import math
# def wish(func):
#     def wrapper(*args,**kwargs):
#         print("Good Morning!")
#         result=func(*args,**kwargs)
#         return result
#     return wrapper

# @wish
# def add(a,b):
#     return a+b

# @wish
# def sub(a,b):
#     return abs(a-b)

# print(add(3,4))
# print(sub(3,5))

# Write a decorator shout that converts the return value of a function to UPPERCASE.

# def shout(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result.upper()
#     return wrapper

# @shout
# def upper_case(str):
#     return str

# print(upper_case("gaurav"))

# Write a decorator run_twice that runs the function 2 times.
def run_twice(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(result)
        print(result)
        return result
    return wrapper
@run_twice
def alert():
    return "alert!! fire!! fire! please get out of here!"

alert()