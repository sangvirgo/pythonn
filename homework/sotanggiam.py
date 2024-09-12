t=int(input().strip())
"""
3
12342
23342
5678961
"""
for _ in range(t):
    n=input().strip()
    n=list(n)
    check=True
    decrease=False
    for i in range(len(n)-1):
        if (int(n[i]) == int(n[i + 1])):
            check = False
            break
        if decrease==False:
            if (int(n[i]) > int(n[i + 1])):
                decrease=True
        elif decrease==True:
            if (int(n[i]) > int(n[i + 1])):
                check=False
                break
    if check:
        print("YES")
    else:
        print("NO")