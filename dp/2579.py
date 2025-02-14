import sys

def solution():
    if num_stair == 0:
        return 0
    if num_stair == 1:
        return stair_point[0]
    if num_stair == 2:
        return stair_point[0] + stair_point[1]

    dp_table = [0] * (num_stair)
    dp_table[0] = stair_point[0]
    dp_table[1] = stair_point[0] + stair_point[1]
    dp_table[2] = max(stair_point[0] + stair_point[2], stair_point[1] + stair_point[2])

    for i in range(3, num_stair):
        dp_table[i] = max(dp_table[i - 2] + stair_point[i], dp_table[i - 3] + stair_point[i - 1] + stair_point[i])

    return dp_table[-1]


num_stair = int(sys.stdin.readline())
stair_point = [int(sys.stdin.readline()) for _ in range(num_stair)]

result = solution()
print(result)