import sys
from collections import deque

# 1. 결과 큐에서 dequeue 실행
# 2. 그 결과 값이 fromSentences의 리스트 0번째 리스트에 있는 지 확인
# 3-1. 있으면 그 리스트에서 pop
# 3-2. 없으면 impossible
# 4. 1~3 반복 (3-2가 아닌 경우 or fromSenetence가 빌 때까지)
# 예외 케이스: toSentence는 비었는데,fromSentence에서 남은 값들이 있는 경우
# toSentence 가 비지 않았는데, fromSentence가 비어있는 경우

def checkIfExist(target):
    isExist = False
    for idx, sentence in enumerate(fromSentences):
        if sentence and target == sentence[0]:
            fromSentences[idx].popleft()
            isExist = True
            break
    return isExist

numOfParrots = int(sys.stdin.readline())
fromSentences = [deque(sys.stdin.readline().strip().split(" ")) for i in range(numOfParrots)]
toSentence = deque(sys.stdin.readline().strip().split())
isExist = False

while toSentence:
    target = toSentence.popleft()
    isExist = checkIfExist(target)

    if not isExist:
        break

if not isExist or any(len(i) > 0 for i in fromSentences):
    print("Impossible")
else:
    print("Possible")