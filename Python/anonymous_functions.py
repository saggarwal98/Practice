from functools import reduce

square=lambda x:x**2
print(square(5))

list1=[1,2,3,4]
list2=[10,100,1000,10000]
map_list=map(lambda x,y: y/x,list2,list2)
print(map_list)
print(type(map_list))
print(map(lambda x,y: y/x,list2,list2))

filter(lambda x : x>100 , list2)
print(list2)

print(reduce (lambda x,y:x*y,list1))