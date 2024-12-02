t=int(input())

for _ in range(t):
    n=input()
    size_num=len(n)
    n=int(n)
    begin_num=int(n/(10**(size_num-2)))
    end_num=n%100
    if not begin_num==end_num:
        print("NO")
    else:
        print("YES")



'''
3
12321
1234512
10233211111
'''