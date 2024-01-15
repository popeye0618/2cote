#맥주 마시면서 걸어가기(골드 5)
#내 풀이
#맥주를 들고 이동할 수 있는 최대거리는 1000이다.
#따라서 편의점이든 목적지든 거리가 1000 이하라면 갈 수 있는 곳이다.
#그리고 편의점을 갔다면 다시 그곳에서부터 1000만큼 갈 수 있다.
#따라서 bfs를 돌 때, 두 지점 사이의 거리가 1000 이하라면 큐에 넣어주는 방식

from collections import deque

def distance(a, b):
  x = abs(a[0] - b[0])
  y = abs(a[1] - b[1])
  return x + y

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited.add((x, y))

  while queue:
    x, y = queue.popleft()
    if x == dest[0] and y == dest[1]:
      return True
    for k in graph:
      if distance((x, y), k) <= 1000 and k not in visited:
        visited.add(k)
        queue.append(k)
  return False

t = int(input())
for _ in range(t):
  n = int(input())
  start = tuple(map(int, input().split()))
  graph = []
  for _ in range(n):
    graph.append(tuple(map(int, input().split())))
  dest = tuple(map(int, input().split()))
  graph.append(dest)
  visited = set()
  print('happy') if bfs(start[0], start[1]) else print('sad')
  