#점프점프 (실버 2)
#내 풀이
#dp 이용해서 더 적은 횟수로 해당 칸에 온 경우를 저장, 갱신

n = int(input())
arr = list(map(int, input().split()))
dp = [1001] * (n + 1)
dp[1] = 0

for i in range(1, n + 1):
  for j in range(i, i + arr[i - 1] + 1):
    if j <= n:
      dp[j] = min(dp[j], dp[i] + 1)

print(-1 if dp[n] == 1001 else dp[n])