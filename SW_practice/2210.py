#숫자판 점프(실버 2)
#내 풀이
#dfs를 이용하고, 방문은 set으로 처리해서 중복을 제거

def dfs(x, y, string):
  if len(string) == 6:
    if string not in visited:
      visited.add(string)
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 5 and 0 <= ny < 5:
      dfs(nx, ny, string + graph[nx][ny])

graph = []
for _ in range(5):
  t = list(map(int, input().split()))
  graph.append(list(map(str, t)))

visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(5):
  for j in range(5):
    dfs(i, j, graph[i][j])

print(len(visited))