#동전 2
#내 풀이
#dp를 사용하고 dp에는 금액 i을 만드는데 사용한 최소 동전 개수가 들어간다.

n, k = map(int, input().split())
money = []
for _ in range(n):
  money.append(int(input()))

dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for i in range(len(money)):
  for j in range(money[i], k + 1):
    if dp[j - money[i]] != 10001:
      dp[j] = min(dp[j - money[i]] + 1, dp[j])

if dp[k] == 10001:
  print(-1)
else:
  print(dp[k])