def check_perfect_number(n):
    temp=1
    if n<1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if n/i==i:
                temp+=i
            else:
                temp+=i
                temp+=n//i
    return temp==n

n=int(input())
if check_perfect_number(n):
    print("YES")
else:
    print("NO")