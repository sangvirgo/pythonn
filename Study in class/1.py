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

# X=set('spamm')
# Y={'h','a','m'}
# # print(X,Y)
# print(X)
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

# fruits = ("apple", "banana", "cherry", "orange")
# (*variable_1, variable_2, variable_3) = fruits
# print(variable_1[-1::-1], variable_2, variable_3)

# y=3
# x=y//2

# while x>1:
#     if y%x==0:
#         print(x)
#         break
#     x-=1
# else:
#     print(y)


# s="spam"
# for i in s:
#     print(i, end=" ")


# T=((1,2),(3,4), (5,6))
# for(_, a) in T:
#     print(a, end=" ")



# D={'a':1, 'b':2, 'c':3}
# for key in D:
#     print(key,"=>", D[key])


# for (a, b, *c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
#     print(a, b, c[-1])


# list_a = [11, 22, 13, 14, 15, 16, 27, 18, 19, 20]

# sum = 0

# for i in range(1, len(list_a), 3):
#     sum += list_a[i]

# print(sum)


# l=[1, 2, 3, 4, 5]

# for i in range(len(l)):
#     l[i]=l[i]+1

# print(l)

# a=[1, 2, 3, 4, 5]

# for x in a:
#     x=x+1

# print(a)


# L = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

# for i in range(len(L)):
#     L[i][1] = L[i][0] + 1
# print(L)


# L = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

# for x in L:
#     x[1] = x[0] + 1

# L


# L = [(0, 100), (1, 101), (2, 102), (3, 103), (4, 104)]
# for item in L:
#     item += (1,)
# print(L)


# L = [(0, 100), (1, 101), (2, 102), (3, 103), (4, 104)]
# for i in range(len(L)):
#     L[i] += (1,)
# print(L)



# l1=[1, 2, 3, 4, 5]
# l2=[6, 7, 8, 9, 10]
# l3=[11, 12, 13, 14]

# temp=list(zip(l1, l2, l3))

# print(temp)



# s="spam"
# for (offset, item) in enumerate(s):
#     print(item, 'appears at offset', offset)


# l=[1, 2, 3, 4, 5]
# l=[x+10 for x in l]
# print(l)


# l=[]
# for x in 'abc':
#     for y in 'def':
#         l.append(x+y)

# print(l)

# h=[x+y for x in 'abc' for y in 'def']
# print(h)


# my_list='abc, 123, cba, 456, 321'.split(', ')
# result=[(j, j[::-1]) for j in my_list if j[::-1]]
# print(result)


# seq=[1, 2, 3, 4, 5]
# a, b, c, *d=seq
# print(a, b, c, d)



# a = b = []
# b.append(42)
# print(a, b)


# l=[1, 2, 3, 4, 5]
# m=l
# l=l+[6]
# print(l, m)

# l2=[1, 2, 3, 4, 5]
# m2=l2
# l2+=[6]
# print(l2, m2)


# Các cấu trúc này bao gồm list, dict, set, bytearray, và các đối tượng tùy chỉnh (custom objects) với thuộc tính có thể thay đổi được.
# Trong Python, có sự khác biệt giữa các phép toán + và += khi làm việc với danh sách (list). Hãy xem xét hai đoạn mã mà bạn đã đưa ra:

# Đoạn mã đầu tiên:
# python
# Copy code
# l = [1, 2, 3, 4, 5]
# m = l
# l = l + [6]
# print(l, m)
# Giải thích:

# l và m đều tham chiếu đến cùng một danh sách ban đầu [1, 2, 3, 4, 5].
# Phép l = l + [6] tạo ra một danh sách mới bằng cách nối danh sách l ban đầu với danh sách [6], sau đó gán lại danh sách mới này cho biến l.
# Bởi vì phép + tạo ra một danh sách mới và gán nó cho l, biến m vẫn tham chiếu đến danh sách ban đầu [1, 2, 3, 4, 5].
# Kết quả là:

# makefile
# Copy code
# l: [1, 2, 3, 4, 5, 6]
# m: [1, 2, 3, 4, 5]
# Đoạn mã thứ hai:
# python
# Copy code
# l2 = [1, 2, 3, 4, 5]
# m2 = l2
# l2 += [6]
# print(l2, m2)
# Giải thích:

