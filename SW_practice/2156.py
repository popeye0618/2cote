#포도주 시식
#내 풀이
#dp[i]에는 i잔째의 최대값
#계단오르기와 다른점은 마지막 칸을 반드시 밟는 조건이 없음
#따라서 이번 칸을 마시는 경우(계단오르기와 같음)와 이번 와인을 안마시는 경우를 비교

n = int(input())
arr = [0]
for _ in range(n):
  arr.append(int(input()))

dp = [0] * (n + 1)
dp[1] = arr[1]
if n >= 2:
  dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
  dp[i] = max(max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]), dp[i - 1])

print(max(dp))