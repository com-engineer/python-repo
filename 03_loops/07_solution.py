num=int(input("Enter the number: "))



while(num<1 or num>10):
    print("Wrong input please enter the valid input")
    num=int(input("Enter the number"))
    if(num>=1 and num<=10):
        print("You have entered valid input")
        break


