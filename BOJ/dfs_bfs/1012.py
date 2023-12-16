#유기농 배추(실버 2)
#내 풀이
#우선 DFS문제라고 생각되고, 상하좌우 네 방향을 탐색하면서 1이면 0으로 바꿔주면서 재귀를 돌린다. dfs함수를 실행할 때는 값이 1일 때 실행해서 붙어있는 1들을 다 0으로 바꿔준다.
#제출해보니 런타임 에러가 뜨는데, recursionError이므로 제한을 높여준다.

import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < m) and (0 <= ny < n):
      if graph[ny][nx] == 1:
        graph[ny][nx] = 0
        dfs(nx, ny)



t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  result = 0
  graph = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  for y in range(n):
    for x in range(m):
      if graph[y][x] == 1:
        result += 1
        dfs(x, y)
  print(result)
  