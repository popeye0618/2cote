#DSLR(골드 4)
#내 풀이
#bfs로 모든 경우를 해본다.

from collections import deque

def calD(num):
  return (num * 2) % 10000

def calS(num):
  if num == 0:
    return 9999
  else:
    return num - 1

def calL(num):
  s = str(num)
  l = 4 - len(s)
  if l > 0:
    s = ('0' * l) + s[:]
  tmp = s[0]
  s = s[1:] + tmp
  return int(s)

def calR(num):
  s = str(num)
  l = 4 - len(s)
  if l > 0:
    s = ('0' * l) + s[:]
  tmp = s[3]
  s = tmp + s[:3]
  return int(s)
  
def bfs(start, end):
  queue = deque()
  queue.append((start, ''))
  visited = set()

  while queue:
    x, path = queue.popleft()
    if x == end:
      print(path)
      break
    if x in visited:
      continue
    visited.add(x)
      
    queue.append((calD(x), path + 'D'))
    queue.append((calS(x), path + 'S'))
    queue.append((calL(x), path + 'L'))
    queue.append((calR(x), path + 'R'))
      
t = int(input())
for _ in range(t):
  start, end = map(int, input().split())

  bfs(start, end)
  