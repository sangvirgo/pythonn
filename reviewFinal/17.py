is_prime=[True]*500
is_prime[0]=is_prime[1]=False

for i in range(2, int(500**0.5)):
    if is_prime[i]:
        for j in range(i*i, 500, i):
            is_prime[j]=False

def sol(n):
    for i in range(0, len(n)):
        if is_prime[n[i]] and not is_prime[i]:
            return False
        elif not is_prime[n[i]] and is_prime[i]:
            return False
    return True

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = list(map(int, input()))
        if sol(n):
            print("YES")
        else:
            print("NO")
