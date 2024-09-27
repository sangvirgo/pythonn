n=int(input().strip())

def sieve(n):
    isPrime=[True]*(n+1)
    isPrime[0]=isPrime[1]=0
    for i in range(2, int(n**0.5), 1):
        if isPrime[i]:
            for j in range(i*i, n, i):
                isPrime[j]=False
    prime=[i for i in range(2, n+1, 1) if isPrime[i]]
    return prime



def solve(n):
    prime=sieve(int(n**0.5))
    cnt=0
    for i in prime:
        if i**8<=n:
            cnt+=1
        else:
            break

    for i in range(len(prime)):
        for j in range(i+1, len(prime)):
            if prime[i]**2 * prime[j]**2<=n:
                cnt+=1
            else:
                break
    return cnt


print(solve(n))

