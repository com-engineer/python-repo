# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car:

    count = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.count += 1
        

print(Car.count)
car = Car("brand1","model1")
print(Car.count)
car1 = Car("brand1","model1")
print(Car.count)
car2 = Car("brand1","model1")
print(Car.count)
car3 = Car("brand1","model1")
print(Car.count)
print(car3.count)

print(car.model)
print(car.brand)