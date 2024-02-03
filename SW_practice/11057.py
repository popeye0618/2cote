#오르막 수
#내 풀이
#dp이용

n = int(input())
answer = [0] * (n + 1)

answer[1] = 10

num = [1] * 10
for i in range(2, n + 1):
  tmp = []
  for j in range(10):
    t = sum(num[j:])
    tmp.append(t)
    answer[i] += t
  num = tmp[:]
  answer[i] %= 10007

print(answer[n])

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(n):
  for j in range(10):
    if i == 0:
      dp[i][j] = 1
    else:
      for k in range(j, 10):
        dp[i][j] += dp[i - 1][k]
        dp[i][j] %= 10007

print(sum(dp[n - 1]) % 10007)


n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]
dp[0] = [1] * 10

for i in range(1, n):
  for j in range(10):
    dp[i][j] = sum(dp[i - 1][j:]) % 10007

print(sum(dp[n - 1]) % 10007)
  