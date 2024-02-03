#동물원
#내 풀이
#규칙 찾아서 dp에 적용함..
#내 점화식은 dp[i - 1] * dp[1] - (dp[i - 1] - dp[i - 2])
#정답 점화식은 2 * dp[i - 1] + dp[i - 2]
#암튼 맞음 ㅋ(내 것도 정답 맞긴함 복잡해서 그렇지)

n = int(input())
dp = [0] * (n + 1)
dp[1] = 3
if n >= 2:
  dp[2] = 7

for i in range(3, n + 1):
  tmp = dp[i - 1] - dp[i - 2]
  dp[i] = dp[i - 1] * dp[1] - tmp
  dp[i] %= 9901
print(dp[n])
