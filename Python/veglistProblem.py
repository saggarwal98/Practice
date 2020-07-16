class Vegetables:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Store:
    def __init__(self,name):
        self.name=name

    def func1(self,veglist):
        newlist=[]
        for i in veglist:
            newlist.append(i.name)
        dictnew={}
        newlist.sort()
        donelist=[]
        for i in newlist:
            if i in donelist:
                continue
            else:
                listnew=[]
                key=i[:1]
                listnew.append(i)
                donelist.append(i)
                innerlist=newlist.copy()
                innerlist.remove(i)
                for j in innerlist:
                    key1=j[:1]
                    if key1==key:
                        listnew.append(j)
                        donelist.append(j)
                    else:
                        break
                listnew.sort()
                dictnew[key]=listnew
        for i in dictnew:
            print(i)
            for j in dictnew[i]:
                print(j)

if __name__ =="__main__":
    count=int(input())
    vegobjlist=[]
    while count>0:
        name=input()
        price=float(input())
        quantity=int(input())
        vegobj=Vegetables(name,price,quantity)
        vegobjlist.append(vegobj)
        count-=1
    sname=input()
    storeobj=Store(name)
    # print(vegobjlist)
    storeobj.func1(vegobjlist)