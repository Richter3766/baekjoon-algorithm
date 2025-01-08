import sys

def dfs(numbers, start):
    stack = [start]
    visited = [False] * length

    while True:
        cur = stack[-1]
        if visited[numbers[cur]] == True:
            break
        visited[numbers[cur]] = True
        stack.append(numbers[cur])

    if all(visited[i] == True for i in stack):
        return [i + 1 for i in range(length) if visited[i] == True]
    else: return []

length = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) - 1 for i in range(length)]
maxLength = 0
resultSet = []
for i in range(length):
    if (i + 1) not in resultSet:
        tempList = dfs(numbers, i)
        resultSet.extend(tempList)

print(len(resultSet))
for i in sorted(resultSet):
    print(i)

# 각 번호에서 dfs 탐색
# 탐색 불가 할 때까지 탐색 후 나온 둘째 줄 수와 첫째 줄 수가 같은 경우에만 인정

