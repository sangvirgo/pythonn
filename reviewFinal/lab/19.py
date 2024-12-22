s=list(input().replace("'", "").strip('[]').split(", "))

result=list(filter(lambda x: (x==x[::-1]), s))

print(result)


'''
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
'''