import sys
from collections import deque


def divideListByZero():
    negativeLocations = deque()
    positiveLocations = []

    for idx, loc in enumerate(locationOfBooks):
        if loc > 0:
            positiveLocations = deque(locationOfBooks[idx:])
            break
        negativeLocations.appendleft(-loc)

    return negativeLocations, positiveLocations


def findMinimumWalks(locations, weightCapacity):
    length = len(locations)
    index = length % weightCapacity
    result = 2 * locations[index - 1] if index != 0 else 0

    while index < length:
        result += 2 * locations[index + weightCapacity - 1]
        index += weightCapacity

    return result


def findLastPosition(negativeLocations, positiveLocations):
    if not negativeLocations:
        return positiveLocations[-1]
    if not positiveLocations:
        return negativeLocations[-1]
    if negativeLocations[-1] > positiveLocations[-1]:
        return negativeLocations[-1]
    return positiveLocations[-1]


numOfBooks, weightCapacity = map(int, sys.stdin.readline().split())
locationOfBooks = list(map(int, sys.stdin.readline().split()))

locationOfBooks.sort()
negativeLocations, positiveLocations = divideListByZero()

leftWalks = findMinimumWalks(negativeLocations, weightCapacity)
rightWalks = findMinimumWalks(positiveLocations, weightCapacity)

result = leftWalks + rightWalks
result -= findLastPosition(negativeLocations, positiveLocations)
print(result)
