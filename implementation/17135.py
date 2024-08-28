import sys
import copy
from itertools import combinations

def playDefense(enemyMap, comb):
    killedEnemiesNum = 0

    while isExistEnemyInMap(enemyMap):
        attackedEnemies = findClosestEnemy(enemyMap, comb)
        killedEnemiesNum += deleteAttackedEnemies(enemyMap, attackedEnemies)
        moveEnemies(enemyMap)
    return killedEnemiesNum


def getArcherBatchList(comb):
    batchList = [0] * cols
    for i in comb:
        batchList[i] = 2
    return batchList


def isExistEnemyInMap(enemyMap):
    for row in enemyMap:
        if 1 in row:
            return True
    return False

def getDistance(archer, enemy):
    return abs(archer[0] - enemy[0]) + abs(archer[1] - enemy[1])


def findClosestEnemy(enemyMap, comb):
    attackedEnemies = []
    for i in comb:
        minDistance = attackRange + 1
        coordinate = ()
        totalRange = rows - 1 - attackRange if rows > attackRange else -1
        for r in range(rows - 1, totalRange, -1):
            for c in range(cols):
                if enemyMap[r][c] == 1:
                    distance = getDistance((rows, i), (r, c))
                    if minDistance > distance:
                        minDistance = distance
                        coordinate = (r, c)
                    elif minDistance == distance and coordinate:
                        if coordinate[1] > c:
                            coordinate = (r, c)
        if coordinate:
            attackedEnemies.append(coordinate)
    return attackedEnemies


def deleteAttackedEnemies(enemyMap, attackedEnemies):
    killedEnemiesNum = 0
    for r, c in attackedEnemies:
        if enemyMap[r][c] == 1:
            enemyMap[r][c] = 0
            killedEnemiesNum += 1
    return killedEnemiesNum


def moveEnemies(enemyMap):
    for r in range(rows - 1, 0, -1):
        for c in range(cols):
            enemyMap[r][c] = enemyMap[r - 1][c]
    for c in range(cols):
        enemyMap[0][c] = 0


rows, cols, attackRange = map(int, sys.stdin.readline().split())
enemyMap = [list(map(int, sys.stdin.readline().split())) for i in range(rows)]

combs = list(combinations(range(cols), 3))
result = 0

for comb in combs:
    curEnemyMap = copy.deepcopy(enemyMap)
    killedEnemiesNum = playDefense(curEnemyMap, comb)
    result = max(killedEnemiesNum, result)

print(result)