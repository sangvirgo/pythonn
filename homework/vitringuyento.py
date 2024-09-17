t=int(input().strip())

MAX=501
is_prime=[True]*MAX
is_prime[0]=is_prime[1]=False

"""
2
14239567
2314514535353
"""

for i in range(2, int(MAX**0.5), 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j]=False

for _ in range(t):
    s=list(map(int, input().strip()))

    ok=True
    for i in range(len(s)):
        if not is_prime[i] and is_prime[int(s[i])] or (is_prime[i] and not is_prime[int(s[i])]):
            ok=False
            break

    if ok:
        print("YES")
    else:
        print("NO")