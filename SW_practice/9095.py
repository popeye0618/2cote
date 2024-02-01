#1,2,3 더하기
#내 풀이
#dp[i]에는 i를 1, 2, 3의 조합의 수

t = int(input())

for _ in range(t):
  n = int(input())
  dp = [1] * (n + 1)
  if n >= 2:
    dp[2] = 2
  if n >= 3:
    dp[3] = 4
  for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

  print(dp[n])
  