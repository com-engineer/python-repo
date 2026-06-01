pet='dog'
age=1

if pet=='dog':
    if age<2:
        print(f"The age of the {pet} is {age} so give them puppy food")
    else:
        print("Plz give valid inputs")
elif pet=='cat':
    if age>5:
        print(f"The age of the {pet} is {age} so give them Senior cat food")
    else:
        print("Plz give valid inputs")
else:
    print("Plz give valid inputs")