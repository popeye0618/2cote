#보물섬(골드 5)
#내 풀이
#모든 경우에서 최대 거리가 나오는 곳을 구한다.
#최대 거리는 bfs로 찾는다

from collections import deque

def bfs(x, y):
  visited = [[-1] * m for _ in range(n)]
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 'L':
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

  max_value = 0
  for i in range(n):
    max_value = max(max_value, max(visited[i]))

  return max_value

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      dis = bfs(i, j)
      answer = max(answer, dis)

print(answer)