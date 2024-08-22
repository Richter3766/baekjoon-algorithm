import sys


def movePosition(operation, diceX, diceY):
    if operation == 1:
        diceY += 1
    elif operation == 2:
        diceY -= 1
    elif operation == 3:
        diceX -= 1
    elif operation == 4:
        diceX += 1
    return diceX, diceY


def isValidPosition(diceX, diceY):
    if diceX < 0 or diceY < 0 or diceX >= height or diceY >= width:
        return False
    return True


def rollDice(operation):
    zero, one, two, three, four, five = dice
    if operation == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = three, one, zero, five, four, two
    elif operation == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = two, one, five, zero, four, three
    elif operation == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = four, zero, two, three, five, one
    elif operation == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = one, five, two, three, zero, four


def reconcileDiceAndFloor(x, y):
    if mapOfNumbers[x][y] == 0:
        mapOfNumbers[x][y] = dice[5]
    else:
        dice[5] = mapOfNumbers[x][y]
        mapOfNumbers[x][y] = 0


height, width, diceX, diceY, numOfOperations = map(int, sys.stdin.readline().split())
mapOfNumbers = [list(map(int, sys.stdin.readline().split())) for i in range(height)]
operations = list(map(int, sys.stdin.readline().split()))

dice = [0] * 6
for operation in operations:
    prevX, prevY = diceX, diceY

    diceX, diceY = movePosition(operation, diceX, diceY)
    if not isValidPosition(diceX, diceY):
        diceX, diceY = prevX, prevY
        continue

    rollDice(operation)
    reconcileDiceAndFloor(diceX, diceY)
    print(dice[0])