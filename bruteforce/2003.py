def countResult(N, M, A):
    count = 0
    left = 0
    currentSum = 0

    for right in range(N):
        currentSum += A[right]

        while currentSum > M and left <= right:
            currentSum -= A[left]
            left += 1

        if currentSum == M:
            count += 1

    return count


N, M = map(int, input().split())
listOfNums = list(map(int, input().split()))

result = countResult(N, M, listOfNums)

print(result)
