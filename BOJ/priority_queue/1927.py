#최소 힙(실버 2)
#내 풀이
#단순히 heapq 라이브러리를 사용하면 된다.
#하지만 우선순위 큐에 대해서 이해는 필수이다.

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
  order = int(input())
  if order == 0:
    if not h:
      print(0)
    else:
      print(heapq.heappop(h))
  else:
    heapq.heappush(h, order)