import sys

def backtracking(num_range, sequence_length):
    if len(num_list) == sequence_length:
        print(*num_list)
        return

    for i in range(1, num_range + 1):
        if not num_list or num_list[-1] <= i:
            num_list.append(i)
            backtracking(num_range, sequence_length)
            num_list.pop()


num_range, sequence_length = map(int, sys.stdin.readline().split())
num_list = []
backtracking(num_range, sequence_length)
