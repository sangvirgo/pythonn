import functools

n=int(input())

listS=list(map(float, input().split()))

maxS=max(listS)
minS=min(listS)

listF=list(filter(lambda p:p!=maxS and p!=minS, listS))

sumS=functools.reduce(lambda a, b: a+b, listF)

print(round(sumS/(len(listF)), 2))




'''
6
6.75 8 9.2 7.25 7.75 6.75
'''