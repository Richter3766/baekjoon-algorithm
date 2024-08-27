import sys

def makeBlockMap():
    blockMap = [[0] * width for i in range(height)]

    for idx, blockHeight in enumerate(blockHeights):
        for i in range(1, blockHeight + 1):
            blockMap[-i][idx] = 1

    return blockMap


def fillRainToBlockMap():
    for r in range(height):
        rainIndexList = []
        isPossibleToFill = False
        for c in range(width):
            if not isPossibleToFill and blockMap[r][c] == 1:
                isPossibleToFill = True
            elif isPossibleToFill and blockMap[r][c] == 0:
                rainIndexList.append(c)
            elif isPossibleToFill and blockMap[r][c] == 1:
                fillRain(r, rainIndexList)
                rainIndexList.clear()


def fillRain(r, rainIndexList):
    global result
    for c in rainIndexList:
        blockMap[r][c] = 2
        result += 1


height, width = map(int, sys.stdin.readline().split())
blockHeights = list(map(int, sys.stdin.readline().split()))

result = 0

blockMap = makeBlockMap()
fillRainToBlockMap()

# print(*blockMap, sep="\n")
print(result)