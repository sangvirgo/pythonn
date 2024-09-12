n=int(input())
import math

def countNum(num):
    res=0
    num=abs(num)
    while num:
        num//=10
        res+=1
    return res

lenN=countNum(n)

endN=int(abs(n)%10)
beginN=int(abs(n)//(10**(lenN-1)))

if n>0:
    n=n-endN+beginN
    n=n+(endN-beginN)*(10**(lenN-1))
else:
    n=abs(n)
    n=n-endN+beginN
    n=n+(endN-beginN)*(10**(lenN-1))
    n=-n
print(n)