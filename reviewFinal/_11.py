s=[]
dic = {}
p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
for i in range(len(p)):
    dic[p[i]] = i

while True:
    line=input()
    if line=='0':
        break
    n, s=line.split()
    n=int(n)
    result=[]
    for c in s:
        result.append(p[(dic[c]+n)%28])
    result=result[::-1]
    print(''.join(result))


'''
1 ABCD
14 ROAD
0

'''
