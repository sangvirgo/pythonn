t=int(input())

for _ in range(t):
    s=input()
    result=[]
    for i in range(0, len(s)):
        if 48 < ord(s[i]) < 58:
        # if ord('0') < ord(s[i]) <= ord('9'):
            num=int(s[i])
            result.append(s[i-1]*(num-1))
        else:
            result.append(s[i])
    print(''.join(result))

'''
2
A8
A2E1C4G3D1
'''