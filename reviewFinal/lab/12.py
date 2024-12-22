from itertools import combinations

def cre_sub_lists(n):
    result=[]
    for r in range(1, len(n)+1):
        result.extend(combinations(n, r))
    return [list(i) for i in result]

n=list(map(int, input().strip('[]').split(',')))

re=cre_sub_lists(n)
for i in range(len(re)):
    print(re[i], end='')
    if i!=len(re)-1:
        print(", ", end="")