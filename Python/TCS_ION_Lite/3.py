def find_Novowels(input_list):
    new_list=[]
    j=""
    for i in input_list:
        j=i
        j=j.lower()
        if j.find("a")>-1:
            continue
        if j.find("e")>-1:
            continue
        if j.find("i")>-1:
            continue
        if j.find("o")>-1:
            continue
        if j.find("u")>-1:
            continue
        new_list.append(i)
    return new_list

if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=find_Novowels(inp_str)
    if len(output)!=0:
        print('Strings without vowels:')
        for i in output:
            print(i)
    else:
        print('No string found')