try:
    x=int(input())
    i=1
    while i<=10:
        print("%d X %d = %d"%(x,i,x*i))
        i+=1
except ValueError:
    print("-1")