# The map() function in Python applies a specific function to every item in an iterable (like a list or tuple) and returns a map object iterator.

# The syntax for the map() function is structured as follows:
        # map(function,iterable1,iterable2...)
# function: The operation you want to apply to each item.
# iterable: The collection of items (lists, tuples, strings) to be processed

# Because map() returns an iterator, you must wrap it in a data structure like list() or tuple() to see the actual results immediately

# Examples
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4]
result = map(square, numbers)

print(list(result)) 

# ++++++++++++++++++++++++++++++++++++++++++++++
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)

print(list(result)) 
# Output: [2, 4, 6, 8]

# +++++++++++++++++++++++++++++++++++++++++++++++
list_a = [1, 2, 3]
list_b = [10, 20, 30]

# Adds corresponding items from both lists together
result = map(lambda x, y: x + y, list_a, list_b)

print(list(result)) 
# Output: [11, 22, 33]