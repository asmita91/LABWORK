#program to take password and check if it is correct or not
uname=input("enter your username::")
pwd=input("enter your password::")
for i in range(3):
    uname1=input("enter the user name::")
    pwd1=input("enter the password")
    if uname ==uname1 and pwd == pwd1:
        print("Logged in Successfully")
        break
    else:
        print("Invalid credentials!!")
else:
     print("Attempts finished!!")
