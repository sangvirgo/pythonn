n=int(input())
s=[]

while n>0:
    s.append(int(n%10))
    n//=10

s=s[::-1]
for i in range(len(s)):
    print(s[i], end="")
    if i !=len(s)-1:
        print(" ", end="")


