import sys

def solveEquation(numbers):
    x, y, z = numbers[0:3]
    if x - y == 0 or ((y - z) % (x - y)) != 0 :
        return -1, -1

    return (y - z) // (x - y), y - ((y - z) // (x - y)) * x


def isValid(numOfNumbers, numbers, a, b):
    for i in range(numOfNumbers - 1):
        if numbers[i + 1] != numbers[i] * a + b:
            return False
    return True


numOfNumbers = int(sys.stdin.readline())
numbers = list(map(int , sys.stdin.readline().split()))

if numOfNumbers <= 1:
    print('A')
elif numOfNumbers == 2:
    if numbers[0] == numbers[1]:
        print(numbers[0])
    else: print('A')
else:
    a, b = solveEquation(numbers)
    if a == b == -1:
        if all(numbers[i] == numbers[i + 1] for i in range(numOfNumbers - 1)):
            print(numbers[-1])
        else: print('B')
    else:
        if isValid(numOfNumbers, numbers, a, b):
            print(numbers[-1] * a + b)
        else: print('B')
