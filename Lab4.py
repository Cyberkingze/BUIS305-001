import math

for i in range (0,11):
    print(i)
for i in range (1,11):
    print(i)
for(i) in range  (1,11,2):
    print (i)

radius=float(input('enter radius'))
area=math.pi*radius*radius
print(area)

length  =float(input('Enter length'))
breadth =float(input('Enter breadth'))
if(length and breadth>0):
    print('Valid input')
    area=length*breadth
    print(area)
else:
    print('Invalid input')


