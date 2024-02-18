""" Write a Python program to get the Fibonacci series of given range."""


num = int(input("enter the number :"))

n1 = 0
n2 = 1
count = 0
if num <= 0:
    print("plz enter the positive number...")
else :
    for i in range(0,num):
        print(count,end = ' ')
        n1 = n2
        n2 = count
        count = n1 + n2

