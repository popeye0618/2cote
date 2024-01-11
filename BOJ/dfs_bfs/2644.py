#촌수계산(실버 2)
#내 풀이
#dfs를 이용해서 얼마나 떨어져있는지 depth를 출력한다.

def dfs(node, cnt):
  visited.add(node)
  if node == end:
    print(cnt)
    return True

  for now in graph[node]:
    if now not in visited:
      if dfs(now, cnt + 1):
        return True
  return False


n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

answer = 0
visited = set()
if not dfs(start, 0):
  print(-1)
