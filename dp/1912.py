import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

max_sum = numbers[0]
current_sum = numbers[0]

for num in numbers[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)