t = int(input())


def calcFactofial(n):
    if n==0:
        return 1
    return n*calcFactofial(n-1)


for _ in range(t):
    n=input()
    temp=int(n)

    sum=0
    for char in n:
        sum+=calcFactofial(int(char))
    if sum==temp:
        print("Yes")
    else:
        print("No")