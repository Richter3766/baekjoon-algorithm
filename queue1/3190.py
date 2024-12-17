import sys
from collections import deque

def checkBoundary(row, col):
    if row >= sizeN or row < 0 or col >= sizeN or col < 0 or (row, col) in body:
        return True
    return False

def checkApple(row, col):
    if board[row][col] == 1:
        board[row][col] = 0
        return True
    return False

def decideDirection(drow, dcol, direction):
    if direction == 'L':
        return -dcol, drow
    else:
        return dcol, -drow


def simulation():
    global result, row, col
    result += 1
    row, col = row + drow, col + dcol
    if checkBoundary(row, col):
        print(result)
        exit(0)
    body.append((row, col))

    if not checkApple(row, col):
        body.popleft()

sizeN = int(sys.stdin.readline())
board = [[0 for i in range(sizeN)] for j in range(sizeN)]

numOfApples = int(sys.stdin.readline())
for i in range(numOfApples):
    row, col = map(int, sys.stdin.readline().split())
    board[row - 1][col - 1] = 1

numOfRotation = int(sys.stdin.readline())
body = deque()
body.append((0, 0))
row, col = 0, 0
drow, dcol = 0, 1
result = 0

for i in range(numOfRotation):
    time, direction = sys.stdin.readline().split()
    for j in range(int(time) - result):
        simulation()
    drow, dcol = decideDirection(drow, dcol, direction)

while True:
    simulation()