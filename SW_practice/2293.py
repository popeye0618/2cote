#동전 1
#내 풀이
#dp를 이용하고 dp[i]에는 i원에서 사용하는 동전의 개수
#모든 동전 m에 대해 dp[i] += dp[i - m]

n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
  for i in range(coin, k + 1):
    dp[i] += dp[i - coin]
    
print(dp[k])