import sys

def solution(row_size, col_size, board):
    dp_table = [[0 for _ in range(col_size + 1)] for _ in range(row_size + 1)]

    for r in range(1, row_size + 1):
        for c in range(1, col_size + 1):
            if board[r - 1][c - 1] == 1:
                if dp_table[r - 1][c] == dp_table[r - 1][c - 1] == dp_table[r][c - 1]:
                    dp_table[r][c] = dp_table[r][c - 1] + 1
                else:
                    dp_table[r][c] = min(dp_table[r - 1][c], dp_table[r][c - 1], dp_table[r - 1][c - 1]) + 1
    max_value = 0
    for row in dp_table:
        max_value = max(max(row), max_value)

    return max_value

row_size, col_size = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for i in range(row_size)]
result = solution(row_size, col_size, board)

print(result ** 2)