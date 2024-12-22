
n=int(input())

am=False
if n<0:
    am=True
    n=abs(n)
def cnt_degit(n):
    cnt=0
    while n>0:
        cnt+=1
        n//=10
    return cnt

cnt=cnt_degit(n)

begin_num=int(n/10**(cnt-1))
end_num=n%10

n=n-(end_num-begin_num)
n=n-(begin_num-end_num)*10**(cnt-1)

if am==True:
    print(-n, end="")
else:
    print(n, end="")