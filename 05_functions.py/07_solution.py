def sum_all(*args):#args is jus the variable we can use any variable
    print(args)#-->return tuples
    for i in args:
        print(i*2)
    return sum(args)# so we are actually passing tuple to sum(tuple) which return the sum of all the element in the tuple 

print(sum_all(1,2,3))
# print(sum_all(1,2,34,5))#we can take these as an array and iterate over it
# print(sum_all(1,2,34,5,7,8,9))

