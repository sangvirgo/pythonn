if __name__=='__main__':
    s=input()
    if len(s)&1:
        s=s[:len(s)-1]

    se=set()
    for i in range(0,len(s)-2, 2):
        se.add(int(s[i:i+2]))
    se=sorted(se)
    print(" ".join(map(str, se)))



"""
124356141111434356149
"""