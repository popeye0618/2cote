#벽 부수고 이동하기(골드 3)
#내 풀이
#우선 최단거리 문제이므로 bfs를 사용하는 문제라고 생각되고, 벽을 하나까지 깰 수 있으므로 count가 0이면 1로 올리면서 벽을 깨보고, 이동한 거리를 기록한다. 막힐 경우 다시 복귀하며 다른 곳 탐색해보고, 벽을 깨기 전으로 돌아오면 다른 벽을 깨고 다시 시작

#제출해보니 시간초과가 났고, n, m, 1 모두 탐색해서 그렇다. n * m크기로 탐색하는 방법을 생각해보자.

from collections import deque

def bfs(x, y, visited):
  queue = deque()
  queue.append((x, y))
  visited[y][x] += 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0 and visited[ny][nx] == 0:
        visited[ny][nx] = visited[y][x] + 1
        queue.append((nx, ny))


def set_graph():
  for y in range(n):
    for x in range(m):
      if graph[y][x] == 1:
        visited = [[0 for _ in range(m)] for _ in range(n)]
        graph[y][x] = 0
        bfs(0, 0, visited)
        if visited[n - 1][m - 1] != 0:
          ans.append(visited[n - 1][m - 1])
        graph[y][x] = 1

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

visitedf = [[0 for _ in range(m)] for _ in range(n)]
bfs(0, 0, visitedf)
set_graph()

if not ans:
  print(-1)
else:
  print(min(ans))