#program to sum 3 integers but if 2 values are same,sum is zero
inp1=int(input("enter any number::"))
inp2=int(input("enter any number::"))
inp3=int(input("enter any number::"))
if(inp1==inp2 or inp2==inp3 or inp3==inp1 or inp1==inp2==inp3):
    sum=0
else:
    sum=inp1+inp2+inp3
print(f"the sum is {sum}")
