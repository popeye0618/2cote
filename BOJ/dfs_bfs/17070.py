#파이프 옮기기1 (골드 5)
#내 풀이
#현재 상태가 가로인 경우, 세로인 경우, 대각선인 경우로
#현재 상태를 넣고, 그에 맞는 연산을 해준다.
#경로의 수를 탐색하니 dfs문제인 것 같다.
#dp를 이용해서 한 번 탐색한 곳은 중복해서 탐색하지 않도록 한다.
#dp에 방향을 추가해서 파이프에 따라 이동할 수 있는 방향을 모두 고려한다.

#피드백
#알게된 점은 dp를 사용할 때 -1로 초기화한 후 0을 만들고 사용하는 것이 더 좋다.
#값이 0인 것과 비교가 가능하기 때문에 더 정확하다.

import sys
input = sys.stdin.readline

def dfs(x, y, d):
  if x == n - 1 and y == n - 1:
    return 1
  
  if dp[x][y][d] != -1:
    return dp[x][y][d]
    
  dp[x][y][d] = 0
  #오른쪽 갈 수 있는 경우
  if d in (0, 1) and y + 1 < n and graph[x][y + 1] == 0:
      dp[x][y][d] += dfs(x, y + 1, 0)
  #아래로 갈 수 있는 경우
  if d in (1, 2) and x + 1 < n and graph[x + 1][y] == 0:
      dp[x][y][d] += dfs(x + 1, y, 2)
  #오른쪽 대각선 갈 수 있는 경우
  if x + 1 < n and y + 1 < n and graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
    dp[x][y][d] += dfs(x + 1, y + 1, 1)
  return dp[x][y][d]

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

if graph[n - 1][n - 1] == 1:
  print(0)
  exit(0)

dp = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]
#오른쪽 0, 대각 1, 아래 2
print(dfs(0, 1, 0))