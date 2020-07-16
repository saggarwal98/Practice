import sys
try:
    x=float(input("Enter a number "))
    y=1/x
    if x<0:
        raise ValueError()
    print()
    print("The reciprocal is: ",y)
except ValueError:
    print("ValueError Exception Occured")
    print("Only positive numbers are allowed")
except:
    print("Exception Occured")
    print(sys.exc_info()[0])
else:
    print("Program terminate successfully")
