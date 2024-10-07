if __name__=='__main__':
    s=input()
    k=int(input().strip())
    if len(s)&1:
        s=s[:len(s)-1]

    se=dict()
    for i in range(0,len(s), 2):
        temp=int(s[i:i+2])
        if temp not in se:
            se[temp]=1
        else:
            se[temp]+=1

    found=False
    for i in sorted(se.keys()):
        if se[i]>=k:
            print(f"{i} {se[i]}")
            found=True

    if not found:
        print("NOT FOUND")

"""
124356141111434356149
2

124356141111434356149
10
"""