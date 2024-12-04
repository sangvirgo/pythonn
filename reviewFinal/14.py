is_prime=[True]*10000000
is_prime[0]=is_prime[1]=False

for i in range(2, int(10000000**0.5)):
    if is_prime[i]:
        for j in range(i * i, 10000000, i):
            is_prime[j] = False

t=int(input())

def calc_num(data):
    result=0
    while data>0:
        result=result*10+data%10
        data//=10
    return result

for _ in range(t):
    n=int(input())
    print(is_prime[799])
    if is_prime[n] and is_prime[calc_num(n)]:
        print("YES")
    else:
        print("NO")


'''
2
123
997
'''