def encode_rot13(s):
    result=[]
    for c in s:
        if c.isalpha():
            temp = ord(c)
            result.append(chr((temp-65+13)%26+65))
        else:
            result.append(c)
    return ''.join(result)

def encode_rot47(s):
    result=[]
    for c in s:
        result.append(chr((ord(c)-33+47)%94+33))
    return ''.join(result)

def save_encode(file, encode):
    f=open(file, 'r')
    temp=f.read()
    content=''
    if encode=='rot13':
        content=encode_rot13(temp)
    else:
        content=encode_rot47(temp)
    f.close()
    ff=open(file, 'w')
    ff.write(content)
    ff.close()


save_encode("file.txt", 'rot13')
'''
ABCDEFWXYZ012789

ABCDEFGHIJKLMN123*z
'''