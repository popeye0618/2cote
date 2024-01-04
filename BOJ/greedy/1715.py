#카드 정렬하기(골드 4)
#내 풀이
#만든 묶음은 마지막을 제외하고 두 번씩 더해진다.
#따라서 정렬 후 묶는 것이 효율적일 것이다.

#피드백
#처음엔 단순히 정렬해서 더해주면 될 것 같았는데 출력초과(틀렸습니다)가 나왔다.
#생각해보니 더한 값이 크다면 결과는 비효율적인 카드 비교 횟수가 나올 것이다.
#따라서 우선순위 큐를 사용해서 더한 값을 우선순위 큐에 또 넣는 방식으로 진행한다.

import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))

result = 0
if len(cards) == 1:
  print(0)
else:
  while len(cards) > 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    result += num1 + num2
    heapq.heappush(cards, num1 + num2)
  print(result)