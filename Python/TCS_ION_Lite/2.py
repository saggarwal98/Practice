def check_palindrome(input_list):
    new_list=[]
    j=""
    for i in input_list:
        j=i
        j=j.lower()
        newword=j[::-1]
        if newword==j:
            new_list.append(i)
    return new_list

if __name__=='__main__': 
    count=int(input())
    inp_str=[]
    for i in range(count):
      inp_str.append(input()) 
    output=check_palindrome(inp_str)
    if len(output)!=0:
        for i in output:
            print(i)
    else:
        print('No palindrome found')