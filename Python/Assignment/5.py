import sys
arg_number=len(sys.argv)
choice=input()
if choice=='a':
    i=1
    sum=0
    while i<arg_number:
        n=int(float(sys.argv[i]))
        sum+=n
    print(sum)
elif choice=='b':
    i=1
    highest=0
    while i<arg_number:
        n=int(sys.argv[i])
        if highest<n:
            highest=n
    print(highest)
elif choice=='c':
    i=1
    sum=0
    while i<arg_number:
        n=int(sys.argv[i])
        sum+=n
    print(sum/arg_number)
elif choice=='d':
    dict1={}
    i=1
    while i<arg_number:
        n=int(sys.argv[i])
        dict1[n]+=1
    highest=0
    for j in dict1:
        if dict1[highest]<dict1[j]:
            highest=j
    print(j)