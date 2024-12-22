arr=list(input().strip().split(","))

temp=[]

ok=True
for i in arr:
    if i in temp:
        print("False", end="")
        ok=False
        break
    else:
        temp.append(i)
if ok:
    print("True", end="")