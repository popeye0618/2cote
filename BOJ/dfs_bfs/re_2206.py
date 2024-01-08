#벽 부수고 이동하기(골드 3)
#내 풀이
#사실 이 문제는 어떻게 푸는지 기억이 난다.
#하지만 어려운 문제였고, 제대로 이해했는지 알기 위해 한번 더 풀어본다.
#풀이 방법은 벽을 만났으며, 벽을 꺨 수 있으면 벽을 깨고
#벽을 깬 순간 두 개의 세계로 나뉘어 지는데
#벽을 깬 세계 따로, 벽을 안 깬 세계 따로 이렇게 나눠진다.
#따라서 방문처리할 때 벽을 깬 세계, 안 깬 세계까지 표시를 해줘야 한다.

#피드백
#풀이법이 기억나서 망정이지 혼자였음 절대 못풀었다.
#단순히 좌표만을 넣어 방문체크 하는 것이 아닌 좌표와 벽을 부순적이 있는지에 대한 
#현재 상태도 visited에 넣어줘야한다.
#다음에 또 풀어보자

from collections import deque

def bfs():
  queue = deque()
  queue.append((0, 0, False, 0))
  visited[0][0][0] = True
  visited[0][0][1] = True
  while queue:
    x, y, wall, dis = queue.popleft()
    if x == n - 1 and y == m - 1:
      print(dis + 1)
      return
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][wall]:
        if graph[nx][ny] == '0':
          visited[nx][ny][wall] = True
          queue.append((nx, ny, wall, dis + 1))
        else:
          if wall == 0:
            visited[nx][ny][wall] = True
            queue.append((nx, ny, 1, dis + 1))
  print(-1)

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

visited = [[[False, False] for _ in range(m)]for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()