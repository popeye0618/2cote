#N번째 큰 수(실버 2)
#내 풀이
#그냥 값 넣고 최대 힙 방식으로 풀면 될 것 같다.

#피드백
#메모리 초과가 나서 다시 생각해봤다.
#메모리를 줄이려면 힙에 넣을 때 다 넣지 말고, n개를 유지하면서 넣었다 뺏다 하는 것이 방법이다.
#최소 힙을 이용하면 n개가 넘을 경우 맨 앞에 가장 작은 원소가 보장되므로
#pop을 하면서 진행할 수 있다.

import sys, heapq
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
  num.append(list(map(int, input().split())))

h = []
for i in range(n):
  for j in range(n):
    heapq.heappush(h, num[i][j])
    if len(h) > n:
      heapq.heappop(h)

print(heapq.heappop(h))