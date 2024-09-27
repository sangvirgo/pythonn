from fcntl import FASYNC

"""
3
192.168.1.1
256.255.255.255
192.168..1
"""

def isValidIP(s):
    try:
        l=list(map(int, s.split(".")))
    except ValueError:
        return False

    # if ".." in s or not all((c.isdigit()) or c=="." for c in s):
    #     return False

    if len(l)!=4:
        return False
    for i in l:
        if i<0 or i>255:
            return False
    return True



t=int(input().strip())
for _ in range(t):
    s=input().strip()
    if isValidIP(s):
        print("YES")
    else:
        print("NO")