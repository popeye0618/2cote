#2xn 타일링
#내 풀이
#dp[i]는 i - 1에 세로 붙이는거 + i - 2에 가로 정사각형 붙이는거

n = int(input())
mod = 10007
dp = [1] * (n + 1)
if n >= 2:
  dp[2] = 2

for i in range(3, n + 1):
  dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[n])