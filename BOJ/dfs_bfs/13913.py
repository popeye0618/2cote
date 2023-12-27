#숨바꼭질4 (골드 4)
#내 풀이
#뭔가 문제가 생긴게 그리디같긴해서 일단 그리디로 풀어본다.
#이런 문제의 특징은 항상 뒤에서 앞으로 가는 방법이 유효했으니까 그 방법으로 풀어본다.

#피드백
#그리디로는 못풀 것 같고, bfs를 이용해야하는데
#n부터 시작해서 n - 1, n + 1, n * 2중에 k가 있는지 확인, 없다면 큐에 넣고
#하나씩 pop하면서 또 -1, +1, *2중에 k가 있는지 확인, 없다면 큐에 넣고 반복
#큐에 넣을 때 time으로 본인이 몇 번 왔는지도 함께 저장해준다.
#경로까지 저장해서 n == k가 됐을 때 시간과 경로를 출력

from collections import deque

n, k = map(int, input().split())
cnt = 0
ans = []

def bfs():
  queue = deque()
  queue.append([n, 0, [n]])
  visited[n] = True

  while queue:
    x, time, route = queue.popleft()
    if x == k:
      print(time)
      print(' '.join(map(str, route)))
      return
    dx = [x - 1, x + 1, x * 2]
    for nx in dx:
      if 0 <= nx <= 100000 and not visited[nx]:
        visited[nx] = True
        r = route + [nx]
        queue.append([nx, time + 1, r])

if n == k:
  print(0)
  print(n)
elif n > k:
  while n >= k:
    ans.append(n)
    n -= 1
    cnt += 1
  print(cnt - 1)
  print(' '.join(map(str, ans)))
else:
  visited = [False for _ in range(250000)]
  bfs()