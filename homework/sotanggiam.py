t=int(input().strip())
"""
4
12342
23342
5678961
123425
"""
for _ in range(t):
    n=list(input().strip())
    if len(n)<3:
        print("NO")
        continue

    increase=True
    ok=True
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            print("NO")
            ok=False
            break
        if increase and n[i]>n[i+1]:
            increase=False
        if not increase and n[i]<n[i+1]:
            print("NO")
            ok=False
            break
    if not increase and ok:
        print("YES")
    elif increase and ok:
        print("NO")