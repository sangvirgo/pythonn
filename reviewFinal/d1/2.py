def check_perfect_number(n):
    if n==0:
        return True
    if n==1:
        return False
    temp=1
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            temp+=i
            if n/i!=i:
                temp+=n//i
    return temp==n

def list_perfect_number(n):
    result=[]
    i=0
    while len(result)!=n:
       if check_perfect_number(i):
           result.append(i)
       i+=1
    return result

n=int(input())
# if check_perfect_number(n):
#     print("YES", end="")
# else:
#     print("NO", end="")

result=list_perfect_number(n)
print(result)
