

def check(a):
    if len(a)!=4:
        return False
    for i in a:
        if i.isdigit():
            if int(i) < 0 or int(i) > 255:
                return False
        else:
            return False
    return True

def solve():
    t=int(input())
    for _ in range(t):
        arr=list(input().split("."))
        if check(arr):
            print("YES")
        else:
            print("NO")


solve()
'''
2
192.168.1.1
256.255.255.255
'''