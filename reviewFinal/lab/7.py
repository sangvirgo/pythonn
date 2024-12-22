arr=list(input().strip().split(", "))
arr=map(int, arr)
dic_result={}

for i in arr:
    if not i in dic_result:
        dic_result[i]=1
    else:
        dic_result[i]+=1

num=tuple(dic_result.keys())
re=tuple(dic_result.values())
print(num, re, end="")