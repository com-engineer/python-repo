# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:

    def battery_info(self):
        return "this is the battery info of electric car"

class Engine:

    def engine_info(self):
            return "this is the engine info of electric car"

class ElectricCar(Battery,Engine):

    def car_info(self):
        return "this is the car info"

car = ElectricCar()

print(car.car_info())
print(car.battery_info())
print(car.engine_info())
