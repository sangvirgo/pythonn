s=input()

cnt=0
for c in s:
    if c in 'aoeui':
        cnt+=1

print(cnt, end="")