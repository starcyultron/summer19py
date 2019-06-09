#!/usr/bin/python3
import os
import crypt
x=input("Enter your username : ")
x.isalpha()
if x.isalpha() == True:
    uname=x
    upass="hello" + uname
    print(upass)
    #The encryption module seems to solve the obvious security leak,
    #but I still don't know whether even the exposed encrypted password is safe or not.
    ucrypt=crypt.crypt(upass,"123")
    os.system("sudo useradd -m -p "+upass+" "+uname)
    print("User created Successfully")
else :
    print("Username is not in specified format")