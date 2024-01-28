#n을 만들기 위해 1과 m으로 조합 구성
#dp를 이용해서 dp[i]는 i초 까지의 조합의 개수이다.
#1초 스킬을 사용하느냐, m초 전에서 m초 스킬을 사용하느냐
#1초 스킬은 경우의 수가 dp[i - 1] 만큼 늘어난다.
#m초 스킬은 경우의 수가 dp[i - m] 만큼 늘어난다.

n, m = map(int, input().split())
dp = [1] * (n + 1)

for i in range(m, n + 1):
  dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007

print(dp[n])