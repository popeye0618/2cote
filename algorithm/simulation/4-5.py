#게임 개발
#내 풀이
#가본 곳은 체크해야 하므로, 0은 방문하지 않은 육지, 1은 바다, 2는 방문 했던 육지

n, m = map(int, input().split())
y, x, d = map(int, input().split())
gmap = []

cnt = 1

for _ in range(n):
  row = list(map(int, input().split()))
  gmap.append(row)

gmap[y][x] = 2
#북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

bx = [0, -1, 0, 1]
by = [1, 0, -1, 0]

end = False
while not end:
  chk = False
  
  for _ in range(4):
    d -= 1
    if d < 0:
      d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    if gmap[ny][nx] == 1 or gmap[ny][nx] == 2:
      continue
    elif gmap[ny][nx] == 0:
      cnt += 1
      gmap[ny][nx] = 2
      x, y = nx, ny
      chk = True
      break

  if not chk: #4방향 모두 바다이거나, 가본 곳인 경우
    nx = x - bx[d]
    ny = y - by[d]
    if gmap[ny][nx] == 1:
      end = True
    x, y = nx, ny

print(cnt)