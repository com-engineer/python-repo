def debug(func):
    def wrapper(*args,**kwargs):
        args_value= ', '.join(str(arg) for arg in args)
        kwargs_value= ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    
    return wrapper

# basic function for hello def
# def debug(func):
#     def wrapper():
#         print("debug is done")
#         return func()
    
#     return wrapper


@debug
def hello():
    print("hello")

hello()

@debug
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}")
    # basic function we need to pass it to the tool

greet("chai",greeting="haaji ")