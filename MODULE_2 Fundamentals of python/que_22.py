"""Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string"""

def str1(s1):
    if len(s1) < 2:
        return ""
    else :
        return s1[:2] + s1[-2:]
my_str1 = input("enter the string :")
print("the new string is :",str1(my_str1))