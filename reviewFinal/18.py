t=int(input())
for _ in range(t):
    n=list(map(int, input()))
    sum_num=0
    multiplication=0
    for i in range(len(n)):
        if i&1 and n[i]!=0:
            # return the first value that it finds
            multiplication= multiplication or 1
            multiplication*=n[i]
        else:
            sum_num+=n[i]
    print(sum_num, multiplication)