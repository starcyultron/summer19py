import datetime
x=input("Enter your Name")
y=int(input("Enter your Age"))
now=datetime.datetime.now()
now=now.year
z= now + (95 - y)
print(f"Year in which you will be of 95 years : {z}" )
