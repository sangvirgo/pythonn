from itertools import combinations



def get_k_skips_n_grams(k, n, input_str):  #to list
    grams=[]
    for i in range(0, len(input_str)):
        grams.append(input_str[i:i+k+n])

    result=[]
    for c in grams:
        for r in combinations(c, n):
            result.append(list(r))
    temp=[]
    for c in range(len(result)-2):
        if not result[c] in temp:
            temp.append(result[c])

    for c in range(len(temp)):
        if c!=len(temp)-1:
            print(' '.join(temp[c]), end=", ")
        else:
            print(' '.join(temp[c]), end="")


k=int(input())
n=int(input())
s=list(input().strip().split())
get_k_skips_n_grams(k, n, s)


'''
1
2
the rain in Spain falls mainly on the plain
'''