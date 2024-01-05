#보석 도둑(골드 2)
#내 풀이
#고려해야 할 점은 보석의 가치와 무게

#피드백
#일단 우선순위 큐에 대해서 더 생각해 보는 계기가 되는 문제였다.
#이 문제는 우선순위 큐를 두 개 사용하는데, 처음에는 무게를 기준으로 최소 힙
#두 번째는 가치를 기준으로 최대 힙 이렇게 사용한다.
#해결 과정은 우선 가방의 용량을 탐색하면서 이 용량보다 가벼운 무게를 가진 모든 보석의 가치를 최대 힙에 넣는다.
#이제 그 최대 힙을 pop하면 가치가 가장 큰 보석이 나올 것이다.
#다음 가방의 용량도 마찬가지로 남은 보석들 중 용량보다 가벼운 무게를 가진 모든 보석의 가치를 최대 힙에 넣고
#최대 힙에서 pop을 해서 나온 가치를 결과에 더해준다.


import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    weight, price = map(int, input().split())
    heapq.heappush(jewels, (weight, price))

bags = sorted([int(input()) for _ in range(k)])
result = 0

available_jewels = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        weight, price = heapq.heappop(jewels)
        heapq.heappush(available_jewels, -price)

    if available_jewels:
        result -= heapq.heappop(available_jewels)

print(result)
