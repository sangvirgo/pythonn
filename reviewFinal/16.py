def calc_sum(data):
    data=int(data)
    result=0
    while data>0:
        result+=data%10
        data//=10
    return result

def check(data):
    temp=calc_sum(data)
    if temp<11:
        return False
    temp1=int(str(temp)[::-1])
    if temp==temp1:
        return True
    else:
        return False

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=input()
        if check(n):
            print("YES")
        else:
            print("NO")


'''
2
12341
22222222222222222222
'''