# import math

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
# Definition:
# - ordered collections of arbitrarily typed objects
# - no fixed size
# - mutable: changed in place, grow, and shrink

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

# import copy
# y=[1,2,3]
# x1=copy.copy(y)
# x2=copy.deepcopy(y)
# print(x1)
# print(x2) => same

# y=[[4, [11, 56],5], [6,7]]
# x1=copy.copy(y)
# x2=copy.deepcopy(y)
# y[0]=1  
# x3=y[:]
# # y[3][1][0]=100
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


# T = ('spam', 3.0, [11, 22, 33])
# print(T[1])

# print(T[2])

# print(T[2][1])

# T[2][1] = 15
# print(T)


# thisdict={  "brand": "Ford",
#             "model": "Mustang",
#             "year": 1964,
#             "temp": [1,[2, 4],3]
# }

# del thisdict['brand']
# print(thisdict)


# 


# Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ một nhóm các phần tử. 
# Các phần tử trong một tuple có thể thuộc các kiểu dữ liệu khác nhau (int, 
# float, string, v.v.). Tuple rất giống với danh sách (list), nhưng có một điểm 
# khác biệt quan trọng là tuple không thể thay đổi (immutable) sau khi đã được 
# tạo ra, tức là bạn không thể thay đổi giá trị của các phần tử trong tuple.

# T=(1,2,3)
# print(T)

# print(type(T))

# set
# set(): not duplicate, not sorted,
# mutable: add, remove, update

X=set('spamm')
Y={'h','a','m'}
# print(X,Y)

# print(X&Y)

# print(X|Y)

# print(X-Y)

# print(X>Y)
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# # thisset.update(tropical)
# # print(thisset)

# thisset.discard("banana")
# print(thisset)



# file
# open file
# ○ "r" - read, opens a file for reading, error
# if the file does not exist
# ○ "a" - append - opens a file for
# appending, creates the file if it does not
# exist
# ○ "w" - write - opens a file for writing,
# creates the file if it does not exist
# ○ "x" - create - creates the specified file,
# returns an error if the file exists

# ● read/write file
# ● close file


# f=open('data.txt', 'w', encoding='utf-8')
# f.write('Hello\n')

# f.write("Sơn ngu vãi lon")

# f.close()


# f=open('data.txt', 'r', encoding='utf-8')

# print(f.read())


# tmp_dict={
#     0: "ford",
#     1: False,
#     3: 19654,
#     2: ["red", "white", "blue"],
#     4: (1, 2, 3, 4)
# }

# tmp_dict[0]+=" Edition 1"
# tmp_dict[2]=tmp_dict[2][1::-1]+["yellow"]
# tmp_dict[4]=tmp_dict[4]+(12)
# print(tmp_dict)



# a, b, c, d, e, f = 'sonngu'
# print(a, b, c, d, e, f)

fruits = ("apple", "banana", "cherry", "orange")
(*variable_1, variable_2, variable_3) = fruits
print(variable_1[-1::-1], variable_2, variable_3)