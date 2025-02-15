import sys

def max_natural_numbers(target):
    N = 0
    total = 0

    while total <= target:
        N += 1
        total += N

    return N - 1


target = int(sys.stdin.readline())
print(max_natural_numbers(target))
