def prime_seive(n):
    '''에라토스테네스 체로 소수 구하는 함수'''
    primes = []
    is_prime = [True] * (n + 1)

    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)
            is_prime[num * num::num] = [False] * ((n - num * num) // num + 1)

    return primes


def count_n(primes, target):
    '''투 포인터를 활용하여 연속된 소수의 합으로 나타낼 수 있는 경우의 수 카운팅하는 함수'''
    count = 0
    cur_sum, left, right = 0, 0, 0
    length = len(primes)
    while True:
        if right > length: break
        if cur_sum < target:
            if right < length:
                cur_sum += primes[right]
            else: break
            right += 1
        elif cur_sum > target:
            cur_sum -= primes[left]
            left += 1
        else:
            count +=1
            if right < length:
                cur_sum += primes[right]
            else: break
            right += 1
    return count


n = int(input())

primes = prime_seive(n)
result = count_n(primes, n)
print(result)