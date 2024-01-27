import sys

n, m = map(int, sys.stdin.readline().split())
growth = [0] * (2 * n - 1)

for _ in range(m):
  zero, one, two = map(int, sys.stdin.readline().split())
  for i in range(zero, zero + one):
    growth[i] += 1
  for i in range(zero + one, 2 * n - 1):
    growth[i] += 2

grid = [[1] * n for _ in range(n)]

for i in range(n):
  grid[i][0] += growth[n - 1 - i]
for i in range(1, n):
  grid[0][i] += growth[n - 1 + i]

for i in range(1, n):
  for j in range(1, n):
    grid[i][j] = grid[0][j]

for row in grid:
  print(' '.join(map(str, row)))
