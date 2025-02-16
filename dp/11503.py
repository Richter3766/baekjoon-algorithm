import sys
import bisect

def solution(num_sequence):
    dp_table = [1] * size

    for i in range(1, size):
        for j in range(i):
            if num_sequence[i] > num_sequence[j]:
                dp_table[i] = max(dp_table[i], dp_table[j] + 1)

    return max(dp_table)


size = int(sys.stdin.readline())
num_sequence = list(map(int, sys.stdin.readline().split()))

result = solution(num_sequence)
print(result)