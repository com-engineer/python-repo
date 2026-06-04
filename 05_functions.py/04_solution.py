import math

def area_circum(r):
    circm=2*math.pi*r
    area=math.pi*r**2
    return circm,area

c,a=area_circum(5)
print("circm: ",c,"area: ",a)