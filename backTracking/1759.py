import sys

def makePassword(target):
    return ''.join(target)


def printIfValid(password):
    sumOfVowel = sum(1 for char in password if char in vowels)
    sumOfConsonant = sum(1 for char in password if char not in vowels)

    if sumOfVowel >= 1 and sumOfConsonant >= 2:
        print(makePassword(password))


def backTracking(password, idx):
    if idx == length:
        printIfValid(password)
        return

    for i in range(idx, numOfAlphbets):
        if alphabets[i] > password[idx - 1]:
            password[idx] = alphabets[i]
            backTracking(password, idx + 1)

def solution(length, numOfAlphbets, alphabets):
    password = ['a'] * length

    for char in alphabets[:numOfAlphbets - length + 1]:
        password[0] = char
        backTracking(password, 1)


length, numOfAlphbets = map(int, sys.stdin.readline().split())
alphabets = list(sys.stdin.readline().strip().split())
alphabets.sort()

vowels = set('aeiou')
solution(length, numOfAlphbets, alphabets)