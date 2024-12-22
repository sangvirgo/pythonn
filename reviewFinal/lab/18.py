arr=list(map(int, input().strip('[]').split(', ')))

# duong=list(filter(lambda x:x>0, arr))
# am=list(filter(lambda x: x<0, arr))
#
# duong.sort()
# am.sort()

arr.sort(key=lambda x:(x<0, x))

print(arr)
