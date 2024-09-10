"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
Output:

Đưa ra kết quả mỗi test theo từng dòng.
Ví dụ:

Input:

Output:

2
12ab29cd19

ab123gh456cd

12
123
"""


t=int(input())

for _ in range(t):
    s=input()
    res = float('inf')
    temp=''
    
    for char in s:
        if char.isdigit():
            temp+=char
        else:
            if temp!='':
                res=min(res,int(temp))
                temp=''
    print(res)    
    
