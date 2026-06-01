# mostly used in no-sql database its a "key"-"value" pair data structure
employee_info={
    'name':"Ayush",
    'mobile_No':8984743,
    'employeement_status':"Employed"
}

# print(employee_info)
# print(employee_info["name"])

# for key in employee_info:#it return keys not the value
#     print(key,"-",employee_info[key])

# for key,value in employee_info.items():#employee_info.items()-->It brings the items as key value pair together
#     # as now we are accessing both key and value
#     print(key,"-",value)

# #checks the presence of the key value in the dictionary
# if "mobile_No" in employee_info:
#     print("it has")

# #find the length of the dictionary
# print(len(employee_info))

# #add key
# employee_info["married"]=True
# print(employee_info)

# #pop
# employee_info.pop("married")
# print(employee_info)

# #remove last element
# employee_info.popitem()
# print(employee_info)

#remove reference of the key-value from the memory
# del employee_info["mobile_No"]

#make copy
employee_info_copy=employee_info.copy()
print(employee_info_copy)

#it can coontain nested dictionary  as well
tea_shop={
    "chai":{
        "Masala":"Spicy",
        "Ginger":"Zesty"
    },
    "Tea":{
        "Green":"Mild",
        "black":"strong"
    }
}

print(tea_shop)
print(tea_shop["chai"]["Ginger"])

squared_nums={x:x**2 for x in range(10)}
print(squared_nums)

#remove all the values inside the squared dictionary
squared_nums.clear()
print(squared_nums)

keys=["Masala","Ginger","Lemon"]#list
default_value="Delecious"
#construct new dictionary from above 
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)
new_dict=dict.fromkeys(keys,keys)
print(new_dict)
#Output of above code
# {'Masala': 'Delecious', 'Ginger': 'Delecious', 'Lemon': 'Delecious'}
# {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
