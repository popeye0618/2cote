#트리의 지름
#내 풀이
#DFS로 모든 노드에서부터 모든 노드까지 가중치가 젤 긴걸 찾는다

#피드백
#트리의 특성과 dfs의 특성으로 인해 어느 지점에서 출발하던 가장 먼 곳에 도착하며,
#그 곳에서 최대 거리를 구하는 dfs를 한 번 더 돌리면 트리의 지름이 나온다.

import sys
sys.setrecursionlimit(10000)

def dfs(x, value):
  visited[x] = True
  max_x, max_value = x, value
  
  for nx, nv in graph[x]:
    if not visited[nx]:
      new_x, new_value = dfs(nx, value + nv)
      if new_value > max_value:
        max_value, max_x = new_value, new_x
  return max_x, max_value
  
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  a, b, v = map(int, input().split())
  graph[a].append((b, v))
  graph[b].append((a, v))

visited = [False] * (n + 1)
start, _ = dfs(1, 0)
visited = [False] * (n + 1)
_, answer = dfs(start, 0)

print(answer)