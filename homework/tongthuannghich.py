t=int(input().strip())
"""
2
12341
22222222222222222222
"""
from functools import reduce
for _ in range(t):
    s=list(map(int, input().strip()))



    summ=reduce((lambda x, y: x + y), s)

    if summ<11:
        print("NO")
        continue

    if str(summ)==str(summ)[::-1]:
        print("YES")
    else:
        print("NO")