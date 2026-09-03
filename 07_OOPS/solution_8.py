# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.


class Car:


    def __init__(self,brand,model):
        self.brand = brand
        self._model = model # _ "This is internal. Please don't access it directly."

    @property
    def model(self):
        return self._model

        
car = Car("brand1","model1")

print(car.model)
car.model = "model2"
print(car.model)
