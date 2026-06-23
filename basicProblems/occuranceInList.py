a = [1,5,3,7,5,3,5,7,4,3,8,9,7,8,5,6,4,6]

dic ={}

for i in a:
    if (i in dic.keys()):
        dic[i]+=1
    else:
        dic[i]=1
        
        
print(dic)