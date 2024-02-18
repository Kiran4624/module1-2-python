"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""


x = input("enter the first string :")
y = input("enter the second string :")

str1 = x[:2] + y[2:] + " " +y[:2] + x[2:]

print("After swapping first two character is :",str1)