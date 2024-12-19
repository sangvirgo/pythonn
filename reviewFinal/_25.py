class Student:
    def __init__(self, last_name, first_name, c, t):
        self.last_name=last_name
        self.first_name=first_name
        self.c=c
        self.t=t

def solve():
    n=int(input())
    students=[]
    for _ in range(n):
        name=list(input().split())
        last_name=name[0:len(name)-1]
        first_name=name[-1:-2: -1]
        c, t=list(map(int, input().split()))
        students.append(Student(last_name, first_name, c, t))
    students.sort(key=lambda student: (-student.c, student.t, student.first_name, student.last_name))
    for st in students:
        print(*st.last_name, *st.first_name, st.c, st.t)

solve()
'''
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
'''