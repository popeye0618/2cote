#병사 배치하기
#가장 긴 감소하는 부분수열 문제

n = int(input())
array = list(map(int, input().split()))
#순서를 뒤집어서 최장 증가 부분수열 문제로 변환
array.reverse()
dp = [1] * n

#LIS(가장 긴 증가하는 부분수열)
for i in range(1, n):
  for j in range(0, i):
    if array[i] > array[j]:
      dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))