#숨바꼭질
#내 풀이
#bfs를 사용

from collections import deque

def bfs(start):
  queue = deque()
  queue.append((start, 0))
  visited[start] = True

  while queue:
    now, time = queue.popleft()
    if now == k:
      return time

    for next in [now - 1, now + 1, now * 2]:
      if 0 <= next <= max_value and not visited[next]:
        queue.append((next, time + 1))
        visited[next] = True
    

n, k = map(int, input().split())
max_value = max(n, k) * 2
visited = [False] * (max_value + 1)
print(bfs(n))