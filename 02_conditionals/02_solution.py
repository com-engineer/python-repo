import random
# day="wednesday"
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day=random.choice(days)
# age=25
age=int(input("Enter your Age: "))

if(day=="Wednesday"):
    if age<18 :
        print("discounted price($8-$2) on wednesday: $6")
    else:
        print("discounted price($12-$2) on wednesday: $10")
else:
    if age<18 :
        print(f"Day: {day} Movie price: $8")
    else:
        print(f"Day: {day} Movie price: $12")
