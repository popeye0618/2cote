#합분해(골드 5)
#내 풀이
#이 문제는 dp에 i개 골라서 j를 만든 경우의 수를 담는다.

n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
  for j in range(n + 1):
    if i == 1 or j == 0:
      dp[i][j] = 1
    else:
      for t in range(j + 1):
        dp[i][j] += dp[i - 1][t]

print(dp[k][n] % 1000000000)