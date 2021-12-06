#program to take password and check if it is correct or not
for i in range(3):
    uname=input("enter the user name::")
    pwd=input("enter your password")
    if uname == 'asmita91' and pwd == 'lifeisgood':
        print("Logged in Successfully")
        break
    else:
        print("Invalid credentials!!")
else:
     print("Attempts finished!!")
