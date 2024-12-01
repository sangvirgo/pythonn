
'''
2
12ab29cd19
ab123gh456cd
'''

t=int(input())

for _ in range(t):
    n=input().strip()

    temp=''
    minNum=float('-inf')
    for c in n:
        if c.isdigit():
            temp+=c
        else:
            if temp:
                minNum = max(minNum, int(temp))
                temp=''
    if temp:
        minNum=max(minNum, int(temp))
    print(minNum)

