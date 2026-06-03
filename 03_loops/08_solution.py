import math

num = int(input("Enter the number: "))

if num <= 1:
    print("Not Prime")
else:
    prime = True

    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not Prime Number")