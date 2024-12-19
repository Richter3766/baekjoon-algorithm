import sys
from itertools import combinations

# a, n, t, c, i

def findCharSet(words):
    charSet = set()
    for word in words:
        for char in word[4:-4]:
            if char not in default:
                charSet.add(char)
    return charSet


def findMaxWords(charSet, words):
    cur = 0
    for word in words:
        isPossible = True
        for char in word[4:-4]:
            if char not in charSet:
                isPossible = False
                break
        if isPossible:
            cur += 1
    return cur

default = {'a', 'n', 't', 'c', 'i'}

N, K = map(int, sys.stdin.readline().split())
words = [list(sys.stdin.readline().strip()) for i in range(N)]

if K < 5:
    print(0)
elif K > 5:
    charSet = findCharSet(words)
    maxNum = 0
    if len(charSet) < K - 5:
        maxNum = findMaxWords(default.union(charSet), words)
    else:
        for comb in combinations(charSet, K - 5):
            maxNum = max(maxNum, findMaxWords(default.union(comb), words))
    print(maxNum)
else:
    maxNum = findMaxWords(default, words)
    print(maxNum)
