import sys

def buildDirections():
    return [(-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1)]

def buildMap():
    newMap = [[[] for i in range(mapSize)] for i in range(mapSize)]

    for fireball in fireballs:
        fireball[row] -= 1
        fireball[col] -= 1
        if fireball[mass] != 0:
            newMap[fireball[row]][fireball[col]].append(fireball)

    return newMap


def moveFireballs(worldMap):
    newMap = [[[] for i in range(mapSize)] for i in range(mapSize)]
    for r in range(mapSize):
        for c in range(mapSize):
            if worldMap[r][c]:
                for i in range(len(worldMap[r][c])):
                    fireball = worldMap[r][c].pop()
                    drow, dcol = directions[fireball[direction]]
                    drow *= fireball[speed]
                    dcol *= fireball[speed]
                    fireball[row] = (fireball[row] + drow) % (mapSize)
                    fireball[col] = (fireball[col] + dcol) % (mapSize)
                    newMap[fireball[row]][fireball[col]].append(fireball)
    return newMap


def combineAndDivideFireballs(worldMap):
    for r in range(mapSize):
        for c in range(mapSize):
            if len(worldMap[r][c]) >= 2:
                totalNum, totalMass, totalSpeed, tempDirections = len(worldMap[r][c]), 0, 0, []
                for fireball in worldMap[r][c]:
                    totalMass += fireball[mass]
                    totalSpeed += fireball[speed]
                    tempDirections.append(fireball[direction])
                newDirection = decideDirction(tempDirections)
                worldMap[r][c].clear()
                newMass, newSpeed = totalMass // 5, totalSpeed // totalNum
                if newMass != 0:
                    for i in range(4):
                        worldMap[r][c].append([r, c, newMass, newSpeed, newDirection])
                        newDirection += 2
    return worldMap


def decideDirction(tempDirections):
    isAllOddOrEven = True
    prev = tempDirections[0] % 2
    for d in tempDirections[1:]:
        if d % 2 != prev:
            isAllOddOrEven = False
            break
    if isAllOddOrEven:
        return 0
    else:
        return 1


def getTotalMassOfFireballs(worldMap):
    totalMass = 0
    for r in range(mapSize):
        for c in range(mapSize):
            if worldMap[r][c]:
                for fireball in worldMap[r][c]:
                    totalMass += fireball[mass]

    return totalMass


mapSize, numOfFireBalls, numOfOrders = map(int, sys.stdin.readline().split())
fireballs = [list(map(int, sys.stdin.readline().split())) for i in range(numOfFireBalls)]

row, col, mass, speed, direction = range(5)
directions = buildDirections()
worldMap = buildMap()
for o in range(numOfOrders):
    worldMap = moveFireballs(worldMap)
    worldMap = combineAndDivideFireballs(worldMap)

result = getTotalMassOfFireballs(worldMap)
print(result)