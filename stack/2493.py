import sys


def findTopCatchingSignals(numOfTops, heightOfTops):
    result = [0] * numOfTops
    stack = []

    for idx in range(numOfTops):
        curTop = heightOfTops[idx]

        while stack and heightOfTops[stack[-1]] < curTop:
            stack.pop()

        result[idx] = stack[-1] + 1 if stack else 0
        stack.append(idx)

    return result


numOfTops = int(sys.stdin.readline())
heightOfTops = list(map(int, sys.stdin.readline().split()))

result = findTopCatchingSignals(numOfTops, heightOfTops)
print(" ".join(map(str, result)))

