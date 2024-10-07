if __name__=="__main__":
    n, m=input().strip().split()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    setA=set(a)
    setB=set(b)

    giao = sorted(setA&setB)
    aTruB = sorted(setA-setB)
    bTruA = sorted(setB-setA)

    # Chuyển đổi các phần tử thành chuỗi và in ra
    print(" ".join(map(str, giao)))
    print(" ".join(map(str, aTruB)))
    print(" ".join(map(str, bTruA)))

"""
5 6
1 2 3 4 5
3 4 5 6 7 8
"""