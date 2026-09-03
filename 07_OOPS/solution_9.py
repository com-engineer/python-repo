# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar


class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model



class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("brand2","model2","564hp")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
