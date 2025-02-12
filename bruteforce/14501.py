import sys

def solution():
    dp_table = [0] * (day_num + 1)
    for i in range(day_num):
        for j in range(i + work_info[i][0], day_num + 1):
            if dp_table[j] < dp_table[i] + work_info[i][1]:
                dp_table[j] = dp_table[i] + work_info[i][1]
    return dp_table[-1]

day_num = int(sys.stdin.readline())
work_info = [list(map(int, sys.stdin.readline().split())) for _ in range(day_num)]

result = solution()
print(result)