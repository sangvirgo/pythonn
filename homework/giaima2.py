"""
1 ABCD
14 ROAD
0
"""


P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
indexP={}
for i in range(len(P)):
    indexP[P[i]]=int(i)

while True:
    line=input().strip()
    if line=='0':
        break
    n, s=line.split(' ')
    n=int(n)
    s=list(s)

    result=''
    for i in range(len(s)):
        index=(indexP[s[i]]+n)%28
        result+=P[index]
    print(result[::-1])

