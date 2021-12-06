#program to determine if the student can attend exam according to their attendance
held=int(input("enter the number of classes held"))
attended=int(input("enter the number of cls attended"))
per_of_attended =((attended/held)*100)
print(f"the class attended is {per_of_attended}")
if(per_of_attended<75):
    print("you will not be allowed to sit in exam ")
else:
    print("you will be allowed to sit in exam ")
