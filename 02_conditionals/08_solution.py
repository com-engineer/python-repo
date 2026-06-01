password='1234'

if len(password)<6:
    print("Weak")
elif len(password)>=6 and len(password)<=10:
    print("Medium")
else:
    print("Strong")