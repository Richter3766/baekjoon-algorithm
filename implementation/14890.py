import sys


def checkRowPossible(index):
    row = slopeMap[index]
    lamp = []
    for i in range(sizeN - 1):
        gap = row[i] - row[i + 1]
        possible = True
        if abs(gap) > 1:
            return 0
        elif gap == 1:
            lamp, possible = tryPutLampInRow(row, lamp, i + 1)
        elif gap == -1:
            lamp, possible = tryPutLampInRow(row, lamp, i - limit + 1)

        if not possible:
            return 0

    return 1


def tryPutLampInRow(row, lamp, index):
    possible = True
    compareValue = row[index]

    for i in range(limit):
        if index + i < 0 or \
                index + i in lamp or \
                index + i >= sizeN or \
                not compareValue == row[index + i]:
            possible = False
            break
        lamp.append(index + i)

    return lamp, possible


def checkColumnPossible(index):
    lamp = []
    for i in range(sizeN - 1):
        gap = slopeMap[i][index] - slopeMap[i + 1][index]
        possible = True
        if abs(gap) > 1:
            return 0
        elif gap == 1:
            lamp, possible = tryPutLampInColumn(i + 1, lamp, index)
        elif gap == -1:
            lamp, possible = tryPutLampInColumn(i - limit + 1, lamp, index)

        if not possible:
            return 0

    return 1


def tryPutLampInColumn(row, lamp, index):
    possible = True
    compareValue = slopeMap[row][index]

    for i in range(limit):
        if row + i < 0 or \
                row + i in lamp or \
                row + i >= sizeN or \
                not compareValue == slopeMap[row + i][index]:
            possible = False
            break
        lamp.append(row + i)

    return lamp, possible


sizeN, limit = map(int, sys.stdin.readline().split())
slopeMap = [list(map(int, sys.stdin.readline().split())) for i in range(sizeN)]

result = 0

for index in range(sizeN):
    result += checkRowPossible(index)
    result += checkColumnPossible(index)

print(result)