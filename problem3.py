#!/usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[]
y=[]
for i in adhoc :
    if i>5 :
        x.append(i)
    elif i<=2 :
        y.append(i)
print(f"Number which are greater than 5 are : {x}" )
print(f"Number which are less than 2 are : {y}" )
