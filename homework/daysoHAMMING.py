"""
11
1
2
6
7
8
9
10
11
12
13
14
"""

import heapq


def find_hamming_numbers(limit):
    hamming_numbers = []
    heap = [1]
    seen = set([1])
    while heap:
        hamming = heapq.heappop(heap)
        hamming_numbers.append(hamming)
        if hamming > limit:
            break
        for multiplier in [2, 3, 5]:
            next_hamming = hamming * multiplier
            if next_hamming <= limit and next_hamming not in seen:
                heapq.heappush(heap, next_hamming)
                seen.add(next_hamming)
    return hamming_numbers


def solve():
    t = int(input().strip())
    arr = [int(input().strip()) for _ in range(t)]

    maxValue = max(arr)

    hamming_numbers = find_hamming_numbers(maxValue)

    hamming_order = {num: idx + 1 for idx, num in enumerate(hamming_numbers)}

    for n in arr:
        if n in hamming_order:
            print(hamming_order[n])
        else:
            print("Not in sequence")


solve()
