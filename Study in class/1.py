import math

# print(math.trunc(-3.14))

# x = 0b001
# print(x<<2)
# print(int(x))

# print(144**.5)

# a=3

# s="1,22\times333, 4444, \next,"
# print(s.rstrip().split(','))
# print(s.split().rstrip(','))



# list
# l=[123, 'spam', 1.23]
# print(len(l))
# print(l[:-1])

# l+=[4,5,6]
# print(l)
# l.append('Ni')
# print(l)
# l.pop(2)
# print(l)

# l.insert(2, 123)
# print(l)

# l.remove(123)
# print(l)

# l.extend([4,5,6])
# print(l)

# del l[0]
# print(l)

# sort 
# reverse


# M=[[1,2,3],[4,5,6],[7,8,9]]


# L1 = [1, 2, 3]
# # L2=L1
# # L1[0]=4
# # print(L2)

# L2=L1[:]
# L1[0]=4
# print(L2)

import copy
# y=[1,2,3]
# x1=copy.copy(y)
# x2=copy.deepcopy(y)
# print(x1)
# print(x2) => same

# y=[[4, [11, 56],5], [6,7]]
# x1=copy.copy(y)
# x2=copy.deepcopy(y)
# x3=y[:]
# # y[3][1][0]=100
# y[0]=1  
# print(x1)
# print(x2) # => different
# print(x3) # => same     


# Y = [[2, [3, 31], 4], [2, 3, [4, 41]], 3]

# X1 = copy.copy(Y)
# X2 = copy.deepcopy(Y)

# Y[2] = 5  # Thay đổi phần tử cấp cao nhất của Y

# print("X1", X1)
# print("X2", X2)

# Y[0][1][1] = 1  # Thay đổi phần tử bên trong một danh sách con của Y

# print("X1", X1)
# print("X2", X2) 



# variable_1 = ["apple", "banana", "cherry", "orange"]

# print(variable_1[:-1], end="; ")
# print(variable_1[::-2], end="; ")
# print(variable_1[-1:])



# dictionaries
# d={'food':'Spam', 'quantity':4, 'color':'pink'}
# print(d)

# rec={'name':{'first':'Bob', 'last':'Smith'}, 'job':['dev', 'mgr'], 'age':40.5}
# # print(rec['name'])
# print(rec['name'][-1])

# D={'a' : 1, 'b' : 2, 'c' : 3}
# print(D.get('e'))

# thisdict = { 
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "temp": [1,[],3]
# }


T = ('spam', 3.0, [11, 22, 33])
print(T[1])

print(T[2])

print(T[2][1])

T[2][1] = 15
print(T)