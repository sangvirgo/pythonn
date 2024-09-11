"""
7
15
14
5
99
12345678
44444445
1445
"""


t = int(input().strip())

for _ in range(t):
    n=input().strip()
    if int(n) <= 10:
        print(n)
        continue
    n=list(n)
    lenN=len(n)
    for i in range(lenN-1, 0, -1):
        if int(n[i])>=5:
            n[i-1]=str(int(n[i-1])+1)
        n[i] = '0'
    if int(n[0])>=10:
        n[0]='0'
        n.insert(0, '1')
    print(''.join(n))
        