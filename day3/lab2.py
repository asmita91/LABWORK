#program to display marks,grades,percentage
sub1=float(input("enter the marks of maths::"))
sub2=float(input("enter the marks of english::"))
sub3=float(input("enter the marks of nepali::"))
sub4=float(input("enter the marks of science::"))
total=sub1+sub2+sub3+sub4
per=float((total/4))
print(f"the total marks obtained is {total} and percentage secured is {per}")
if(per>70):
    print("you secured distinction")
elif(per>60 and per<70):
    print("you secured first division")
elif(per>40 and per<60):
    print("you passed")
else:
    print("you failed")

