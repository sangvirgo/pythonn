def sum_of_num(x):
  s=0
  while x>0:
    s+=x%10
    x//=10
  return s

def solve():
  t=int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=lambda x: (sum_of_num(x), x))
    print(*arr)

solve()
'''
1
8
143 43 22 99 7 9 1111 10000000

'''