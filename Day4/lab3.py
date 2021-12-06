#program to take data of employees and assign work areas according
age=int(input("enter your age::"))
gen=(input("enter your gender i.e. F for female and M for male::"))
if(gen=="F"):
    print("you will work in urban area")
elif(gen=="M" and (age>20 and age<40)):
    print("you can work anywhere")
elif(gen=="M" and (age<40 and age>60)):
    print("you can work only on urban area")
else:
    print("ERROR")


