n=int(input().strip())

def countUoc(n):
    cnt=0
    for i in range(1, int( n**0.5)+1, 1):
        if n%i==0:
            if n/i==i:
                cnt+=1
            else:
                cnt+=2
    return cnt==9


def solve(n):
    cnt=0
    for i in range(36, n, 1):
        if countUoc(i):
            cnt+=1
    return cnt

print(solve(n))


