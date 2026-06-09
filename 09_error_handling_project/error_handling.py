# >>> x=('Masala','lemon','ginger')
# >>> y=enumerate(x)# after this y will have the list of above tuples in the key-value form as given below
# >>> y
# <enumerate object at 0x000002A5B5C3F100>
# >>> list(y)
# [(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]


# file opening
# fle = open('test.py','w')# write mode where it make new file so be cautious

file=open('youtube.txt','w')

try:
    file.write("Chai aur code")
finally:
    file.close()

# file handling
with open('youtube.txt','w') as file:# it automatically handle the try, finally block
    file.write("Chai aur Python")