from itertools import combinations
from tempfile import tempdir


def find_combinations(m, h, tmp_list):
    result=[]
    for c in combinations(tmp_list, m):
        if sum(c)==h:
            result.append(list(c))
    for i in range(len(result)):
        if i != len(result)-1:
            print(result[i])
        else:
            print(result[i], end='')


n=int(input().strip())
k=int(input().strip())
arr=list(map(int, input().strip("[]").split(", ")))
find_combinations(n, k, arr)


'''
4 
53 
[10, 20, 30, 40, 1, 2]
'''


