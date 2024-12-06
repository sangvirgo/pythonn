def check(s):
    for i in range(3, len(s)):
        if  s[i]!='_' and not s[i].isalpha() or s[i]!='.':
            return False
        return True

s=input()

s=s[::-1]
if s[0:3]!="yp.":
    print("no")
else:
    if check(s):
        print('yes')
    else:
        print('no')


'''
ghsdjhfsjfsdjh.py

sdfjhsajd343fhjsdf.py

asjfhajdfasd_.safasd1fhfjsdafhsj.py

'''