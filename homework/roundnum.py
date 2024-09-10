t=int(input())

for _ in range(t):
    n=input()

    if int(n)>=5 and int(n)<=10:
        print(10)
    elif int(n) < 5:
        print(n)
    else :
        n=list(n)
        for i in range(len(n)-1, 0, -1):
            if(int(n[i])>=5 and int(n[i])<=9):
                n[i-1]=str(int(n[i-1])+1)
                n[i]='0'
            elif int(n[i])<5:
                n[i]='0'
            elif int(n[i])==10:
                n[i]='0'
                temp=i-1
                if temp<0:
                    n='1'+n
                else:
                    n[i-1]=str(int(n[i-1])+1)
    print(n)
        