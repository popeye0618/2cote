#숫자 고르기(골드 5)
#내 풀이
#얼추 비슷했지만 수정해야 할 사항도 여럿 있었다.

#피드백
#아무래도 사이클이 있는 그래프를 찾는걸 처음해보니 헷갈렸다.
#순환의 시작점으로 돌아왔을 경우에만 고려해야한다.

def dfs(x):
  stack = []
  start = x
  stack.append((x, [start]))
  visited[x] = True

  if graph[x] == x:
    answer.add(x)
    return

  while stack:
    x, past = stack.pop()
    nx = graph[x]
    if nx in answer:
      return
    if visited[nx]:
      if nx == start:
        for i in past:
          answer.add(i)
      return

    visited[nx] = True
    past.append(nx)
    stack.append((nx, past))

n = int(input())
graph = [0] * (n + 1)
for i in range(1, n + 1):
  graph[i] = int(input())

answer = set()

for i in range(1, n + 1):
  if graph[i] == i:
    answer.add(i)

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  if i not in answer:
    dfs(i)

print(len(answer))
ans = sorted(answer)
for i in ans:
  print(i)