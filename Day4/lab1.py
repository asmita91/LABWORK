#program to determine if a year is leap year or not
year=int(input("enter the year::"))
if(year%400==0):
    print("leap year")
elif(year%4==0 and year%100!=0 ):
    print("leap year")
else:
     print("common year")
