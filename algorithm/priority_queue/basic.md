우선순위 큐
우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.

구현하는 방법
1. 단순히 리스트를 이용하여 구현 (삽입 시간: O(1), 삭제 시간: O(N))
2. 힙(heap)을 이용하여 구현 (삽입 시간: O(log N), 삭제 시간: O(log N))

힙의 특징
힙은 완전 이진 트리 자료구조의 일종
힙에서는 항상 루트 노드를 제거한다.

최소 힙(min heap)
 - 루트 노드가 가장 작은 값을 가진다. 따라서 값이 작은 데이터가 우선적으로 제거
최대 힙(max heap)
 - 루트 노드가 가장 큰 값을 가진다. 따라서 값이 큰 데이터가 우선적으로 제거

우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
파이썬의 큐 라이브러리는 기본적으로 min heap이며
max heap이 필요한 경우 데이터를 넣을 때와 꺼낼 때 -를 붙여서 꺼내면 된다.
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
  h = []
  result = []
  #모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

n = int(input())
arr = []

for i in range(n):
  arr.append(int(input()))
res = heapsort(arr)

for i in range(n):
  print(res[i])

