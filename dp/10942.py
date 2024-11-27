import sys

def findPalinrome(numOfArray, infoOfArray):
    dp = [[False for i in range(numOfArray)] for j in range(numOfArray)]

    for i in range(numOfArray):
        dp[i][i] = True

    for i in range(numOfArray - 1):
        if infoOfArray[i] == infoOfArray[i + 1]:
            dp[i][i + 1] = True

    for length in range(3, numOfArray + 1):
        for i in range(numOfArray - length + 1):
            j = i + length - 1
            if infoOfArray[i] == infoOfArray[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    return dp

numOfArray = int(sys.stdin.readline())
infoOfArray = list(map(int, sys.stdin.readline().split()))
numOfQuestion = int(sys.stdin.readline())
infoOfQuestion = [list(map(int, sys.stdin.readline().split())) for i in range(numOfQuestion)]

dp = findPalinrome(numOfArray, infoOfArray)

for start, end in infoOfQuestion:
    if dp[start - 1][end -1]: print(1)
    else: print(0)