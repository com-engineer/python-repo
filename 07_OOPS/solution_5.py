# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.


class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "diesel"


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric"


electric_car1 = ElectricCar("brand2","model2","564hp")
print(electric_car1.fuel_type())

car = Car("brand1","model1")
print(car.fuel_type())
