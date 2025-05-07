import sys

""" 문제
어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 표현
N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
"""

""" 풀이 과정
1. 배열을 정렬 - NLogN
2. 배열의 각 수를 목표값으로 설정함.
3. 해당 목표값이 만들어지는 지 배열에서 두 포인터로 체크
4. 가능하면 answer +1 이후 종료
5. 모든 값에 대해 2~4 반복
"""

""" 시간 복잡도 고민
서로 다른 수의 합은 N^2을 피하기 어려워 보임
이진 탐색을 위한 정렬에 NLog(N)
아마 최적화를 해도 N^2 수준일 것
"""
answer = 0
num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort() # 주어진 배열을 정렬

for i in range(num):
    target = num_list[i] # 배열의 각 수를 목표값으로 설정하기
    left, right = 0, len(num_list) - 1 # 두 포인터 초기값 설정
    while True:
        # 서로 다른 수의 합이어야 하므로 같아지는 부분은 스킵
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if left == right: break # 두 포인터가 만나면 종료

        if num_list[left] + num_list[right] > target: # target보다 크면 right -1
            right -= 1
        elif num_list[left] + num_list[right] < target: # target보다 작으면 left + 1
            left += 1
        else: # 같으면 정답 체크하고 종료
            answer += 1
            break

print(answer)