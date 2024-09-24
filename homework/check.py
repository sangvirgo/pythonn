n=int(input().strip())

arr = [float(item.strip()) for item in input().strip().split()]

minValue=min(arr)
maxValue=max(arr)

# Filter elements and convert to list
filtered_list = list(filter(lambda x: x!=minValue and x!=maxValue, arr))

# Calculate average using list methods
avg = sum(filtered_list) / len(filtered_list)

print(round(avg, 2))