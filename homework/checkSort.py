n=list(input().strip().replace(",","").split(" "))

def checkSort(n):
    preN=n[0]
    for i in range(1, len(n)):
        if preN>n[i]:
            return False
        preN=n[i]
    if preN>n[len(n)-1]:
        return False
    return True

if checkSort(n):
    print("True", end="")
else:
    print("False", end="")