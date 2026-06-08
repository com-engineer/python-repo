class Car:
    #solution for 6th que class variables
    total_car=0

    def __init__(self,brand,model):# self means jisne bhi call kiya
        # self.brand=brand
        self.__brand=brand#for encapsultion solution __brand basically makes it "private" so to access it we use get
        self.__model=model
        #init also known as constructor

        Car.total_car+=1#Q.6 now how to access it?

    #getters and setters
    def get_brand(self):# for encapsultion solution
        return self.__brand
    def set_brand(self,brand):# for encapsultion solution
        self.__brand=brand
    
    def car_full_name(self):
        return f"{self.__brand} {self.__model}"
    
    #polymorphism solution
    def fuel_type(self):
        return "petrol or deisel"
    
    #Q.7
    @staticmethod#-->decorators
    def general_description():
        return "Cars are means of transport"
    
    # Q.8
    # @property
    def model(self):
        return self.__model

    
   


    

my_car= Car("Toyoto","Corolla")

safari = Car("Tata","safari")#polymorphism
print(safari.fuel_type())#polymorphism

#Q.6 solution
# safariThree = Car("Tata","Nexon")#Q6
# print(safari.total_car)# we generally do not access this using the object let us see why
# test=Car("test","test")
# print(test.total_car)
# print(Car.total_car)


# print(my_car.brand)
# print(my_car.model)
# print(my_car.car_full_name())

# my_new_car = Car("Tata","safari")
# print(my_new_car.car_full_name())


#3 Inheritance-solution

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    #polymorphism solution
    def fuel_type(self):
        return "Electric charge"

my_Tesla = ElectricCar("Tesla","Model S","85KWH")
# print(my_Tesla.model)
# print(my_Tesla.brand)
# print(my_Tesla.car_full_name())
# print(my_Tesla.battery_size)

#4. Encapsulation-solution==>adding access modifier
# print(my_Tesla.get_brand())
# # my_Tesla.set_brand("BMW")
# print(my_Tesla.get_brand())

#5.Polymorphism-solution
# print(my_Tesla.fuel_type())

#6 solution
# print(test.total_car)
# print(Car.total_car)

#Q.7 static method-no need to create the object to access it
# print(my_car.general_description())# gives output=Cars are means of Transport
# Lets us try to access via class name
# print(Car.general_description())# gives error
# if i remove self then the method can be accessible through class

# to make any method static we use @staticmethod keyword without "self" keyword but there is question when i tried to acces without mentioning the static keyword it was working fine so what is the difference lets see

# answer:when we do not use @staticmethod and self then we can access it using class name only not with any object
# but when we use @saticmethod keyword object and class both can use it without using self 

#Q.8 use property decorator
# @property lets you access a method like an attribute (obj.name) instead of calling it like a function (obj.get_name()).

# model is still accessible so it can be overridden
# so we need to make it read only...so one can think of making it also a private but we have seen that we can still override using "setter method"

# my_car.model="city"
# print(my_car.model)# even though declare a variable private by __var we have to call by obj.var not by obj.__var 
# print(my_car.model())# this gives error after declaring "property decorator"


# Q.9 
# print(isinstance(my_Tesla,Car))
# print(isinstance(my_Tesla,ElectricCar))
# true


# Q.10 Multiple inheritance  is possible
class Batteru:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar2(Batteru,Engine,Car):
    pass

my_new_tesla=ElectricCar2("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())