#노드 사이의 거리 (골드 5)
#내 풀이
#bfs를 이용해서 노드 탐색하면 된다.

from collections import deque

def bfs(start, end):
  queue = deque()
  queue.append((start, 0))
  visited[start] = True

  while queue:
    now, dis = queue.popleft()
    if now == end:
      print(dis)
      return
      
    for next, d in graph[now]:
      if not visited[next]:
        visited[next] = True
        queue.append((next, dis + d))

n, m = map(int, input().split())
graph = [[]for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, d = map(int, input().split())
  graph[a].append((b, d))
  graph[b].append((a, d))

for _ in range(m):
  start, end = map(int, input().split())
  visited = [False] * (n + 1)
  bfs(start, end)