import math


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, p):
        return math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def calc_chu_vi(self):
        c1=self.p1.distance(self.p2)
        c2 = self.p1.distance(self.p3)
        c3=self.p2.distance(self.p3)

        if (c1 + c2 <= c3) or (c1 + c3 <= c2) or (c2 + c3 <= c1):
            print("INVALID")
        else:
            print(f"{(c1+c2+c3):.3f}")

def solve():
    t = int(input())
    a = []
    for _ in range(t):
        a += map(float, input().split())

    i = 0
    for _ in range(t):
        triangle = Triangle(
            Point(a[i], a[i + 1]),
            Point(a[i + 2], a[i + 3]),
            Point(a[i + 4], a[i + 5])
        )
        triangle.calc_chu_vi()
        i += 6

solve()
'''
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
'''