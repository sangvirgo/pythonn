p=input().strip()

def check(p):
    if len(p) < 10:
        return False
    num_cnt = 0
    for c in p:
        if not c.isalnum():
            return False
        if c.isdigit():
            num_cnt += 1
    if num_cnt < 2:
        return False
    return True

print(check(p), end='')
