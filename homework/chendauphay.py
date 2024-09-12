n=input().strip()

for i in range(len(n)):
    if(i%3==0 and i!=0):
        print(",", end='')
    print(n[i], end="")