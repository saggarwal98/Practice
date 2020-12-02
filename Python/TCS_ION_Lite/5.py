def getIndex(num_list,n):
    try:
        val1=num_list.index(n)
        del num_list[val1]
        return num_list.index(n)+1
        # new_list=[]
        # for i in range(len(num_list)):
        #     if i!=val1:
        #         new_list.append(num_list[i])
        # print(new_list)
        # return new_list.index(n)+1
    except ValueError:
        return 0

if __name__=="__main__":
    count=int(input())
    numlist=[]
    for i in range(count):
        numlist.append(int(input()))
    val=int(input())
    print(getIndex(numlist,val))