#치킨 배달(골드 5)
#내 풀이
#백트래킹으로 구현
#치킨집을 폐업시키면서 모든 경우의 수 돌려보기
#맵을 수정하는 느낌의 문제는 백트래킹 항상 생각해보기

#피드백
#그래프 탐색문제 풀때처럼 하나하나 구현하는 방식으로 했는데 도저히 시간초과때문에 안됐다.
#해설을 보니 조합을 사용했는데, 왜 이생각을 못했을까..
#치킨집 m개를 선택하는 모든 조합에 대하여 치킨거리를 구한다.

from itertools import combinations

n, m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
ans = []
chickens = []
house = []
for x in range(n):
  for y in range(n):
    if graph[x][y] == 2:
      chickens.append([x + 1 , y + 1])
    if graph[x][y] == 1:
      house.append([x + 1, y + 1])

for case in combinations(chickens, m):
  sum = 0
  for home in house:
    min_value = 99999
    a, b = home
    for x, y in case:
      dist = abs(x - a) + abs(y - b)
      min_value = min(min_value, dist)
    sum += min_value
  ans.append(sum)

print(min(ans))