def check(s):
    if len(s)<3:
        return False
    if not s.lower().endswith('.py'):
        return False
    for c in s[:-3]:
        if not (c.isalpha() or c!='.' or c!='_'):
            return False
    return True

s=input()
if check(s):
    print('yes')
else:
    print('no')


'''
ghsdjhfsjfsdjh.py

sdfjhsajd343fhjsdf.py

asjfhajdfasd_.safasd1fhfjsdafhsj.py

'''