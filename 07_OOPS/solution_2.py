# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"full name of the car is: {self.brand} {self.model}"

car = Car("brand1","model1")

print(car.model)
print(car.brand)
print(car.full_name())