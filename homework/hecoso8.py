def split_string(s):
    temp=3-len(s)%3
    if temp==3: temp=0
    digit= temp*'0'+s

    l=[digit[i:i+3] for i in range(0, len(s), 3)]
    return l

def convert_to_oct(s):
    result=0
    j=0
    for i in range(2, -1, -1):
        digit=int(s[j])
        result+=2**i*digit
        j+=1
    return str(result)


def main():
    s = input()
    digit=split_string(s)
    result=''
    for i in digit:
        result+=convert_to_oct(i)


    print(int(result))


if __name__ == "__main__":
    main()
"""
1010
11001100
110011001
"""