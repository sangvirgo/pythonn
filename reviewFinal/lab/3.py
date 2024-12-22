s1, s2=input().lower().strip().split()

dic1={}

for i in s1:
    if not i in dic1:
        dic1[i]=1
    else:
        dic1[i]+=1

for i in s2:
    if not i in dic1:
        dic1[i]=1
    else:
        dic1[i]+=1


ok=False
for k, v in dic1.items():
    if v!=2:
        print("False", end='')
        ok=True
        break
if not ok:
    print("True", end="")