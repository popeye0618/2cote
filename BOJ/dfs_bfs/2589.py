#보물섬(골드 5)
#내 풀이
#보물이 묻혀있는 곳을 찾기 위해 bfs를 이용하여 최단거리를 찾아야 한다.
#피드백
#자꾸 bfs돌릴 때 처음 위치 방문처리 안하는거 고쳐야 한다.

from collections import deque

def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((x, y))
  visited[y][x] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and graph[ny][nx] == 'L':
        queue.append((nx, ny))
        visited[ny][nx] = visited[y][x] + 1

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())
max_value = 0

for y in range(n):
  for x in range(m):
    if graph[y][x] == 'L':
      visited = [[0 for _ in range(m)] for _ in range(n)]
      bfs(x, y)
      for i in range(n):
        if max_value < max(visited[i]):
          max_value = max(visited[i])

print(max_value - 1)
    