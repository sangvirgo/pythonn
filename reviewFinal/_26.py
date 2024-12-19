import math


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, p):
        return f"{math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2):.4f}"


def solve():
    t=int(input())
    for _ in range(t):
        x1, y1, x2, y2 = list(map(float, input().split()))
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        print(p1.distance(p2))

solve()
'''
2
0 0 0 5
0 199 5 6



5.0000
193.0648
'''