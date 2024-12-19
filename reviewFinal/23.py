def tic_so(x):
    tic=1
    while x!=0:
        tic=(x%10)*tic
        x//=10
    return tic

def solve():
    t=int(input().strip())
    for _ in range(t):
        n=int(input())
        arr=list(map(int, input().split()))
        arr.sort(key=lambda x: (tic_so(x), x))
        print(*arr)


solve()
'''
1
8
143 43 22 99 7 9 1111 10000000
'''