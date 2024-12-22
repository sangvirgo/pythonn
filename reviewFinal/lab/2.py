s=input().lower().strip()

re_s=s[::-1]

if re_s!=s:
    print("False", end='')
else:
    print('True', end='')