#why we need tuple when we already have list?
#tuple is immutable and it is faster than list

# all the methods in the tuples is same as list only we cannot update the tuple once created

#unwrapping the tuple
# >>> tea_type 
# ('Black', 'Green', 'Oolaong')
# >>> (black,green,oolong)=tea_type  
# >>> black
# 'Black'

# nested tuple is similar to nested list 

# code snippet
# >>> tea_type=("Black","Green","Oolaong")
# >>> tea_type
# ('Black', 'Green', 'Oolaong')
# >>> tea_type[1:]
# ('Green', 'Oolaong')
# >>> tea_type[0]="Lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     tea_type[0]="Lemon"
#     ~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# >>> more_tea=("Herbal","Early "Grey")
#   File "<stdin>", line 1
#     more_tea=("Herbal","Early "Grey")
#                                    ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> more_tea=("Herbal","Early Grey") 
# >>> more_tea
# ('Herbal', 'Early Grey')
# >>> 
# >>> all_tea=tea_type+more_tea
# >>> all_tea 
# ('Black', 'Green', 'Oolaong', 'Herbal', 'Early Grey')
# >>> if "Green" in all_tea:
# ...  print("Present")
# ... 
# Present
# >>> more_tea=("Herbal","Early Grey","Herbal")
# >>> more_tea.count("Herbal")
# 2
# >>> tea_types 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     tea_types
# NameError: name 'tea_types' is not defined. Did you mean: 'tea_type'?
# >>> tea_type 
# ('Black', 'Green', 'Oolaong')
# >>> (black,green,oolong)=tea_type  
# >>> black
# 'Black'
# >>> type(tea_type)
# <class 'tuple'>
# >>> 