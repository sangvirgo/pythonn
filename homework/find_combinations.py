from itertools import combinations
"""
4 
53 
[10, 20, 30, 40, 1, 2]
"""
def find_combinations(n, k, tmp_list) :
    result=[]
    for c in combinations(tmp_list, n):
        if sum(c)==k:
            result.append(list(c))
    return result

k=int(input().strip())
s=int(input().strip())
l = list(map(int, input().strip().strip('[]').split(',')))

combinations_found = find_combinations(k, s, l)
for i in range(len(combinations_found)):
    if i!=len(combinations_found)-1:
        print(combinations_found[i])
    else:
        print(combinations_found[i], end='')