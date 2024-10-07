import math

class  Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distance(self, p1):
        return math.sqrt((self.x-p1.x)**2+(self.y-p1.y)**2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def check(self):
        a=self.p1.distance(self.p2)
        b=self.p2.distance(self.p3)
        c=self.p1.distance(self.p3)
        if (a + b > c) and (a + c > b) and (b + c > a):
            print("{:.2f}".format(0.25*math.sqrt((a+b+c)*(a+b-c)*(-a+b+c)*(a-b+c))))
        else:
            print("INVALID")

def main():
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triangle = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
        triangle.check()
        i += 6





if __name__ == "__main__":
    main()


"""
3
0 0 0 5 0 199
0 0 0 5 5 0
1 1 1 1 1 1
"""