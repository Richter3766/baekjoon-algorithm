import sys

def solution(num_app, target_memory, app_memory_list, cost_list):
    total_cost = sum(cost_list) + 1
    dp_table = [[0] * (total_cost) for _ in range(num_app + 1)]

    result = total_cost
    for i in range(num_app):
        memory, cost = app_memory_list[i], cost_list[i]
        for c in range(total_cost):
            if cost <= c:
                dp_table[i + 1][c] = max(dp_table[i][c], dp_table[i][c - cost] + memory)
                if dp_table[i + 1][c] >= target_memory and result > c: result = c
            else: dp_table[i + 1][c] = dp_table[i][c]

    return result

num_app, target_memory = map(int, sys.stdin.readline().split())
app_memory_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))

result = solution(num_app, target_memory, app_memory_list, cost_list)
print(result)
