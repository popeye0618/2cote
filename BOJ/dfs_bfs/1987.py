#알파벳 (골드4)
#내 풀이
#이 문제는 dfs로 풀어야 할 것 같다. 지나갔던 알파벳들을 리스트와 비교해서 없으면 넣고, 있으면 거기서 dfs를 종료
#1트 시간초과, 2트 틀림
#검색해보니 시간초과를 방지하기 위해 지나온 좌표까지 저장하는 것을 볼 수 있었다. 그리고 dfs를 재귀로밖에 구현하지 못했는데, 스택으로 구현하는 연습도 필요하다고 느꼈다.
#스택으로 구현은 약간 bfs느낌도 나는 것 같다. 똑같이 얘는 스택에 add하고, pop하고 pop한 원소에 관해서 처리하고 하는 느낌

def dfs(v, already, depth):
  global ans
  y, x = v
  stack = set()
  stack.add((y, x, already + graph[y][x], depth))
  while stack:
    nowy, nowx, nowalready, nowdepth = stack.pop()
    ans = max(ans, nowdepth)

    for i in range(4):
      nx = nowx + dx[i]
      ny = nowy + dy[i]
      if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] not in nowalready:
        stack.add((ny, nx, nowalready + graph[ny][nx], nowdepth + 1))

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
dfs((0, 0), '', 1)
print(ans)