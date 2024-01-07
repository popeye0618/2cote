#트리의 부모 찾기
#내 풀이
#bfs를 이용해서 각 노드의 부모를 파악한다.

from collections import deque

def bfs():
  queue = deque()
  queue.append(1)
  visited[1] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        answer[i] = v

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


visited = [False] * (n + 1)
answer = [0] * (n + 1)
bfs()
for x in answer[2:]:
  print(x)