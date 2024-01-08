#토마토(골드 5)
#내 풀이
#bfs문제로 보인다.
#큐에 1인 곳을 모두 넣고 시작
#방문을 거리표현으로 한다.

from collections import deque

def bfs():
  queue = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        queue.append((i, j))
        visited[i][j] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))


m, n = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]

bfs()

flag = False
for i in range(n):
  if flag:
    break
  for j in range(m):
    if visited[i][j] == 0 and graph[i][j] != -1:
      flag = True
      break

ans = max(max(row) for row in visited)

if flag:
  print(-1)
else:
  print(ans - 1)
