# 1.re.search()
# Searches the first occurrence of a pattern anywhere in the string.

# re.search(pattern, string)

# import re
# text = "My phone number is 9876543210"
# match = re.search(r"\d+", text)
# if match:
#     print(match.group())


# 2.re.match()
# Checks only from the beginning of the string.

# import re
# text = "Hello World"
# print(re.match(r"Hello", text))
# print(re.match(r"World", text))


# 3.re.findall()
# Returns all matches as a list.

# import re

# text = "I have 2 apples and 15 oranges."

# numbers = re.findall(r"\d+", text)

# print(numbers)