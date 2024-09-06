import sys
import math


def drawDragonCurves():
    for x, y, direction, generation in curvesInfo:
        points = [(x, y)]
        nextPoint = drawZeroGeneration(x, y, direction)
        points.append(nextPoint)
        for g in range(generation):
            pivot = points[-1]
            for point in reversed(points[:-1]):
                nextPoint = rotatePointAroundOrigin(point, 90, pivot)
                gridMap[nextPoint[1]][nextPoint[0]] = 1
                points.append(nextPoint)


def drawZeroGeneration(x, y, direction):
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    gridMap[y][x] = 1
    gridMap[ny][nx] = 1
    return (nx, ny)


def rotatePointAroundOrigin(point, angle, origin):
    relativeX = point[0] - origin[0]
    relativeY = point[1] - origin[1]

    angleRad = math.radians(angle)

    xNew = relativeX * math.cos(angleRad) - relativeY * math.sin(angleRad)
    yNew = relativeX * math.sin(angleRad) + relativeY * math.cos(angleRad)

    return (round(xNew + origin[0]), round(yNew + origin[1]))


def findRectPartOfCurves():
    result = 0
    for r in range(gridSize):
        for c in range(gridSize):
            if checkDrawed(r, c) and \
                    checkDrawed(r + 1, c) and \
                    checkDrawed(r, c + 1) and \
                    checkDrawed(r + 1, c + 1):
                result += 1
    return result


def checkDrawed(r, c):
    if 0 <= r < gridSize and 0 <= c < gridSize and gridMap[r][c] == 1:
        return True
    return False


numOfCurves = int(sys.stdin.readline())
curvesInfo = [list(map(int, sys.stdin.readline().split())) for i in range(numOfCurves)]
gridSize = 101
gridMap = [[0] * gridSize for i in range(gridSize)]
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

drawDragonCurves()
result = findRectPartOfCurves()

print(result)
