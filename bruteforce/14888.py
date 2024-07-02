import sys

# 아이디어는 dfs
def dfs(index, current_result):
    global max_result, min_result
    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    if operators[0] > 0:
        operators[0] -= 1
        dfs(index + 1, current_result + numbers[index])
        operators[0] += 1

    if operators[1] > 0:
        operators[1] -= 1
        dfs(index + 1, current_result - numbers[index])
        operators[1] += 1

    if operators[2] > 0:
        operators[2] -= 1
        dfs(index + 1, current_result * numbers[index])
        operators[2] += 1

    if operators[3] > 0:
        operators[3] -= 1
        if current_result < 0:
            dfs(index + 1, -(-current_result // numbers[index]))
        else:
            dfs(index + 1, current_result // numbers[index])
        operators[3] += 1

# input
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split())) # 차례로 덧셈, 뺄셈, 곱셈, 나눗셈

max_result = -sys.maxsize
min_result = sys.maxsize

dfs(1, numbers[0])

print(max_result)
print(min_result)
