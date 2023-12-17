#영역 구하기
#내 풀이
#DFS를 이용해서 몇 개의 영역으로 나누어지는지를 구하면서, 다음 재귀로 넘어갈 때 마다 넓이 추가 후 마지막에 넓이 리턴
#피드백
#탐색 불가 지역 설정하는 것이 헷갈렸고, 방문했던 곳을 또 방문하는 경우가 생겨서 visited 리스트를 추가했다.
#인터넷을 찾아보니 bfs가 더 효율적이라고 해서 어떨 때 bfs이고 어떨 때 dfs인지 알아봐야겠다.

import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  global area
  visited[y][x] = True
  area += 1
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0 and not visited[ny][nx]:
      graph[ny][nx] = 1
      dfs(nx, ny)
  return area

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
ans = []
cnt = 0
area = 0

for _ in range(k):
  lx, ly, rx, ry = map(int, input().split())
  for y in range(ly, ry):
    for x in range(lx, rx):
      graph[y][x] = 1

for y in range(m):
  for x in range(n):
    if graph[y][x] == 0 and not visited[y][x]:
      cnt += 1
      ans.append(dfs(x, y))
      area = 0

ans.sort()
print(cnt)
print(' '.join(map(str, ans)))