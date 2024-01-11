#빙산 (골드 4)
#내 풀이
#이 문제는 bfs를 돌면서 다음 지점이 0인경우 그래프의 값을 -1 해준다.

#피드백
#아직도 어디가 문제였는지 모르겠다. 계속 수정만 하면 이런 결과가 발생한다.
#풀이를 보고나서 이해한 점
#우선 빙산의 개수를 셀 때, 연결된 빙산들을 다 돌면서 인접한 물의 개수를 저장하고
#bfs를 한 번 돌릴 때마다 빙산도 1개 있다는 뜻이다.
#따라서 리턴값을 아무거나 주면서 answer 리스트의 길이로 빙산이 몇 개인지 센다.
#그래서 빙산의 개수가 1이면 반복하지만 0이거나 2가 넘을 경우 종료하고 출력한다.
#반복문을 돌린 횟수가 걸린 시간을 뜻한다.

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if graph[nx][ny] > 0:
          queue.append((nx, ny))
          visited[nx][ny] = True
        else:
          count[x][y] += 1

  return 1

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while True:
  answer = []
  visited = [[False for _ in range(m)] for _ in range(n)]
  count = [[0 for _ in range(m)] for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0 and not visited[i][j]:
        answer.append(bfs(i, j))

  for i in range(n):
    for j in range(m):
      graph[i][j] = max(graph[i][j] - count[i][j], 0)

  if len(answer) == 0 or len(answer) >= 2:
    break
  year += 1

print(year) if len(answer) else print(0)