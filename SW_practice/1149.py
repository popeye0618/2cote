#RGB거리
#내 풀이
#dp[i]는 i번째 집까지의 최소 비용
#dp에 넣을 때는 이전 집의 색 하나를 골랐을 때, 나머지 둘 중 최소값

#피드백
#처음 생각한 방법이 안되는 경우가 있다는 건 알았는데, 어떻게 개선해야할지 생각이 안남
#그냥 브루트포스를 메모이제이션하는 방법으로 DP사용
#모든 경우에서의 최소값을 dp에 저장, 마지막에 셋 중 최소값을 출력

n = int(input())
house = []
for _ in range(n):
  house.append(list(map(int, input().split())))

dp = [[3001 for _ in range(3)] for _ in range(n)]
for i in range(3):
  dp[0][i] = house[0][i]

for i in range(1, n):
  for j in range(3):
    if j == 0:
      dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][j]
    elif j == 1:
      dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][j]
    elif j == 2:
      dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][j]

print(min(dp[n - 1]))