#집합의 표현(골드 5)
#내 풀이
#유니온 파인드 알고리즘을 공부하자

import sys
sys.setrecursionlimit(10000)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  

n, m = map(int, input().split())
parent = list(range(n + 1))
commands = []
for _ in range(m):
  o, a, b = map(int, input().split())
  commands.append((o, a, b))

for i in range(m):
  order, a, b = commands[i]

  if order == 0:
    union_parent(parent, a, b)
  elif order == 1:
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x == y:
      print('YES')
    else:
      print('NO')