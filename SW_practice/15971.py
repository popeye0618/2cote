#두 로봇
#내 풀이
#DFS, BFS를 이용해서 두 로봇을 움직이며 만나는 경우 출력
#중요한 점은 로봇이 만나고 나서 가장 길었던 통로를 총 이동거리에서 빼주는 것
#bfs로 타뷸레이션 방식으로 dp에 b에서부터 모든 노드 거리 저장

from collections import deque

def bfs():
  queue = deque()
  queue.append((b, 0))
  dp[b] = 0

  while queue:
    t, v = queue.popleft()

    for x in graph[t]:
      if dp[x[0]] == -1:
        dp[x[0]] = v + x[1]
        queue.append((x[0], dp[x[0]]))

def dfs(a):
  global answer
  stack = []
  stack.append((a, 0, 0))
  visited = [False] * (n + 1)
  visited[a] = True
  while stack:
    t, v, max_len = stack.pop()
    answer = min(answer, v + dp[t] - max_len)
      
    for x in graph[t]:
      if not visited[x[0]]:
        n_len = max(max_len, x[1])
        stack.append((x[0], v + x[1], n_len))
        visited[x[0]] = True
    
n, a, b = map(int, input().split())
if n == 1 or a == b:
  print(0)
  exit(0)

graph = [[] for _ in range(n + 1)]
dp = [-1] * (n + 1)
answer = float('inf')
for _ in range(1, n):
  x, y, v = map(int, input().split())
  graph[x].append((y, v))
  graph[y].append((x, v))
bfs()
dfs(a)
print(answer)