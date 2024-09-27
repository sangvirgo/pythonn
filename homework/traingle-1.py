import math

class  Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distance(self, p1):
        result=(self.x-p1.x)**2+(self.y-p1.y)**2
        return float(math.sqrt(result))

    def isValidTraingle(self, p1, p2):
        a=self.distance(p1)
        b=self.distance(p2)
        c=p1.distance(p2)
        EPSILON=1e-9
        return (a+b>c+EPSILON) and (a+c>b+EPSILON) and (b+c>a+EPSILON)



def main():
    t=int(input().strip())
    for _ in range(t):
        arr=[float(i.strip()) for i in input().strip().split()]
        x1, y1, x2, y2, x3, y3=arr
        p1=Point(x1, y1)
        p2=Point(x2, y2)
        p3=Point(x3, y3)
        if p1.isValidTraingle(p2, p3):
            a=p1.distance(p2)
            b=p1.distance(p3)
            c=p2.distance(p3)
            print(f"{(a+b+c):.3f}")
        else:
            print("INVALID")


if __name__ == "__main__":
    main()


"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
"""