#효율적인 화폐구성

n, m = map(int, input().split())
money = []
dp = [10001] * (m + 1)
dp[0] = 0
for _ in range(n):
  t = int(input())
  money.append(t)

for i in range(n):
  for value in range(money[i], m + 1):
    if dp[value - money[i]] != 10001:
      dp[value] = min(dp[value], dp[value - money[i]] + 1)
if dp[m] == 10001:
  print(-1)
else:
  print(dp[m])