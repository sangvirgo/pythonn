def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
    return True

def func1(tmp_list):
    tmp=list(filter(lambda x: check_prime(x), tmp_list))
    max_len=0
    current_len=1
    temp=[tmp[0]]
    result=[]
    for i in range(1, len(tmp)):
        if tmp[i]>tmp[i-1] and check_prime(tmp[i]) and check_prime(tmp[i-1]):
            current_len+=1
            temp.append(tmp[i])
        else:
            if max_len<current_len:
                max_len=current_len
                result=temp[:]
            current_len=1
            temp=[tmp[i]]
    return result



input_list = [10, 25, 13, 18, 29, 33, 5, 31]
print("Output:", func1(input_list))