import sys
import heapq

def solution(rowSize, colSize, maze):
    heap = [(0, 0, 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    weights = [[float('inf') for i in range(colSize)] for i in range(rowSize)]
    weights[0][0] = 0

    while heap:
        b, r, c = heapq.heappop(heap)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rowSize and 0 <= nc < colSize:
                newWeight = weights[r][c] + maze[nr][nc]
                if newWeight < weights[nr][nc]:
                    weights[nr][nc] = newWeight
                    heapq.heappush(heap, (newWeight, nr, nc))

    return weights[-1][-1]


colSize, rowSize = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(rowSize)]

result = solution(rowSize, colSize, maze)
print(result)