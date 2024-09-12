t=int(input().strip())
"""
2
123
997
"""
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

for _ in range(t):
    n=input().strip()
    m=n[::-1]
    result=gcd(int(n), int(m))
    if result==1:
        print("YES")
    else:
        print("NO")