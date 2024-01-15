#그림(실버 1)
#내 풀이
#그림의 넓이를 세는 bfs에 리턴값도 줘서 몇 개인지도 센다.

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  count = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = True
        queue.append((nx, ny))
        count += 1
  return count

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      answer.append(bfs(i, j))

if len(answer):
  print(len(answer))
  print(max(answer))
else:
  print(0)
  print(0)