# l2 và m2 đều tham chiếu đến cùng một danh sách ban đầu [1, 2, 3, 4, 5].
# Phép l2 += [6] (hay l2.extend([6])) không tạo ra danh sách mới mà thực hiện phép cộng trực tiếp trên danh sách mà l2 và m2 cùng tham chiếu đến. Kết quả là danh sách [1, 2, 3, 4, 5] được thay đổi thành [1, 2, 3, 4, 5, 6].
# Vì m2 và l2 cùng tham chiếu đến danh sách đó, cả hai sẽ thay đổi.
# Kết quả là:

# makefile
# Copy code
# l2: [1, 2, 3, 4, 5, 6]
# m2: [1, 2, 3, 4, 5, 6]
# Tóm lại:
# Phép + tạo ra một danh sách mới và không thay đổi danh sách ban đầu.
# Phép += (hay extend) thay đổi trực tiếp danh sách ban đầu, do đó tất cả các biến tham chiếu đến danh sách đó sẽ thấy sự thay đổi.



# a=3
# if a==1:
#     print("a")
# elif a==2:
#     print("b")
# else:
#     print("c")


# branch = {'spam': 1.25,
#         'ham': 1.99,
#         'eggs': 0.99}

# print(branch.get('spam', 'Bad choice'))



# print(['f', 't'][bool('')])


# Truth Values and Boolean Tests
# print(2 or 3)
# print(3 or 2)
# nếu không null thì trả về giá trị đầu còn khi null trả value thứ 2

# print(2 and 3)
# print(3 and 2)
# if not null then return value 2 else return value 1





# a=3
# b=2 if a>1 else 1
# print(b)


# while Loops
# x=10
# while x>1:
#     print(x)
#     x/=2
# else:
#     print("Done")


# x="spam"
# while x:
#     print(x)
#     x=x[1:]


# T = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# for (_, a, _) in T:
#     print(a)



# D = {'a': 1, 'b': 2, 'c': 3}
# for key in D:
#     print(key, '=>', D[key])

# for (key, value) in D.items():
#     print(key, '=>', value)


# list = [11, 22, 13, 14, 15, 16, 17, 18, 19, 20]

# for i in range(1, len(list), 3):
#     print(list[i])



# L = [1, 2, 3, 4, 5]
# for i in range(len(L)):
#     L[i] = L[i] + 1
# print(L)


# M = [1, 2, 3, 4, 5]
# for x in M:
#     x += 1
# print(M)



# L1 = [1,3,5,7] # 4
# L2 = [2,4,6,8] # 4

# temp=list(zip(L1, L2))
# print(temp)


# for (x, y) in zip(L1, L2):
#     print(x, y, "=>", x+y)


# dictionary with zip
# keys=['name', 'job', 'zip']
# values=[1, 2, 3]
# d=dict(zip(keys, values))
# print(d)


# s="spam"
# for (index, item) in enumerate(s):
#     print(item, 'at', index)


# for x in [1, 2, 3, 4]:
#     print(x**2, end=' ')


# import sys
# print(sys.path)


# f=open('script2.py')
# for line in f.readlines():
#     print(line.upper(), end='')


# # vertion 1
# L = [1, 2, 3, 4, 5]
# for i in range(len(L)):
#     L[i]+=10
# print(L)


# m=[1, 2, 3, 4, 5]
# for i in m:
#     i+=10
# print(m)

# # version 2
# m=[x+10 for x in m]
# print(m)


# line=[line.rstrip() for line in open('script2.py')]
# print(line)




# # coding functions
# seq1=[1, 2, 3, 4, 5]
# seq2=[5, 7, 8, 9, 10]
#
#
# def intersect(seq1, seq2):
#     res=[]
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#     return res
#
# print(intersect(seq1, seq2))

# x = 300
# def myfunc():
#     global x
#     x += 200
#     def mysubfunc():
#         x = 100
#         return x
#     return mysubfunc
# if __name__ == "__main__":
#     x = 20
#     myfunc()()
#     print(x)


# def minmax(test, *args):
#     res = args[0]
#     count = 0
#     for arg in args[1:]:
#         if test(arg, res):
#             res = arg
#             count += 1
#     return res, count

# def lessthan(x, y):
#     return x < y

# if __name__ == '__main__':
#     print(minmax(lessthan, 4, 2, 1, 5, 6, 3))

# L="123456"

