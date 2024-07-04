import sys

def findMax(N):
    if N == 1:
        return wines[0]
    elif N == 2:
        return wines[0] + wines[1]

    maxWine = [0] * N
    maxWine[0] = wines[0]
    maxWine[1] = wines[0] + wines[1]
    maxWine[2] = max(maxWine[1], maxWine[0] + wines[2], wines[1] + wines[2])

    for idx in range(3, N):
        maxWine[idx] = max(maxWine[idx - 1],
                           maxWine[idx - 2] + wines[idx],
                           maxWine[idx - 3] + wines[idx] + wines[idx - 1])
    return maxWine[-1]


N = int(sys.stdin.readline())
wines = [int(sys.stdin.readline()) for i in range(N)]

print(findMax(N))

