import numpy as np


def func1():
    a=np.array([1, 2, 3])
    b=np.array((5, 7, 2))
    result=np.array([np.sum(a), np.sum(b)])
    print(result)

func1()