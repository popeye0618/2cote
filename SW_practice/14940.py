#쉬운 최단거리
#내 풀이
#BFS를 이용해서 시작지점부터 visited 리스트에 거리를 저장, 출력

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] != 0:
        queue.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
  for y in range(m):
    if graph[x][y] == 2:
      bfs(x, y)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      visited[i][j] += 1
    print(visited[i][j], end = ' ')
  print()