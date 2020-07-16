str1=input()
str2=input()
if str1==str2:
    print("Both are equal")
elif str2 in str1:
    print(str2+" is a substring of "+str1)
else:
    print(-1)