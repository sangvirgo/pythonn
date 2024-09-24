n=int(input().strip())

arr = [float(item.strip()) for item in input().strip().split()]

minValue=min(arr)
maxValue=max(arr)

summ=list(filter(lambda x: x!=minValue and x!=maxValue, arr))

avg=sum(summ)/len(summ)

print(round(avg, 2))

"""
6
6.75 8 9.2 7.25 7.75 6.75
"""