#program to determine the number of desk to be replaced 
grp1=int(input("enter the total number of students in group1::"))
grp2=int(input("enter the total number of students in group2::"))
grp3=int(input("enter the total number of students in group3::"))
#only 2 stds can sit in 1 desk
if(grp1%2==0):
    desk1=grp1/2
else:
    desk1=(grp1//2+1)
if(grp2%2==0):
    desk2=grp2/2
else:
    desk2=(grp2//2+1)
if(grp3%2==0):
    desk3=grp3/2
else:
    desk3=(grp3//2+1)
total=int(desk1+desk2+desk3)
print(f"the total number of desk required is {total}")
