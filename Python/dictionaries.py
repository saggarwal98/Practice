dict1={"abc":10,"bcd":"4"}
print(dict1)
dict1["cde"]=5
print(dict1)
print(type(dict1))
del(dict1["bcd"])
print(dict1)
dict2=dict (abc=10,bcd=20,cde=30)
print(dict2)
for i in dict2:
    print(dict2[i])