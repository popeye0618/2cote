#오르막 수
#내 풀이
#dp이용

n = int(input())
dp = [0] * (n + 1)

dp[1] = 10

num = [1] * 10
for i in range(2, n + 1):
  tmp = []
  for j in range(10):
    t = sum(num[j:])
    tmp.append(t)
    dp[i] += t
  num = tmp[:]
  dp[i] %= 10007

print(dp[n])