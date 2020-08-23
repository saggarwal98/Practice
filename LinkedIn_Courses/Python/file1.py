str="abcdefghijklmnopqrstuvwxyz"
print(len(str))
print(str[0:1])
print(str[-3:-1])
print(str[0:-1])
for i in range(0,7,2):
    print(i)
def printfunc(a,b=10):
    print(a+b)
printfunc(3)
printfunc(3,4)
print(type(print("",end="")))
print(2**3)