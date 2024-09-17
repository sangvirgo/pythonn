from curses.ascii import isalpha

s=input().strip().lower().replace(" ", "")

def checkPasswords(s):
    if len(s) < 10:
        return False
    cnt=0
    for i in s:
        if not i.isalnum():
            return False
        if i.isdigit():
            cnt+=1
    if cnt<2:
        return False
    return True

if checkPasswords(s):
    print("True", end="")
else:
    print("False", end="")