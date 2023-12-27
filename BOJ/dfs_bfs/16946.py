#벽 부수고 이동하기4(골드 2)
#내 풀이
#bfs문제인 것 같고, 맵을 탐색하면서 1인 경우 0으로 바꾸고, 인접한 0의 개수 저장하고 반복

#피드백
#처음 아이디어로 문제를 풀 경우 시간초과가 발생한다.
#그 이유는 1인 칸에서 bfs를 하면 0을 중복탐색하므로 시간복잡도가 커지게 된다.
#따라서 새로운 아이디어는 처음에 묶여있는 0이 몇 개인지 따로 저장해두고
#맵을 한 번만 돌면서 상하좌우 묶여있는 정보만 더해주면 될 것 같다.

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  cnt = 1
  temp = []

  while queue:
    a, b = queue.popleft()
    temp.append((a, b))
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
        visited[nx][ny] = True
        queue.append((nx, ny))
        cnt += 1

  for c, d in temp:
    zero[c][d] = cnt
    tag[c][d] = t
    
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

zero = [[0 for _ in range(m)] for _ in range(n)]
tag = [[0 for _ in range(m)] for _ in range(n)]
ans = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]

t = 1
for x in range(n):
  for y in range(m):
    if graph[x][y] == 0 and not visited[x][y]:
      bfs(x, y)
      t += 1

for x in range(n):
  for y in range(m):
    if graph[x][y] == 1:
      ans[x][y] += 1
      tmp = [0]
      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and tag[nx][ny] not in tmp:
          ans[x][y] += zero[nx][ny]
          tmp.append(tag[nx][ny])
      ans[x][y] %= 10
      
for i in range(n):
  print(''.join(map(str, ans[i])))