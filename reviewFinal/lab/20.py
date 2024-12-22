def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
    return True

def cnt_degit(n):
    cnt=0
    while n>0:
        cnt+=1
        n//=10
    return cnt


def circular_num(n):
    end_num=n%10
    begin_num=int(n/10)
    cnt=cnt_degit(n)
    return end_num*10**(cnt-1)+begin_num

def check(n):
    if not is_prime(n):
        return False
    for i in range(cnt_degit(n)):
        if not is_prime(circular_num(n)):
            return False
    return True

n=int(input().strip())
print(check(n), end="")