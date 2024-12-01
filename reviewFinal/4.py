t=int(input())

def calFatorial(data):
    if data==0:
        return 1
    else:
        return data*calFatorial(data-1)


for _ in range(t):
    n=input()
    sum=0
    for i in range(0, len(n)):
        sum+=calFatorial(int(n[i]))
    if sum==int(n):
        print("Yes")
    else:
        print("No")
