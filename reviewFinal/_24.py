import re


def solve():
    lines=[]
    while True:
        try:
            line=input().strip()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break

    content=" ".join(lines)
    sequences=re.split(r'[.?!]', content)
    for t in sequences:
        t=t.strip()
        if t:
            sequence=t[0].upper()+t[1:].lower()
            print(' '.join(sequence.split()))
solve()
'''
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
'''