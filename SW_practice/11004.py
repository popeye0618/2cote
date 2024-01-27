#k번째 수
#내 풀이
#우선순위 큐 사용

import heapq

n, k = map(int, input().split())
h = list(map(int, input().split()))

heapq.heapify(h)

for i in range(k - 1):
    heapq.heappop(h)

print(heapq.heappop(h))
