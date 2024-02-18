"""
Write a Python program to count the number of characters (character
frequency) in a string

"""
str1 = input("enter the string :")
s1 = input("enter the charachter that you want to check :")
count = 0
for i in str1 :
    if i in s1 :
        count += 1
print("The occurance is : ",count)

