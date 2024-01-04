#절댓값 힙(실버 1)
#내 풀이
#단순히 heapq 라이브러리를 사용하면 된다.
#하지만 절댓값 힙이므로 abs를 붙여야한다.
#그리고 우선순위 큐를 사용할 때 튜플로 사용하면 첫 번째 원소를 기준으로 작동한다.

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
      val = heapq.heappop(h)
      if val[1] == 'minus':
        print(-(val[0]))
      else:
        print(val[0])
  elif order > 0:
    heapq.heappush(h, (abs(order), 'plus'))
  else:
    heapq.heappush(h, (abs(order), 'minus'))