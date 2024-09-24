str=input().strip()

str_list=[s.strip("'") for s in str.strip("[]").split(", ")]
"""
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
"""


result=list(filter(lambda x: x==x[::-1], str_list))
print(result)

