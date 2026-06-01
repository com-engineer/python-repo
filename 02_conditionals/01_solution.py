# age=25
age=int(input("Provide me your age:"))

if(age<13):
    print("Child")
elif(age>=13 and age<=19):
    print("Teanager")
elif(age>=20 and age<=59):
    print("Adult")
else:
    print("Senior")
