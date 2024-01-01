#평범한 배낭
#내 풀이
#dp를 이용하는 방식은 무게가 i인 배낭에 넣을 수 있는 최대 가치를 dp에 저장
#dp 원리는(점화식)
#가방의 용량보다 i번째 무게가 큰 경우 i - 1번째 dp를 그대로 가져온다.
#그렇지 않은 경우 i만큼의 용량을 비우고 i를 넣은 값과 용량을 비우기 전 i - 1과 비교한 최적값
#배낭문제 연습 더 필요

n, k = map(int, input().split())
w = []
v = []
for _ in range(n):
  weight, value = map(int, input().split())
  w.append(weight)
  v.append(value)
dp = [[0 for _ in range(k + 1)]for _ in range(n + 1)]

for i in range(n + 1):
 for j in range(k + 1):
  if i == 0 or j == 0:
    dp[i][j] = 0
  elif w[i - 1] <= j:
     dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j])
  else:
    dp[i][j] = dp[i - 1][j]

print(dp[n][k])
  