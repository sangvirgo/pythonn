
dic=eval(input().strip())

min_size = min(len(v) for k, v in dic.items())

result=[]
for k, v in dic.items():
    if len(v)==min_size:
        result.append(k)
print(result, end="")




'''
{'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
'''