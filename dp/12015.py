import sys
import bisect

def solution_bisect(num_sequence):
    num_list = []

    for num in num_sequence:
        postition = bisect.bisect_left(num_list, num)

        if postition == len(num_list):
            num_list.append(num)
        else:
            num_list[postition] = num

    return len(num_list)

size = int(sys.stdin.readline())
num_sequence = list(map(int, sys.stdin.readline().split()))

result = solution_bisect(num_sequence)
print(result)