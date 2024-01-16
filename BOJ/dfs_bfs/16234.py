#인구 이동(골드 4)
#내 풀이
#bfs를 이용해서 연합인 경우 각 숫자 더해줘서 더 이상 연합이 아니면 인원 배정
#연합이 없을 때까지 실행

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  cnt = 1
  sum = graph[x][y]
  visited[x][y] = True
  people = [(x, y)]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if a <= abs(graph[x][y] - graph[nx][ny]) <= b:
          cnt += 1
          sum += graph[nx][ny]
          queue.append((nx, ny))
          visited[nx][ny] = True
          people.append((nx, ny))

  value = sum // cnt
  for i, j in people:
    graph[i][j] = value
  return cnt

n, a, b = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
while True:
  visited = [[False] * n for _ in range(n)]
  flag = False
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        if bfs(i, j) > 1:
          flag = True
  if not flag:
    break
  answer += 1
print(answer)