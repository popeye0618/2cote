#숨바꼭질
#bfs를 사용해서 가장 거리가 먼 곳 중에서 가장 숫자가 작은 걸 출력

from collections import deque

def bfs():
  queue = deque()
  queue.append(1)
  visited[1] = 0
  max_value = 0
  while queue:
    now = queue.popleft()
    for x in graph[now]:
      if visited[x] == -1:
        queue.append(x)
        visited[x] = visited[now] + 1
        max_value = max(max_value, visited[x])

    
  ans = []
  for i in range(1, n + 1):
    if visited[i] == max_value:
      ans.append(i)
    
  return (ans[0], max_value, len(ans))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [-1] * (n + 1)
print(' '.join(map(str, bfs())))
