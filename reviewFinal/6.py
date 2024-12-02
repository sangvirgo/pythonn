def calc_round(data):
    if len(data)>1:
        data=list(data[::-1])
        for i in range(len(data)-1):
            if int(data[i]) >= 5:
                data[i]=str(0)
                data[i+1]=str(int(data[i+1])+1)
            else:
                data[i]=str(0)
        data=''.join(data[::-1])
        return int(data)
    else:
        return int(data)


t=int(input())

for _ in range(t):
    n=input()
    print(calc_round(n))



'''
7
15
14
5
99
12345678
44444445
1445
'''