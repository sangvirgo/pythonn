def solve():
    num = input()
    pow_value = len(num)
    multi_value = pow(10, pow_value - 1)
    if len(num) < 2:
        print(num)
        return

    remember = False
    for i in range(len(num) - 1, 0, -1):
        digit = int(num[i])
        if remember: digit += 1

        if digit >= 5: remember = True
        else: remember = False

    digit = int(num[1])
    if remember: digit += 1
    if digit >= 5:
        res = (int(num[0]) + 1) * multi_value
        print(res)
    else:
        res = int(num[0]) * multi_value
        print(res)

def main():
    T = int(input())

    for _ in range(T):
        solve()

main()