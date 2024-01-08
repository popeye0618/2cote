#내리막 길(골드 3)
#내 풀이
#dfs를 이용해서 목적지에 도착하는 개수를 세면 될 것 같다.
#시간복잡도를 생각하면 한 번 방문한 곳은 다시 경로를 재탐색하지 않아도 된다.
#따라서 메모이제이션을 통해 그 지점에서의 경로의 수를 저장해놓고
#지점에 도착하면 더해줘서 시간복잡도를 줄일 수 있다.

def dfs(x, y):
  if x == n - 1 and y == m - 1:
    return 1
  if dp[x][y] != -1:
    return dp[x][y]
  dp[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
      dp[x][y] += dfs(nx, ny)
  return dp[x][y]
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1 for _ in range(m)] for _ in range(n)]
answer = dfs(0, 0)
print(answer)