#01타일
#내 풀이
#dp를 이용

n = int(input())
dp = [1] * (n + 1)
if n >= 2:
  dp[2] = 2

for i in range(3, n + 1):
  dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
