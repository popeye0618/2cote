#강의실 배정(골드 5)
#내 풀이
#우선 강의 시작시간 기준으로 오름차순 정렬을 한다.
#첫 번째 강의 종료 시간을 우선순위 큐에 넣는다.
#그 다음 강의의 시작시간과 우선순위 큐의 첫 번째 원소를 비교해서 크거나 같다면 
#강의실 재사용 가능하므로 pop한 후 그 강의의 종료시간을 넣어준다.
#작다면 pop하지 않고 그 강의의 종료시간을 새로 넣어준다.

import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
  time.append(tuple(map(int, input().split())))

sorted_time = sorted(time, key = lambda x : x[0])

h = [sorted_time[0][1]]
for lecture in sorted_time[1:]:
  if lecture[0] >= h[0]:
    heapq.heappop(h)
    heapq.heappush(h, lecture[1])
  else:
    heapq.heappush(h, lecture[1])
print(len(h))