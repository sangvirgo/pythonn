k=int(input().strip())
l=list(map(int, input().strip().split()))
"""
3
1 3 2 5 7

1
1 3 2 5 7
"""
def rotate(k, tmp_list):
    n=len(tmp_list)
    return tmp_list[n-k: n]+tmp_list[:n-k]

result=rotate(k, l)
for i in range(len(result)):
    print(result[i], end='')
    if(i!=len(result)):
        print("", end=" ")
