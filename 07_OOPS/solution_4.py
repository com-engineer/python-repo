# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


class Car:

    def __init__(self,brand,model):
        self.__brand = brand  # _ protected while __ private
        self.model = model
# car = Car("BMW")

# print(car.model)      # BMW
# print(car.__model)    # ❌ AttributeError

# However, technically you can still access it:

# print(car._Car__model)

# So __ is not true privacy either. It mainly prevents accidental access and naming conflicts.
    def get_brand(self):
        return self.__brand

car = Car("brand1","model1")

print(car.model)
print(car.get_brand())
