t=input()

sum=0
for c in t:
    if c=='7' or c=='4':
        sum+=1
if sum==4 or sum==7:
    print("YES")
else:
    print('NO')