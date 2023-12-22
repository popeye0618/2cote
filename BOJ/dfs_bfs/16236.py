#아기 상어(골드 3)
#내 풀이
#bfs문제이며, 계속해서 바뀌는 아기상어의 크기에 맞춰서 문제를 풀어야한다.
#중요한건 목적지를 정하는 부분인 것 같은데 현재 위치에서 bfs를 돌려서 목적지를 찾고,
#그 목적지에서 또 돌리고 해서 이동할 때 마다 계속해서 bfs를 돌려보자
#bfs로 거리를 계산하고, 반복문으로 왼쪽 위에서부터 먹을 수 있는 물고기중 가장 가까우며 가장 왼쪽 위에 있는 물고기를 먹는다.

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] <= size:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
time = 0
size = 2
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while True:
  visited = [[0 for _ in range(n)] for _ in range(n)]
  c = False
  for x in range(n):
    if c:
      break
    for y in range(n):
      if graph[x][y] == 9:
        bfs(x, y)
        graph[x][y] = 0
        c = True
        break
        
  min_value = 99999
  minx, miny = -1, -1
  for x in range(n):
    for y in range(n):
      if 0 < graph[x][y] < size and visited[x][y] > 0:
        if visited[x][y] < min_value:
          min_value = visited[x][y]
          minx, miny = x, y

  if minx == -1 and miny == -1:
    break
  time += min_value
  graph[minx][miny] = 9
  cnt += 1
  if cnt == size:
    cnt = 0
    size += 1

print(time)