import sys
from collections import Counter

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


def convertWeightToNumber(weightDict):
    num = 9
    for key in weightDict.keys():
        weightDict[key] = num
        num -= 1
    return weightDict


def convertWordToNumber(wordList, weightDict):
    numList = []
    for i in range(len(wordList)):
        for j in range(len((wordList[i]))):
            wordList[i][j] = weightDict[wordList[i][j]]
        numList.append(int(''.join(map(str, wordList[i]))))
    return numList


n = int(sys.stdin.readline())
wordList = [list(sys.stdin.readline().strip()) for i in range(n)]

weightDict = calculateWeightOfWords(wordList)
weightDict = convertWeightToNumber(weightDict)
numList = convertWordToNumber(wordList, weightDict)

print(sum(numList))