n=int(input())


def cnt_degit(n):
    cnt=0
    while n>0:
        cnt+=1
        n//=10
    return cnt

cnt=cnt_degit(n)
end_num=n%100
begin_num=int(n/(10**(cnt-2)))

n=n-(end_num-begin_num)
n=n-(-end_num+begin_num)*10**(cnt-2)

print(n, end='')
