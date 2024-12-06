def check(data):
    if len(data)<3:
        return False
    data = list(map(int, data))
    res=max(data)
    found=False
    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            return False
        elif data[i]==res:
            found=True
        else:
            if not found and data[i]>data[i+1]:
                return False
            elif found and data[i]<data[i+1]:
                return False
    return True

if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=input()
        if check(n):
            print("YES")
        else:
            print("NO")

'''
3
12342
23342
5678961
'''