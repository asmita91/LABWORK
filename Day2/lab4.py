#program to determine how many apples each student gets and how many remains in the basket
N=int(input("enter the number of students::"))
K=int(input("enter the total number of apples they have::"))
get=K//N
rem=K%N
print(f"the total number of apples distributed equally is {get} and the apples that remain in the basket is {rem}.")