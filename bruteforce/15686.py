import sys
from itertools import combinations

def findChickenDistance(distances, row, col):
    for idx, house in enumerate(houses):
        y, x = house
        distances[idx] = min(distances[idx], abs(row - y) + abs(col - x))
    return distances

sizeN, chickens = map(int, sys.stdin.readline().split())

houses = []
chickenHouse = []

for y in range(sizeN):
    row = list(map(int, sys.stdin.readline().split()))
    for x, value in enumerate(row):
        if value == 1:
            houses.append((y, x))
        elif value == 2:
            chickenHouse.append((y, x))

chickenCombination = list(combinations(chickenHouse, chickens))
result = []

for combination in chickenCombination:
    distances = [10000000000] * len(houses)
    for row, col in combination:
        distances = findChickenDistance(distances, row, col)
    result.append(sum(distances))

print(min(result))