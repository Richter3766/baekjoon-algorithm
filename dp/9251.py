import sys

def solution(first_string, second_string):
    first_length = len(first_string) + 1
    second_length = len(second_string) + 1
    dp_table = [[0 for i in range(first_length)] for i in range(second_length)]

    for r in range(1, second_length):
        for c in range(1, first_length):
            if second_string[r - 1] == first_string[c - 1]:
                dp_table[r][c] = dp_table[r - 1][c - 1] + 1
            else: dp_table[r][c] = max(dp_table[r - 1][c], dp_table[r][c - 1])

    return dp_table[-1][-1]


first_string = list(map(str, sys.stdin.readline().strip()))
second_string = list(map(str, sys.stdin.readline().strip()))

result = solution(first_string, second_string)
print(result)