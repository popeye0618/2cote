#RGB거리(실버 1)
#내 풀이
#dp를 이용

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
dp = [[3001 for _ in range(3)]for _ in range(n)]

for j in range(3):
  dp[0][j] = arr[0][j]

for i in range(1, n):
  for j in range(3):
    #red
    if j == 0:
      dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][j]
    #green
    elif j == 1:
      dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][j]
    #blue
    else:
      dp[i][j] = min(dp[i - 1][1], dp[i - 1][0]) + arr[i][j]

print(min(dp[n-1]))