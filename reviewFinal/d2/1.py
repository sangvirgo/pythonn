def func1(tmp_list):
    max_len=0
    current_len=1
    result=[]
    temp=[tmp_list[0]]
    for i in range(1, len(tmp_list)):
        if tmp_list[i]>tmp_list[i-1]:
            current_len+=1
            temp.append(tmp_list[i])
        else:
            if current_len>max_len:
                max_len=current_len
                result=temp[:]
            current_len=1
            temp=[tmp_list[i]]
    return result


# Test
input_list = [10, 25, 13, 18, 29, 33, 5, 31]
print("Output:", func1(input_list))