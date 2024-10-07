
def isNhuan(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    else:
        return False



if __name__=="__main__":
    s=list(map(int, input().strip().split("/")))

    if isNhuan(s[2]) and s[0]<=29 and s[1]==2:
        print("True", end="")
    elif s[1] in [1, 3, 5, 7, 8, 10, 12] and s[0]<=31:
        print("True", end="")
    elif s[1] in [4, 6, 9, 11] and s[0]<=30:
        print("True", end="")
    else:
        print("False", end="")




"""
10/10/2020

29/02/2019
"""