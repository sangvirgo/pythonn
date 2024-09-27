import math

class  Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distance(self, Point):
        result=(self.x-Point.x)**2+(self.y-Point.y)**2
        print(f"{math.sqrt(result): .4f}")


def main():
    t=int(input().strip())
    for _ in range(t):
        arr=[float(i.strip()) for i in input().strip().split()]
        x1, y1, x2, y2=arr
        p1=Point(x1, y1)
        p2=Point(x2, y2)
        p1.distance(p2)


if __name__ == "__main__":
    main()


"""
2
0 0 0 5
0 199 5 6
"""