t=int(input())

for _ in range(t):
    s=input()
    res=float('-inf')
    temp=''

    for char in s:
        if char.isdigit():
            temp+=char
        else:
            if temp!='':
                res=max(res,int(temp))
                temp=''
    if temp:
        res=max(res,int(temp))
    print(res)