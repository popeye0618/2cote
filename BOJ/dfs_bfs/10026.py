#적록색약(골드 5)
#내 풀이
#구역나누기이므로 bfs로 풀어야 할 것 같다.

from collections import deque

def bfs(x, y, c):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == c:
        queue.append((nx, ny))
        visited[ny][nx] = True
  
n = int(input())
graph = []
for _ in range(n):
  graph.append(input())
visited = [[False for _ in range(n)] for _ in range(n)]
nans = 0
wans = 0
for y in range(n):
  for x in range(n):
    if not visited[y][x]:
      if graph[y][x] == 'R':
        nans += 1
        bfs(x, y, 'R')
      elif graph[y][x] == 'G':
        nans += 1
        bfs(x, y, 'G')
      elif graph[y][x] == 'B':
        nans += 1
        bfs(x, y, 'B')

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  graph[i] = graph[i].replace('R', 'G')
for y in range(n):
  for x in range(n):
    if not visited[y][x]:
      if graph[y][x] == 'G':
        wans += 1
        bfs(x, y, 'G')
      elif graph[y][x] == 'B':
        wans += 1
        bfs(x, y, 'B')

print(nans, wans)
        
    