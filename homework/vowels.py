s=input().strip().lower().replace(" ", "")

def checkVowels(s):
    cnt=0
    for i in s:
        if i in "aeiou":
            cnt+=1
    print(cnt, end="")

checkVowels(s)

