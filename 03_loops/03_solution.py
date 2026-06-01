num=int(input("Enter the number:"))

for n in range(1,11):
    if n==5:
        continue
    else:
        print(f"{num} X {n} = {num*n}")