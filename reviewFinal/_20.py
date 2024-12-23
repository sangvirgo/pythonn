dic_num={}
a=[]

for i in range(60):
    for j in range(40):
        for k in range(30):
            temp=2**i*3**j*5**k
            if not temp in dic_num:
                dic_num[temp]=1
                a.append(temp)

a.sort()

def binary_search(l, r, x):
    while l <=r:
        mid=(l+r)//2
        if a[mid]==x:
            return mid+1
        elif a[mid]>x:
            r=mid-1
        else:
            l=mid+1
    return -1

for _ in range(int(input())):
    temp=int(input())
    hi=binary_search(0, len(a)-1, temp)
    if hi!=-1:
        print(hi)
    else:
        print("Not in sequence")


'''
11
1
2
6
7
8
9
10
11
12
13
14

'''
