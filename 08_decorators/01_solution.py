# "Decorators" are like tolls on the highways where every vehicle have to pass through it anf if any charges has to be taken then it is taken depending on the type of vehicle...jus like that we pass the function throught the pipe where if any task required to do on thet will be done other wise the fiuntion will easily pass through the pipe without any changes...so this is the basic concept of "Decorators"

import time
# "Decorator k eliye function ke andar function banana hota hai like below"
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer# now after this when i call example_function it will definitely pass through the timer function now this function will be passed to the timer function
def example_function(n):
    time.sleep(n)

example_function(2)