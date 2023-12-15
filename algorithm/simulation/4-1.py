#상하좌우
#여행가 A는 N*N 크기의 정사각형 공간 위에 서 있다. 가장 왼쪽 위 좌표는 (1,1)이다. A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작좌표는 항상 (1,1)이다.

n = int(input())
x, y = 1, 1
plans = input().split()

#북, 남, 동, 서 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  nx, ny = 0, 0
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)
    