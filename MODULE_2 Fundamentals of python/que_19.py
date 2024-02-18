"""Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string"""

str1 = input("Enter a string: ")

not1 = str1.find('not')
poor1 = str1.find('poor')
# print(not1)
# print(poor1)
if not1 < poor1 :
    print(str1[:not1] + "good")