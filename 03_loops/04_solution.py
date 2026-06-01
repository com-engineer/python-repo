str=input("Enter the string:")

# String is immutable so we cannot reverse the string with following method
# x=0
# y=len(str)-1
# while(x<y):
#     temp=str[x]
#     str[x]=str[y]
#     str[y]=temp
#     x+=1
#     y-=1

revered_str=""

for c in str:
    revered_str=c+revered_str
    
print(f"The reversed string is {revered_str}")
