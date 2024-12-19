class Matrix:
    def __init__(self, n, m, a):
        self.n=n
        self.m=m
        self.a=a
    def calc(self):
        b=[]
        for i in range(self.m):
            b.append([])
            for j in range(self.n):
                b[i].append(self.a[j][i])

        result=[[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                temp=0
                for k in range(self.m):
                    temp+=self.a[i][k]*b[k][j]
                result[i][j]=temp

        for row in result:
            print(*row)

def solve():
    t=int(input())
    for _ in range(t):
        n, m=list(map(int, input().split()))
        a=[]
        for i in range(n):
            a.append(list(map(int, input().split())))
        ma=Matrix(n, m, a)
        ma.calc()

solve()
'''
1
2 2
1 2
3 4
'''