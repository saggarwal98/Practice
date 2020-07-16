inputlist1=[1,2,3,4,5]
outputlist1=[i**2 for i in inputlist1 if isinstance(i,int)]
print(outputlist1)
inputlist2=[['a','b'],['b','c'],['c','d']]
outputlist2=[j for i in inputlist2 for j in i]
print(outputlist2)

Names=["abc","bcde","efghij"]
Names_len_dict={key:len(key) for key in Names}
print(Names_len_dict)
Scores=[10,20,30]
Names_scores_dict={key:value for (key,value) in zip(Names,Scores)}
print(Names_scores_dict)
Names_filtered_dict={key:value for (key,value) in Names_len_dict.items() if value>3}
print(Names_filtered_dict)
print(Names_filtered_dict.items())

Names=["abc","bcde","efghij"]
new_Names=[i for i in Names if i!="bcde"]
print(new_Names)
print(type(new_Names))