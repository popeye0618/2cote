#보석 도둑
#내 풀이
#무게 기준으로 최소 힙으로 보석 입력
#그 다음 가방 무게 탐색하며 현재 가방에 들어갈 수 있는 보석들을
#가격 기준으로 최대 힙에 넣음


import heapq, sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
bags = []
for _ in range(n):
  w, p = map(int, input().split())
  heapq.heappush(jewels, (w, p))
for _ in range(k):
  bags.append(int(input()))

bags.sort()
price = []
result = 0

for bag in bags:
  for _ in range(n):
    if jewels and jewels[0][0] <= bag:
      w, p = heapq.heappop(jewels)
      heapq.heappush(price, -p)
    else:
      break

  if price:
    p = heapq.heappop(price)
    result += -p

print(result)