t=int(input().strip())
"""
3
12345678
20000
22334455667788
"""

for _ in range(t):
    s=list(map(int, input().strip()))
    even=list(s[i] for i in range(len(s)) if i%2==0)
    odd=list(s[i] for i in range(len(s)) if i&1)

    sum_even=sum(even)
    sum_odd=0
    for i in odd:
        if i==0:
            continue
        if sum_odd==0:
            sum_odd=i
        else:
            sum_odd*=i

    print(sum_even, sum_odd)