#카드 구매하기
#내 풀이
#dp[i]에는 i개의 카드를 사는 최대 가격
#i를 만드는 조합 중 max값으로 갱신

n = int(input())
price = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = price[0]
for i in range(2, n + 1):
  dp[i] = price[i - 1]
  for j in range(1, i):
    dp[i] = max(dp[i], dp[i - j] + dp[j])
    
print(dp[n])