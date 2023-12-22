#연구소(골드 4)
#내 풀이
#아이디어는 벽을 칠 수 있는 만큼 치고 바이러스를 퍼뜨린 후에, 빈칸의 개수를 저장
#max값 출력
#벽을 칠 때는 그냥 하나하나 다 쳐보는 방법
#바이러스를 퍼뜨릴 때는 bfs를 이용, 빈칸의 개수를 셀 때는 bfs를 이용해도 되지만, 최대가 8 * 8이므로 반복문으로 세도 될 것 같다.

from collections import deque
import copy

def bfs():
  global result
  copy_lab = copy.deepcopy(lab)
  queue = deque()
  for y in range(n):
    for x in range(m):
      if copy_lab[y][x] == 2:
        queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and copy_lab[ny][nx] == 0:
        copy_lab[ny][nx] = 2
        queue.append((nx, ny))
        
  temp = 0
  for i in range(n):
    for j in range(m):
      if copy_lab[i][j] == 0:
        temp += 1
  result = max(result, temp)

#몰랐는데 벽을 세우고 다시 허무는 이 과정을 백트래킹이라고 한다.
def wall(cnt):
  if cnt == 3:
    bfs()
    return
    
  for y in range(n):
    for x in range(m):
      if lab[y][x] == 0:
        lab[y][x] = 1
        wall(cnt + 1)
        lab[y][x] = 0

n, m = map(int, input().split())
lab = []
for _ in range(n):
  lab.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
wall(0)

print(result)