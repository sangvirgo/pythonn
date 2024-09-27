def calcProductNum(n):
    result=1
    while n>0:
        result=result*(n%10)
        n//=10
    return result


def solve():
    t=int(input().strip())
    for _ in range(t):
        n=int(input().strip())
        arr=[int(item.strip()) for item in input().strip().split()]

        d={}
        for i in arr:
            p=calcProductNum(i)
            if p in d.keys():
                d[p].append(int(i))
            else:
                d[p]=[i]
        dSort=dict(sorted(d.items()))
        for k, v in dSort.items():
            temp=list(sorted(v))
            dSort[k]=temp

        for k, v in dSort.items():
            for i in v:
                print(i, end=' ')
        print()

solve()

"""
1
8
143 43 22 99 7 9 1111 10000000
"""

