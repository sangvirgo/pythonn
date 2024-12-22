dic1=eval(input().strip())
dic2=eval(input().strip())

dic_result=dic1

for k, v in dic2.items():
    if not k in dic_result:
        dic_result[k]=v
    else:
        temp=list()
        temp.append(dic_result[k])
        temp.append(v)
        dic_result[k]=temp

print(dic_result, end="")


'''
{1: "abc", 3: "def", 5: "ghi"}
{2: "ABC", 4: "DEF", 6: "GHI"} 


{1: "abc", 3: "def", 5: "ghi"}
{5: "ABC", 4: "DEF", 6: "GHI"} 
'''