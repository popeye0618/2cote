#안전 영역(실버 1)
#내 풀이
#이 문제는 dfs문제인 것 같다. 까다로운 부분이라고 하면 n의 값마다 그래프가 다르게 그려진다는 점이다. 우선 2부터 들어온 값의 최댓값까지 반복해봐야한다. 그 때 마다 그래프를 수정해서 dfs를 수행한다.

#피드백
#메모리 초과가 나서 알아보니 BFS방식이 더 효율적이라는 것을 알게되었다. 문제를 보고 어떤 알고리즘을 사용할지 정하는 연습이 더 필요하다.

# import copy
# import sys
# sys.setrecursionlimit(10000)

# def dfs(x, y):
#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]
#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if (0 <= nx < n) and (0 <= ny < n):
#       if field[ny][nx] >= height:
#         field[ny][nx] = 0
#         dfs(nx, ny)
      
# n = int(input())
# graph = []
# ans = []
# max_value = 0
# for _ in range(n):
#   t = list(map(int, input().split()))
#   if max_value < max(t):
#     max_value = max(t)
#   graph.append(t)

# for height in range(2, max_value + 1):
#   cnt = 0
#   field = copy.deepcopy(graph)
#   for i in range(n):
#     for j in range(n):
#       if field[i][j] >= height:
#         cnt += 1
#         dfs(j, i)

#   ans.append(cnt)

# print(max(ans))


from collections import deque

def bfs(x, y, h):
  queue = deque()
  queue.append((x, y))
  visited[y][x] = True
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (0 <= nx < n) and (0 <= ny < n) and graph[ny][nx] > h and not visited[ny][nx]:
          visited[ny][nx] = True
          queue.append((nx, ny))
      
n = int(input())
graph = []
ans = []
max_value = 0
for _ in range(n):
  t = list(map(int, input().split()))
  if max_value < max(t):
    max_value = max(t)
  graph.append(t)

for height in range(max_value + 1):
  visited = [[False for _ in range(n)] for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if (not visited[i][j]) and graph[i][j] > height:
        cnt += 1
        bfs(j, i, height)

  ans.append(cnt)
print(max(ans))