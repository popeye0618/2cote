#미로 탈출
#N * M 크기의 직사각형 형태의 미로가 있다. 처음 위치는 (1, 1)이며, 미로의 출구는 (N, M)에 존재한다. 한 번에 한 칸씩 이동할 수 있으며, 괴물이 있는 부분은 0, 괴물이 없는 부분은 1이다. 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하라.(시작 칸, 마지막 칸, 포함)

#문제 해결 아이디어
#BFS는 간선의 비용이 모두 같을 때 최단거리를 탐색할 때 사용하는 알고리즘(시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문)

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n - 1][m - 1]
    

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))
