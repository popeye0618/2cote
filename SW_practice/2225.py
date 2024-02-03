#합분해
#내 풀이

# n, k = map(int, input().split())
# dp = [0] * (k + 1)
# dp[1] = 1
# if k >= 2:
#   dp[2] = n + 1

# num = list(range(n + 1, 0, -1))
# if k >= 3:
#   dp[3] = sum(num)
# for i in range(4, k + 1):
#   tmp = []
#   for j in range(len(num)):
#     t = sum(num[j:])
#     tmp.append(t)
#     dp[i] += t
#   num = tmp[:]
#   dp[i] %= 1000000000

# print(dp[k])

n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
  for j in range(n + 1):
    if i == 1:
      dp[i][j] = 1
    else:
      for t in range(j + 1):
        dp[i][j] += dp[i - 1][t]
        dp[i][j] %= 1000000000

print(dp[k][n])
