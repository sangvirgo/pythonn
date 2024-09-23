d=eval(input())
"""
{'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
"""

def find_shortest_lists(d):
    min_len=min(len(v) for v in d.values())
    return [k for k, v in d.items() if len(v)==min_len]

result=find_shortest_lists(d)
print(result, end='')