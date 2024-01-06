#빵집(골드 2)
#내 풀이
#우선 깊이우선 탐색이 좋아보인다.
#오른쪽 위, 오른쪽, 오른쪽 아래를 순차적으로 탐색하며
#맨 끝 열에 도착한 경우 True를 리턴하고, 나머지는 False를 리턴한다.

#중요한 사실을 알게되었는데
#백트래킹이 필요한 경우 재귀함수를 사용하는게 좋고,
#재귀 호출 횟수가 많아질 것 같은 경우에는 스택을 사용하는게 좋다.
#스택을 사용하며 백트래킹을 구현하는 것은 복잡하기 때문

import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  if y == m - 1:
    return True

  for i in range(3):
    nx = x + dx[i]
    ny = y + 1
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
      graph[nx][ny] = 'x'
      if dfs(nx, ny):
        return True
  return False

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

dx = [-1, 0, 1]
answer = 0

for x in range(n):
  if dfs(x, 0):
    answer += 1

print(answer)