"""Write a Python function that takes a list of words and returns the length
of the longest one."""

str1 = input("enter the string :")
s1 = str1.split()
longest = len(s1)
for i in s1 :
    if len(i) > longest :
        longest = len(i)
print("the longest string is :",longest)