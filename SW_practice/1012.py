#유기농 배추
#bfs이용해서 1 범위갯수 찾기

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
        queue.append((nx, ny))
        visited[nx][ny] = True

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  for _ in range(k):
    y, x = map(int, input().split())
    graph[x][y] = 1
  visited = [[False] * m for _ in range(n)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  answer = 0
  for x in range(n):
    for y in range(m):
      if not visited[x][y] and graph[x][y] == 1:
        answer += 1
        bfs(x, y)

  print(answer)