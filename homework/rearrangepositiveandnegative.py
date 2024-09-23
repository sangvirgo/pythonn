from PIL.ImageOps import posterize

l=list(map(int, input().strip('[]').split(',')))
"""
[-1, 2, -3, 5, 7, 8, 9, -10]
"""
positive=list(filter(lambda x: x>0, l))
negative=list(filter(lambda x: x<0, l))

positive.sort()
negative.sort()
print(positive+negative)
