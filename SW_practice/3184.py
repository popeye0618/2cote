#양(실버 1)
#내 풀이
#bfs를 이용해서 각 영역 안에 양, 늑대의 수를 구한다.

from collections import deque

def bfs(x, y):
  global sheep, wolf
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  s, w = 0, 0

  while queue:
    x, y = queue.popleft()
    if graph[x][y] == 'o':
      s += 1
    elif graph[x][y] == 'v':
      w += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != '#':
        visited[nx][ny] = True
        queue.append((nx, ny))

  if s > w:
    sheep += s
  else:
    wolf += w


n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(input())

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sheep = 0
wolf = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] != '#' and not visited[i][j]:
      bfs(i, j)

print(sheep, wolf)