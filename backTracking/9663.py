import sys

def solution(size):
    global result
    board = [-1] * size
    nqueen(board, 0)

def nqueen(board, row):
    global result
    if row == len(board):
        result += 1
        return

    for i in range(len(board)):
        if isSafe(board, row, i):
            board[row] = i
            nqueen(board, row + 1)

def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        elif abs(col - board[i]) == abs(row - i):
            return False
    return True

size = int(sys.stdin.readline())
result = 0
solution(size)
print(result)
