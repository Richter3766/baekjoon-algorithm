import sys

# 디버깅을 위해 추가 배열을 활용했다.
# 만약 공간 및 시간복잡도를 더 중요하게 생각한다면 추가 배열 없이 바로 result 계산해도 무방하다

def bindingPositiveNumbers():
    global idx
    bindedNumbers = []
    while idx < sizeN:
        if numbers[idx] <= 0:
            break
        if idx < sizeN - 1 and numbers[idx] > 1 and numbers[idx + 1] > 1:
            bindedNumbers.append(numbers[idx] * numbers[idx + 1])
            idx += 2
        else:
            bindedNumbers.append(numbers[idx])
            idx += 1
    return bindedNumbers


def bindingNegativeNumbers(negativeNumbers):
    idx = 0
    size = len(negativeNumbers)
    bindedNumbers = []
    while idx < size:
        if idx < size - 1 and negativeNumbers[idx] <= 0 and negativeNumbers[idx + 1] <= 0:
            bindedNumbers.append(negativeNumbers[idx] * negativeNumbers[idx + 1])
            idx += 2
        else:
            bindedNumbers.append(negativeNumbers[idx])
            idx += 1
    return bindedNumbers

sizeN = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(sizeN)]

idx = 0
result = 0
numbers.sort(reverse=True)

bindedNumbers = bindingPositiveNumbers()

negativeNumbers = numbers[idx:]
negativeNumbers.sort()

bindedNumbers.extend(bindingNegativeNumbers(negativeNumbers))

print(sum(bindedNumbers))