list_primes=[]
def hi():
    MAX = 10**5
    is_prime = [True] * MAX
    is_prime[0] = is_prime[1] = False

    for a in range(2, int(MAX ** 0.5)):
        if is_prime[a]:
            for b in range(a * a, MAX, a):
                is_prime[b] = False
    for i in range(MAX):
        if is_prime[i]:
            list_primes.append(i)


def check(n):
    hi()
    cnt=0
    for i in list_primes:
        temp=i**8
        if temp>=n:
            break
        cnt+=1
    for i in list_primes:
        for j in list_primes:
            if i<j:
                temp=i**2*j**2
                if temp<n:
                    cnt+=1
                else:
                    break
    print(cnt)

n=int(input())
check(n)