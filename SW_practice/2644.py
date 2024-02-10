#촌수 계산

def dfs(x, cnt):
  stack = []
  stack.append((x, cnt))
  visited.add(x)
  
  while stack:
    x, cnt = stack.pop()
    if x == e:
      return cnt
    for i in range(len(graph[x])):
      if graph[x][i] not in visited:
        stack.append((graph[x][i], cnt + 1))
        visited.add(graph[x][i])

  return -1

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = set()
ans = dfs(s, 0)
print(ans)