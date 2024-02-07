#평범한 배낭
#내 풀이
#dp[i][j]는 i번째 물건까지의 무게가 j인 배낭의 최댓값
#현재 물건을 안넣은 경우와, 현재 물건을 넣은 경우를 비교

n, k = map(int, input().split())
arr = [0]
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    w = arr[i][0]
    v = arr[i][1]

    if j < w:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])