#연구소(골드 4)
#내 풀이
#백트래킹과 bfs를 활용해서 문제를 풀면 될 것 같다.
#벽을 3개 세우고 bfs 돌리고 벽 옮기고 bfs돌리고 해서
#bfs돌리고 나서 안전영역이 더 크면 저장 하는 식으로 반복한다.

from collections import deque
import copy

def bfs():
  global answer
  temp = copy.deepcopy(graph)
  queue = deque()
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
        temp[nx][ny] = 2
        queue.append((nx, ny))
        
  cnt = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        cnt += 1
  answer = max(answer, cnt)

def set_graph(count):
  if count == 3:
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        set_graph(count + 1)
        graph[i][j] = 0

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

answer = 0
set_graph(0)

print(answer)