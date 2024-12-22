k=int(input())
arr=list(map(int, input().split()))

def rotate(k, tmp_list):
    tmp_list=tmp_list[len(tmp_list)-k::]+tmp_list[:len(tmp_list)-k]
    for i in range(len(tmp_list)):
        if i!=len(tmp_list)-1:
            print(tmp_list[i], end=" ")
        else:
            print(tmp_list[i], end="")

rotate(k, arr)

'''
3
1 3 2 5 7


2 5 7 1 3
'''