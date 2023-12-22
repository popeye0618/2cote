#벽 부수고 이동하기(골드 3)
#내 풀이
#우선 최단거리 문제이므로 bfs를 사용하는 문제라고 생각되고, 벽을 하나까지 깰 수 있으므로 count가 0이면 1로 올리면서 벽을 깨보고, 이동한 거리를 기록한다. 막힐 경우 다시 복귀하며 다른 곳 탐색해보고, 벽을 깨기 전으로 돌아오면 다른 벽을 깨고 다시 시작

#피드벡
#결국 해설을 봤다. 우선 아이디어부터 처음봤어서 아마 고민을 해도 굉장히 오래걸렸을 것 같은데,
#일단 아이디어는 문제가 벽을 부술수도 있고, 안부술 수도 있으니 모든 벽에 대해 깨고가는 경로를 확인하면 시간초과이고,
#따라서 방문여부를 체크할 때 현재 상태를 표시해줘야 한다.
#벽을 부순 경우와 부수지 않은 경우를 체크해주면서, 약간 두 개의 세계선이 있는 느낌인데 z가 0인 아직 벽을 부수지 않은 세계선과
#z가 1인 벽을 부수고 난 세계선이 존재하며, 아예 각각의 세계라서 내가 벽을 뚫고 오지 않았어도, 한 번 벽을 부수면 내가 지나온 곳도 다시 탐색할 수 있다.
#결국 반복문을 늘리거나 하는것이 아닌, 상태를 하나 더 추가해서 이중 반복문 안에 해결할 수 있는지를 보는 문제였다.


from collections import deque

def bfs():
  queue = deque()
  queue.append((0, 0, 0, 0))
  visited[0][0][0] = True
  visited[0][0][1] = True
  while queue:
    x, y, z, dis = queue.popleft()
    if x == n - 1 and y == m - 1:
      print(dis + 1)
      return
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z]:
        if graph[nx][ny] == 0:
          visited[nx][ny][z] = True
          queue.append((nx, ny, z, dis + 1))
        else:
          if z == 0:
            visited[nx][ny][z] = True
            queue.append((nx, ny, 1, dis + 1))

  print(-1)

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

visited = [[[False, False] for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs()

