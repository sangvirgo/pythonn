n=list(input())
n=n[::-1]
result=[]
for i in range(len(n)):
    if i!=0 and i % 3==0:
        result.append(',')
        result.append(n[i])
    else:
        result.append(n[i])

result=result[::-1]
print(''.join(result))

'''
153920529
452163687
'''