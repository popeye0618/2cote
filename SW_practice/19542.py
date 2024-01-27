#내 풀이
#depth를 기록하며, 끝까지 방문한 후 현재 answer에서 d만큼 빼줌

# def dfs(s, depth):
#   global answer

#   visited[s] = True
#   flag = False
#   for i in graph[s]:
#     if not visited[i]:
#       flag = True
#       break
#   if not flag:
#     return depth - d
  
#   for i in graph[s]:
#     if not visited[i]:
#       t = dfs(i, depth + 1)
#       if t >= 0:
#         answer += 1
#       print('now', s, 't', t, 'ans', answer)
        
#   return t - 1
  
# n, start, d = map(int, input().split())
# graph = [[]for _ in range(n + 1)]
# for _ in range(1, n):
#   x, y = map(int, input().split())
#   graph[x].append(y)
#   graph[y].append(x)

# visited = [False] * (n + 1)
# answer = 0
# dfs(start, 0)
# print(answer)


def dfs(now, pre):
  global answer
  max_depth = 0
  visited[now] = True
  for i in graph[now]:
    if i != pre:
      max_depth = max(max_depth, dfs(i, now))

  if max_depth >= d:
    answer += 1
  print('now', now, 'return', max_depth + 1, 'ans', answer)
  return max_depth + 1

n, s, d = map(int, input().split())
graph = [[]for _ in range(n + 1)]
for _ in range(1, n):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n + 1)
answer = 0
dfs(s, 0)
print(2 * (answer - 1))