# def mysum1(L):
#     return 0 if not L else L[0] + mysum1(L[1:])
# print(mysum1(L))


# def mysum2(L):
#     return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])
# print(mysum2(L))

# def mysum3(L):
#     first, *rest = L  # [1, 2, 3, 4, 5]
#     return first if not rest else first + mysum3(rest)
# print(mysum3(L))



# f=lambda x, y, z: x+y+z
# print(f(2, 3, 4))
#
# def f1(x): return x**2
# def f2(x): return x**3
# def f3(x): return x**4
#
# L=[f1, f2, f3]
#
# for fz in L:
#     print(fz(2))
#

# print(L[0](3))



# def action(x):
#     return lambda y: x+y
#
# act=action(99)
# print(act(2))
#
#
# action2=lambda x: lambda y: x+y
#
# act1=action2(99)
# print(act1(2))

# from functools import reduce
# print(reduce((lambda x, y: x+y), [1, 2, 3, 4, 5]))


#
# x=[1, 2, 3, 4, 5]
# y=2
# temp_func=(i**y for i in x)
# print(list(temp_func))




# import numpy as np
#
# # 1. Sinh ngẫu nhiên các phần tử số nguyên cho mảng 3 chiều (4, 3, 2); giá trị các phần tử nằm trong đoạn [1, 10]
# array = np.random.randint(1, 11, size=(4, 3, 2))
# print("Mảng ngẫu nhiên 3 chiều (4, 3, 2):\n", array)
#
# # 2. Xuất ra vị trí của các phần tử thỏa điều kiện: >= 2
# condition = np.where(array >= 2)
# print("\nVị trí của các phần tử >= 2:\n", condition)
#
# # 3. Tính tổng các phần tử theo axis 0, 1, 2
# sum_axis0 = np.sum(array, axis=0)
# sum_axis1 = np.sum(array, axis=1)
# sum_axis2 = np.sum(array, axis=2)
#
# print("\nTổng các phần tử theo axis 0:\n", sum_axis0)
# print("\nTổng các phần tử theo axis 1:\n", sum_axis1)
# print("\nTổng các phần tử theo axis 2:\n", sum_axis2)




import numpy as np
from collections import Counter

# 1. Sinh ngẫu nhiên các phần tử số nguyên cho mảng 3 chiều (4, 3, 2); giá trị các phần tử nằm trong đoạn [1, 10]
array = np.random.randint(1, 11, size=(4, 3, 2))
print("Mảng ngẫu nhiên 3 chiều (4, 3, 2):\n", array)

# 2. Xuất ra vị trí của các phần tử thỏa điều kiện: >= 2
condition = np.where(array >= 2)
print("\nVị trí của các phần tử >= 2:\n", condition)

# 3. Tính tổng các phần tử theo axis 0, 1, 2
sum_axis0 = np.sum(array, axis=0)
sum_axis1 = np.sum(array, axis=1)
sum_axis2 = np.sum(array, axis=2)

print("\nTổng các phần tử theo axis 0:\n", sum_axis0)
print("\nTổng các phần tử theo axis 1:\n", sum_axis1)
print("\nTổng các phần tử theo axis 2:\n", sum_axis2)

# 4. Tính tổng các phần tử duy nhất trong mảng
unique_elements = np.unique(array)
sum_unique = np.sum(unique_elements)
print("\nTổng các phần tử duy nhất trong mảng:\n", sum_unique)

# 5. Tìm phần tử xuất hiện nhiều nhất trong mảng sử dụng np.unique và return_counts
flat_array = array.flatten()
unique_values, occurrence_count = np.unique(flat_array, return_counts=True)
max_count_index = np.argmax(occurrence_count)  # Tìm chỉ số của phần tử xuất hiện nhiều nhất
most_frequent_value = unique_values[max_count_index]
most_frequent_count = occurrence_count[max_count_index]

print("\nPhần tử xuất hiện nhiều nhất:", most_frequent_value, "với số lần xuất hiện:", most_frequent_count)

# 6. Tìm 3 phần tử có giá trị lớn nhất trong mảng
top_3_elements = np.sort(flat_array)[-3:]  # Sắp xếp và lấy 3 phần tử cuối (lớn nhất)
print("\n3 phần tử có giá trị lớn nhất trong mảng:\n", top_3_elements)