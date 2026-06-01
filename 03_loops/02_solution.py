sum=0
num=int(input("Enter the number:"))
# for n in range(num+1):
for n in range(1,num+1):
    if n%2==0:
        sum+=n

print(f"The sum of even number upto {num} is {sum}")
