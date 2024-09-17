n=input().strip()

result=[]
cnt=0
for i in range(len(n)-1, -1, -1):
    result.append(n[i])
    cnt+=1
    if cnt%3==0 and i!=0:
        result.append(",")
        cnt=0

print(''.join(result[::-1]), end='')