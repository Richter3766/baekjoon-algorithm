import sys
from collections import deque

N = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for i in range(N)]

stack = deque([0])
index = 0
number = 1
# 언제 푸시하는가?
# 현재 수열의 포인터가 가리키는 곳의 값보다 스택 top의 값이 작을 때

# 언제 팝 하는가?
# 현재 수열의 포인터가 가리키는 곳의 값과 스택 top의 값이 같을 때

# 예외 케이스?
# 현재 수열의 포인터가 가리키는 곳의 값보다 스택 top의 값이 클 경우
result = []
while True:
    if index == N:
        break

    if sequence[index] > stack[-1]:
        stack.append(number)
        number += 1
        result.append('+')
    elif sequence[index] == stack[-1]:
        stack.pop()
        result.append('-')
        index += 1
    else:
        print('NO')
        exit(0)

for i in result:
    print(i)