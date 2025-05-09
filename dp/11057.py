n = int(input())  # 수의 길이 N 입력 받기

# dp[i][j]: 길이가 i이고 마지막 자릿수가 j인 오르막 수의 개수
dp = [[0] * 10 for _ in range(n + 1)]
dp[0] = [1] * 10

# 길이를 1부터 n까지 늘려가며 DP 테이블 채우기
for length in range(1, n + 1):
    # 마지막 자릿수를 0부터 9까지 바꿔가며 계산
    for last_digit in range(10):
        # 길이가 length-1이고 마지막 자릿수가 last_digit인 경우들을 먼저 더함
        dp[length][last_digit] += dp[length - 1][last_digit]

        # 마지막 자릿수가 0보다 크다면,
        # 길이가 length이고 마지막 자릿수가 last_digit-1인 경우들에 last_digit을 붙이는 경우를 더함
        if last_digit > 0:
            dp[length][last_digit] += dp[length][last_digit - 1]

# 결과를 10007로 나눈 나머지 출력
print(dp[n][9] % 10007)

