#List mostly treated as array

states=["Pune","dhule","Pimperi"]
print(states[0])
print(states[:2])
print(states[-1:])
print(len(states))

for elem in states:
    print(elem)#each value will be printed on the new line so to print in one line we use end="anything"
    print(elem,end="-")

states[1]="Goa"
print(states)

#what happen when we change the element by this slicing lets see
states[1:2]="Rajasthan"
print(states)#-->['Pune', 'R', 'a', 'j', 'a', 's', 't', 'h', 'a', 'n', 'Pimperi']

#what  happened here --when i was assigning the new value through the slicing then the value is 
# substituted as array of character

#to avoid this we can pass the value as an arrray only like
states[1:2]=["Rajasthan"]
print(states)#['Pune', 'Rajasthan', 'a', 'j', 'a', 's', 't', 'h', 'a', 'n', 'Pimperi']

print(states[1:1])#-->[] no index is passed means if i do something like this
states[1:1]=["test","test"]#it will not replace any value or index instead it gets inserted and rest ofthe
#element get shofted
print(states)

states[1:3]=[]#insert nothing will delete test
print(states)


if "Pune" in states:
    print("Its present")

# states.append("")-->add element in the last
# states.pop()-->remove last element and return
# states.remove("")-->specific element and do not return
# states.insert(index,value)-->insert at specific index
# states_copy=states-->it give the reference of the states do not give the copy
# states_copy=states.copy()--.have different reference
# states_copy.append("Karnataka")
squared_nums=[x**2 for x in range(10)]#list comprehension
print(squared_nums)