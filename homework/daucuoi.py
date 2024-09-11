"""
3
12321
1234512
10233211111
"""



t=int(input().strip())

def countDigit(n):
    res=0
    while(n>0):
        res+=1
        n//=10
    return res

for _ in range(t):
    n=int(input().strip())
    endNum=n%100
    n=n//(10**(countDigit(n)-2))
    if endNum==n:
        print("YES")
    else:
        print("NO")