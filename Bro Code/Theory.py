"""

name="Bro"
print(name)
print("hihih")
print(type(name))


age=21
print(type(age))
# print("Your age is: " + age)
print("Your age is: " + str(age))


height=2005.5
# print("Your heigh is: "+ str(height))
print(type(height))


sang=han=su=ri=0


name="sang sang sang"
thefirstname=''
# print(len(name))
# print(len(thefirstname))

# print(name.find('g'))

# capitalize the first char 
# print(name.capitalize())

# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())

# # Chuỗi chứa toàn bộ là chữ cái
# print("Hello".isalpha())  # True

# # Chuỗi có chứa số
# print("Hello123".isalpha())  # False

# # Chuỗi có chứa khoảng trắng
# print("Hello World".isalpha())  # False

# # Chuỗi rỗng
# print("".isalpha())  # False


# print(name.count("s"))
# print(name.replace('s', 'S'))
# print(name*3)


a=3; b=4.4; c="5"
print(a)
print(int(b))
print(int(c))


name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello " + name + "!"+" Your age is: " + str(age))


import math

pi=3.14

print(math.ceil(pi))
print(math.floor(pi))
print(round(pi))
print(math.sqrt(16))
print(pow(2,3))



# string slicing
# slicing : [start:end:step]

website1="http://www.google.com"
website2="http://www.facebook.com"

slice1=website1[11: 17: 1]
slice2=website2[: : -1]
print(slice1)
# reverse the string
print(slice2)

slice3=slice(11, -4)
print(website1[slice3])



# if statement
# use (and, or, not) 
a=3
if a>3 and a<3: 
    print("a is not 3")
elif a==3:
    print("a is 3")


b=5
if b>3 or b<3:
    print("b is not 3")

else :
    print("b is 3")


# while statement
name=None

while not name: 
    name=input("Enter your name: ")

print("Hello " + name + "!")



# for statement

# from 50 to 99 have step = 2

import time
for i in range(50, 100, 2):
    print(i)

for second in range(10, 0, -1): 
    print(second)
    time.sleep(1)
print("Happy new year") 


# loop control statement
# break: exit the loop
# continue: skip the current iteration
# pass: do nothing

for i in range(10): 
    if i==3:
        pass
    print(i)

for i in range(10): 
    if i==3:
        continue
    print(i)

"""


# array
food=["rice", "noodle", "bread", "meat", "vegetable"]

# add in the end of array
# food.append("fish")

# delete the specific element
# food.remove("noodle")

# delete the last element
# food.pop()

# insert the element at the specific position
# food.insert(3, "pizza")

# food.sort()

# food.reverse()

food.clear()

for i in food:
    print(i)


