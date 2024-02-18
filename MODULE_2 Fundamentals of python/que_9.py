# """Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.
# """

x=int(input("enter the first number :"))
y=int(input("enter the second number :"))
z=int(input("enter the third number :"))

if x==y or y==z or z==x:
    print("the sum is :",0)
else:
    print("the sum is :",x+y+z)