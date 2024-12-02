t=int(input())

for _ in range(t):
    s=input()
    result=[]
    i=0
    while i <len(s):
        previous_char=s[i]
        cnt=1
        i+=1
        while i < len(s) and previous_char == s[i] :
            i+=1
            cnt+=1
        result.append(str(cnt))
        result.append(previous_char)
    print(''.join(result))


'''
3
AACDDPQ
11111147g
1111111111
'''