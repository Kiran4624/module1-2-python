"""Write a Python function to insert a string in the middle of a string."""

def middle(str1,word):
    return str1[:3] + word + str1[-15:]
print(middle('hi this is python','kiran'))