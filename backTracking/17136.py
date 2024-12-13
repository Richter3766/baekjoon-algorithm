import sys

# 색종이 붙일 곳 검사
def countOne(board):
    return sum(sum(i) for i in board )

# 색종이 붙이기 가능 여부
def isPossible(board, size, row, col):
    if row + size > 10 or col + size > 10:
        return False    
    
    for r in range(size):
        for c in range(size):
            if board[row + r][col + c] == 0:
                return False
    
    return True

# 색종이 붙이기
def putOnPaper(board, size, row, col):
    for r in range(size):
        for c in range(size):
            board[r + row][c + col] = 0
            

# 색종이 떼기
def putOffPaper(board, size, row, col):
    for r in range(size):
        for c in range(size):
            board[r + row][c + col] = 1


def backTracking(board, papers, paperCount):
    if countOne(board) == 0:
        return paperCount

    minCount = float('inf')
    for r in range(length):
        for c in range(length):
            if board[r][c] == 1:
                for size in range(4, -1, -1):
                    if papers[size] > 0 and isPossible(board, size + 1, r, c):
                        papers[size] -= 1
                        putOnPaper(board, size + 1, r, c)
                        result = backTracking(board, papers, paperCount + 1)
                        minCount = min(result, minCount)
                        putOffPaper(board, size + 1, r, c)
                        papers[size] += 1
                return minCount
    return minCount


def solution(board):
    papers = [5] * 5
    result = backTracking(board, papers, 0)

    return result if result != float('inf') else -1




length = 10
board = [list(map(int, sys.stdin.readline().split())) for i in range(10)]

result = solution( board)
print(result)