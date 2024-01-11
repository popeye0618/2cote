#스타트링크
#내 풀이
#현재 층에서 올라가고 내려가는걸 모두 해본다.
#목표 층을 방문하면 visited 값을 출력하고 멈춘다.

from collections import deque

def bfs(s):
  queue = deque()
  queue.append(s)
  visited[s] = 1
  while queue:
    x = queue.popleft()
    if x == g:
      return True
    for i in range(2):
      nx = x + dx[i]
      if 1 <= nx <= f and visited[nx] == 0:
        queue.append(nx)
        visited[nx] = visited[x] + 1
  return False
  

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
dx = [u, -d]

if bfs(s):
  print(visited[g] - 1)
else:
  print('use the stairs')