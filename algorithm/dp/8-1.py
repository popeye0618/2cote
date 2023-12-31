#개미 전사
#문제 해결 아이디어
#ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
#a0 = 1, a1 = 3, a2 = 3, a3 = 8
#현재 식량 창고 i로 부터 i - 1과 i - 2 + i를 비교해서 더 큰 경우를 선택한다.

n = int(input())
k = list(map(int, input().split()))

dp = [0] * 100

#바텀업 방식
dp[0] = k[0]
dp[1] = max(k[0], k[1])
for i in range(2, n):
  a = dp[i - 1]
  b = dp[i - 2] + k[i]
  dp[i] = max(a, b)

print(dp[n - 1])