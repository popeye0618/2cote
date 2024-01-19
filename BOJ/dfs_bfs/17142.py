#연구소 3(골드 3)
#내 풀이
#visited 리스트의 값을 +1 해주는 방식으로 해본다.
#백트래킹 대신 조합을 사용해서 시간을 줄인다.
#계속해서 그래프를 수정하고 복사하는 것도 시간이 늘어나므로
#그래프를 바꾸지 않고, 방문 리스트로 바이러스가 전파되었는지 체크한다.
#그래프가 0인 visited 중에서 가장 큰 값을 리턴
#그래프가 0인데 방문하지 않은 경우는 바로 -1을 리턴 후 종료
#또한 -1을 출력하는 경우는 한 번이라도 다 퍼뜨리는 경우가 나오면 -1은 나오지 않게되므로
#초기 answer 값 그대로라면 -1을 출력한다.

from collections import deque
from itertools import combinations

def bfs(v):
  visited = [[-1 for _ in range(n)] for _ in range(n)]
  queue = deque(v)
  for x, y in v:
    visited[x][y] = 0
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] != 1:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

  max_value = 0
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 0:
        if visited[i][j] == -1:
          return -1
        max_value = max(max_value, visited[i][j])
  return max_value

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
  
virus = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      virus.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 2501
for c in combinations(virus, m):
  result = bfs(c)
  if result != -1:
    answer = min(answer, result)
print(answer) if answer != 2501 else print(-1) 
