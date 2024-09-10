t=int(input())
MAX =1000001
is_prime=[True]*MAX
is_prime[0]=is_prime[1]=False

for i in range(2, int(MAX**0.5), 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j]=False


for _ in range(t):
    n=int(input())
    s={}
    for i in range(13, n, 1):
        reversed_i = int(str(i)[::-1])
        if is_prime[i] and is_prime[reversed_i] and i!=reversed_i and reversed_i<n: 
            s[i]=reversed_i
            is_prime[reversed_i]=False
    for key, value in s.items():
        is_prime[int(key)]=is_prime[int(value)]=True
        print(f"{key} {value}", end=' ')
    print()  