arr=list(input().strip().split(", "))

arr_sort=list(i for i in arr)
arr_sort.sort()

print(arr==arr_sort, end='')