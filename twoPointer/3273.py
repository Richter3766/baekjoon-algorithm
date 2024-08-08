import sys

sizeN = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

numbers.sort()

left = 0
right = sizeN - 1

result = 0
while left < right:
    if numbers[left] + numbers[right] == target:
        result += 1
        left += 1
    elif numbers[left] + numbers[right] < target:
        left += 1
    else:
        right -= 1
print(result)