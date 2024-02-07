#연속합
#내 풀이
#dp[i]에는 i에서의 최대값
#현재 i를 연속된 값에 더했을 때 현재 i의 값보다 크면 연속
#현재 i 보다 작아지면 연속이 끊김

n = int(input())
num = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = num[0]

for i in range(1, n):
  dp[i] = max(num[i], dp[i - 1] + num[i])

print(max(dp))