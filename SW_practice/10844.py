#쉬운 계단수
#dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

mod = 1000000000
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(10):
    if i == 1:
      dp[i][j] = 1
    elif j == 0:
      dp[i][j] = dp[i - 1][j + 1] % mod
    elif j == 9:
      dp[i][j] = dp[i - 1][j - 1] % mod
    else:
      dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod

print((sum(dp[n]) - dp[n][0]) % mod)