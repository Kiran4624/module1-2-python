"""Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.
"""
def test(x, y):
    if x == y or x + y == 5 or x - y == 5:
        return True
    else:
        return False

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

result = test(x, y)
print(result)

