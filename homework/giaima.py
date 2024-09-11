"""
2
A8
A2E1C4G3D1
"""


t=int(input().strip())


for _ in range(t):
    s=input().strip()
    s=list(s)
    result=''
    preChar=''
    for i in range(len(s)):
        if s[i].isalpha():
            preChar=s[i]
        elif s[i].isdigit():
            lenN=int(s[i])
            result=result+preChar*lenN
    print(result)