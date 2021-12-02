#program to display minutes and hours in 24h digital clock
N=int(input("enter the value in minutes that is passed since midnight"))
hr=N//60
rem=N%60
minu=int(rem)
print(f"{hr}.{minu}")