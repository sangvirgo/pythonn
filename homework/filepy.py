def check(f):
    if len(f)<1 or len(f)>128:
        return False

    if not f.endswith('.py'):
        return False

    for c in f[:len(f) - 3]:
        if not (c.isalnum() or c == '_'):
            return False

    return True

f=input().strip().lower()

if check(f):
    print('yes')
else:
    print('no')