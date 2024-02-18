"""Write a Python function to reverses a string if its length is a multiple of
4."""

def rev_str1(str1):
    if len(str1) % 4 == 0 :
        return str1[::-1]
    return str1
s1 = input("enter the string :")
result = rev_str1(s1)
print("the result is :",result)