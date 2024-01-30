#로봇 시뮬레이션
#시뮬레이션 돌려보기

b, a = map(int, input().split())
n, m = map(int, input().split())
graph = [[0 for _ in range(b)] for _ in range(a)]
direct = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robots = []
orders = []
for i in range(n):
  x, y, d = input().split()
  x, y = int(x)-1, int(y)
  graph[a - y][x] = i + 1
  robots.append([a - y, x, direct[d]])
for _ in range(m):
  x, y, z = input().split()
  orders.append((int(x) - 1, y, int(z)))

for i in range(m):
  robot, order, repeat = orders[i]
  x, y, z = robots[robot]

  if order == 'F':
    for _ in range(repeat):
      x, y, d = robots[robot]
      nx = x + dx[d]
      ny = y + dy[d]
      if nx < 0 or nx >= a or ny < 0 or ny >= b:
        print(f'Robot {robot + 1} crashes into the wall')
        exit()
      if graph[nx][ny] != 0:
        print(f'Robot {robot + 1} crashes into robot {graph[nx][ny]}')
        exit()
      graph[x][y], graph[nx][ny] = 0, robot
      robots[robot] = [nx, ny, d]

  elif order == 'L':
    x, y, d = robots[robot]
    for _ in range(repeat):
      d = (d + 3) % 4
    robots[robot] = [x, y, d]
  elif order == 'R':
    x, y, d = robots[robot]
    for _ in range(repeat):
      d = (d + 1) % 4
    robots[robot] = [x, y, d]

print('OK')
