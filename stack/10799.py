import sys

ironSticks = list(sys.stdin.readline().strip())

# ( 나오면 스택에 푸쉬
# ) 나오면 스택에서 팝
# 팝 했을 때 스택의 길이 len 만큼 막대 수 추가
# 단 ) 연속이면 1만 추가
sticks = []
result = 0
prev = '('
for item in ironSticks:
    if item == '(':
        sticks.append(item)
    elif item == ')' and prev == ')':
        sticks.pop()
        result += 1
    else:
        sticks.pop()
        result += len(sticks)
    prev = item
print(result)