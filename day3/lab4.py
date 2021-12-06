#program to print the smallest among 3 integer
inp1=int(input("enter first number::"))
inp2=int(input("enter second number::"))
inp3=int(input("enter third number::"))
if(inp1<inp2 and inp1<inp3):
    print(f"the first number {inp1} is smallest")
elif(inp2<inp1 and inp2<inp3):
    print(f"the second number {inp2} is smallest")
else:
    print(f"the third number {inp3} is smallest")