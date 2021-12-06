#program to find sum of digits of a number
inp1=int(input("enter any number ::"))
sum1=0
while(inp1!=0):
    rem=inp1%10
    inp1=inp1//10
    sum1=sum1+rem
print(f"the sum of digits of a number is {sum1}")

    
