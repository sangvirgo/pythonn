l=list(map(int, input().strip().replace(",", "").split()))
d={}

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


ele=tuple(d.keys())
result=tuple(d.values())

print(ele, result)
