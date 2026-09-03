# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:


    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "This is the car class having attribute brand and model"
        
car = Car("brand1","model1")

print(car.general_description())
print(Car.general_description())

# ## Static Method vs Normal Method in Python

# A method inside a class does **not automatically become a static method** just because we call it using the class name.

# ### Example

# ```python
# class Car:

#     def general_description():
#         return "This is a car"

# print(Car.general_description())
# ```

# This works because when we call the method using the **class directly**, Python does not automatically pass an object (`self`).

# However:

# ```python
# car = Car()
# car.general_description()
# ```

# will cause an error because when a method is called using an **object**, Python automatically passes that object as the first argument.

# Conceptually:

# ```python
# car.general_description()
# ```

# becomes:

# ```python
# Car.general_description(car)
# ```

# But `general_description()` does not accept any argument.

# ---

# ## Static Method

# ```python
# class Car:

#     @staticmethod
#     def general_description():
#         return "This is a car"
# ```

# `@staticmethod` tells Python:

# > Do not automatically pass `self` or `cls` to this method.

# Therefore, a static method can be called using both:

# ```python
# Car.general_description()
# ```

# and:

# ```python
# car.general_description()
# ```

# without receiving an automatic `self`.

# ### Key Point

# A static method is **not defined by whether we can call it without creating an object**.

# The real purpose of `@staticmethod` is:

# > **It prevents Python from automatically passing the instance (`self`) or class (`cls`) to the method.**

# A static method is simply a function placed inside a class because it is logically related to that class, but it does not need instance data or class data.

# 