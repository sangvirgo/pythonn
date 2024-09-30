def main():
    t=int(input().strip())
    arr=[int(i.strip()) for i in input().split()]

    ans=None
    v=0
    for i in arr:
        res=0
        for j in arr:
            res+=abs(i-j)
        if ans is None or ans>res :
            ans=res
            v=i

    print(ans, v)

if __name__ =="__main__":
    main()




"""
8
13 5 8 7 9 15 26 34
"""