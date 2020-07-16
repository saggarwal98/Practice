try:
    x=int(input())
    if x%2==0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("-1")