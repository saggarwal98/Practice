def check_prime(n):
    if n<=1:
        return -1
    else:
        i=2
        while i*i<=n:
            if n==2 or n==3:
                return 1
            elif n%i==0:
                return 0
            else:
                i+=1
        return 1

def prime_composite_list(num_list):
    prime_list=[]
    composite_list=[]
    for i in num_list:
        val=check_prime(i)
        if val==1:
            prime_list.append(i)
        if val==0:
            composite_list.append(i)
    list_of_lists=[prime_list,composite_list]
    return list_of_lists

if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    result=prime_composite_list(inp)
    print(result)