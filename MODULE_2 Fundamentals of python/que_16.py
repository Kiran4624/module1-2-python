"""Write a Python program to count the occurrences of each word in a
given sentence"""

str1 = input("enter the sentence :")
str1 = str1.split( )
i = 0
count = 0
while i < len(str1):
    count = 0
    for j in str1:
        if str1[i]==j:
            count += 1     
    print((str1[i]),"The occurance is :",count)
    i += 1