import sys
# 간소화 버전(불필요 로직 삭제)
def calculateWeightOfWords(wordList):
    weightDict = dict()
    for word in wordList:
        length = len(word) - 1
        for alpha in word:
            if weightDict.get(alpha) is None:
                weightDict[alpha] = 10 ** length
            else:
                weightDict[alpha] = weightDict[alpha] + 10 ** length
            length -= 1
    sortedWeightDict = dict(sorted(weightDict.items(), key=lambda item:item[1], reverse=True))
    return sortedWeightDict


def getResult(weightDict):
    result = 0
    num = 9
    for key in weightDict.keys():
        result += weightDict[key] * num
        num -= 1
    return result


n = int(sys.stdin.readline())
wordList = [list(sys.stdin.readline().strip()) for i in range(n)]

weightDict = calculateWeightOfWords(wordList)
result = getResult(weightDict)

print(result)