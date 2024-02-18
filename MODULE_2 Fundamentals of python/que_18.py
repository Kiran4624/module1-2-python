"""Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged."""

str1 = input("enter the string :")

if len(str1) > 3 :
    if str1.endswith('ing') :
        str1 += 'ly'
    else :
        str1 += 'ing'
print("after changes the string is :",str1)