#아기상어(골드 3)
#내 풀이
#bfs로 아기상어로부터 물고기들의 거리를 계산
#결과를 토대로 어디로 이동할지를 계산

from collections import deque

def bfs(x, y):
  visited = [[-1] * n for _ in range(n)]
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

  min_value = 99999
  minx, miny = -1, -1
  for i in range(n):
    for j in range(n):
      if 0 < graph[i][j] < size and visited[i][j] > 0:
        if visited[i][j] < min_value:
          min_value = visited[i][j]
          minx, miny = i, j

  if minx == -1 and miny == -1:
    return 0, minx, miny

  return min_value, minx, miny
    
n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

size = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
x, y = -1, -1
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      x, y = i, j
      graph[i][j] = 0

cnt = 0
while True:
  value, nx, ny = bfs(x, y)
  
  if not value:
    break

  graph[nx][ny] = 0
  answer += value
  cnt += 1
  if cnt == size:
    cnt = 0
    size += 1

  x, y = nx, ny

print(answer)