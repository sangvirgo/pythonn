def calcDigit(n):
    summ=0
    while n>0:
        temp=n%10
        summ+=temp
        n//=10
    return summ

def solve():
    n=int(input().strip())
    arr=[int(item.strip()) for item in input().strip().split()]
    d={}
    for i in range(n):
        s=calcDigit(arr[i])
        if s in d.keys():
            d[int(s)].append(int(arr[i]))
        else:
            d[int(s)] = [int(arr[i])]
    di=dict(sorted(d.items()))
    for k, v in di.items():
        temp=list(sorted(v))
        di[k]=temp

    for k, v in di.items():
        for i in v:
            print(i, end=' ')

    print()




t=int(input().strip())

for _ in range(t):
    solve()


"""
1
8
143 43 22 99 7 9 1111 10000000
"""