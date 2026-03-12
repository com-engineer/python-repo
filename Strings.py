# # Strings in python

# #Strings are unicode character
# #Strings are immutable

# str1="Post Office" #Strings are also treated as list therefore qwe can access the character like list only
# print(str1)

# first_char=str1[0]#we can also use -ve index as well
# print(first_char)

# #remove post from post office use slice
# slice_str1=str1[0:4]
# print(slice_str1)
# print(str1[:])
# print(str1[:7])
# print(str1[2:])
# print(str1[2:5:7])

# ##Result
# # Post Office
# # P
# # Post
# # Post Office
# # Post Of
# # st Office
# # s

# print(str1.lower())
# print(str1.upper())
# #Remove spaces from start and end
# str2="   My Code   "
# print(str2.strip())

# #Replace strings
# print(str2.replace('My','Your'))

# str3= "Hey Good Morning, How are you"
# #convert above string into list--split
# print(str3.split())#-->['Hey', 'Good', 'Morning,', 'How', 'are', 'you']
# print(str3.split(", "))#-->['Hey Good Morning', 'How are you']

# print(str3.find("Good"))# if i don't get any value it will return -1 as result this is not the -ve index

# #count the occurance of the word int the sentence
# print(str3.count("My"))

# #Adding variables in the placeholder
# item="Book"
# qunatity=2
# Bougth="I have purchased {} quantity of the {} which i likes the most"
# print(Bougth)#I have purchased {} quantity of the {} which i likes the most
# print(Bougth.format(qunatity,item))#I have purchased 2 quantity of the Book which i likes the most

# products=["pencil","pen","Paper"]
# #convert above into string
# print(" ".join(products))#pencil pen Paper
# print("-".join(products))#pencil-pen-Paper

# print(len(str3))

# #printing the letters in the string
# for letter in str3:
#     print(letter)#prints vertiically

# sentence='He said,"Your vocubalory is very good" '#pythons  gets confused with this types of qoute 
#here we can use ''

chai="Masala\nchai"#-->this print the Masala and chai in next line not together
#this problem may arrise when dealing with the paths which includes lots of forward slash "\"
#so in that case we can use r"Masala\nchai" it willl consider whole senetence as one string 
chai=r"Masala\nchai" #this is row string
# chai=r"Masala\nchai\"-->it gives  erro due to presence present at the last
print(chai)
print("c:\\user\\pwd")#it skips the single slash  c:\user\pwd this is unicode escaping therefore we use  
# row string


text1="ToDay is Monday"
print("is" in text1)#-->True