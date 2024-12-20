import sys
from collections import deque

def inspectBoard(board, row, col):
    moverQueue, waterQueue = deque(), deque()
    for r in range(row):
        for c in range(col):
            if board[r][c] == location:
                moverQueue.append((r, c))
            elif board[r][c] == water:
                waterQueue.append((r, c))
    return moverQueue, waterQueue


def waterSpread(board, waterQueue):
    newWaterQueue = deque()
    while waterQueue:
        r, c = waterQueue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0<= nr < row and 0<= nc < col and (board[nr][nc] == empty or board[nr][nc] == location):
                newWaterQueue.append((nr, nc))
                board[nr][nc] = water

    return newWaterQueue


def move(board, moverQueue):
    newMoverQueue = deque()
    isPossible = False
    while moverQueue:
        r, c = moverQueue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0<= nr < row and 0<= nc < col:
                if board[nr][nc] == empty:
                    newMoverQueue.append((nr, nc))
                    board[nr][nc] = location
                elif board[nr][nc] == destination:
                    isPossible = True
                    return newMoverQueue, isPossible

    return newMoverQueue, isPossible


row, col = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for i in range(row)]

location = 'S'
destination = 'D'
stone = 'X'
empty = '.'
water = '*'
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

moverQueue, waterQueue = inspectBoard(board, row, col)
dayCount = 0
while True:
    dayCount += 1
    waterQueue = waterSpread(board, waterQueue)
    moverQueue, isPossible = move(board, moverQueue)

    if isPossible:
        print(dayCount)
        break

    if not moverQueue:
        print("KAKTUS")
        break



