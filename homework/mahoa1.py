"""
3
AACDDPQ
11111147g
1111111111
"""

t=int(input().strip())

for _ in range(t):
    s=input().strip()
    s=list(s)
    preChar=''
    result=''
    i=0
    while i<len(s):
        preChar=s[i]
        cnt=1
        i+=1
        while i<len(s) and s[i]==preChar:
            cnt+=1
            i+=1
        result=result+str(cnt)+preChar
    print(result)

