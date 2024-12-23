import numpy as np
a=np.array([2, 3, 4])
print(a)

b=np.arange(15).reshape(3, 5)
print(b)

# c=np.empty(3)
# print(c)
#
#
# d=np.ones((3, 2))
# print(d)
#
# e=np.zeros((3, 2))
# print(e)
#
# f=np.random.default_rng().random(3, 2)
# print(f)


r= np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
h=np.unique(r)
print(h)