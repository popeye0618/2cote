#토마토(골드 5)
#내 풀이
#우선 주어진 상황이 3차원이기 때문에 3차원 리스트를 사용해야할 것 같은데
#잘 사용할 수 있을지 모르겠다.
#그냥 높이만 추가해서 bfs돌리면 되는게 그리 어렵지 않았다.

from collections import deque

def bfs():
  queue = deque()
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 1:
          queue.append((i, j, k))

  while queue:
    z, x, y = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dh[i]
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        queue.append((nz, nx, ny))


m, n, h = map(int, input().split())
graph = []
temp = []
for _ in range(h):
  for _ in range(n):
    temp.append(list(map(int, input().split())))
  graph.append(temp)
  temp = []

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

bfs()

flag = False
for i in range(h):
  if flag: break
  for j in range(n):
    if flag: break
    for k in range(m):
      if graph[i][j][k] == 0:
        flag = True
        break
if flag:
  print(-1)
else:
  max_value = max(max(max(sublist) for sublist in submatrix) for submatrix in graph)
  print(max_value - 1)