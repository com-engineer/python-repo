# when we have fixed number of named arguements
# def print_kwargs(name,power):
#     print("Name ",name,"Power ",power)


# print_kwargs(name="shaktiman",power="lazer")
# print_kwargs(power="lazer",name="shaktiman")#order of output do not change
# print_kwargs("lazer","shaktiman")#-->here the order of arguement is changed so the ooutput order will also change


# in case of named arguement the order of output remains the same even if we change the order of passing the arguement

# +++++++++++++++++++++++++++++++++++++++++++++

# when we have variable named arguement

def print_kwargs(**kwargs):
    print(kwargs)
    print(**kwargs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="shaktiman",power="lazer",enemy="Dr. jackaal")