#program to print its fractional part
import math
inp1=float(input("enter any number"))
x,y=math.modf(inp1)
print(x)
print(y)
