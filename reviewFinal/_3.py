MAX=int(1e6+1)
is_prime=[True]*MAX
is_prime[0]=is_prime[1]=False

def checkNum():
    for i in range(2, int(MAX ** 0.5), 1):
        if is_prime[i]:
            for j in range(i * i, MAX, i):
                is_prime[j] = False


t=int(input())
checkNum()

for _ in range(t):
    n=int(input())
    result=[]
    for i in range(13, n):
        reverseNum=int(str(i)[::-1])
        if is_prime[reverseNum] and is_prime[i] and reverseNum<=n and i!=reverseNum:
            result.append(i)
            result.append(reverseNum)
            is_prime[reverseNum]=False

    for val in result:
        is_prime[val]=True
        print(val, end=" ")
    print()



'''
2
40
100
'''