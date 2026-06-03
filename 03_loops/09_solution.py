items = ["apple", "banana", "orange", "apple", "mango"]

for ls in items:
    if items.count(ls)>1:
        print(f"The list contain the duplicate and 1st duplicate is: {ls} ")
        break
        