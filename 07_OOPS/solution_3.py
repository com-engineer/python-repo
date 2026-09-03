# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model



class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


electric_car1 = ElectricCar("brand2","model2","564hp")
print(electric_car1.model)
print(electric_car1.brand)
print(electric_car1.battery_size)