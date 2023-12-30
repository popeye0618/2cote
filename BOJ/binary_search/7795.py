#먹을 것인가 먹힐 것인가(실버 3)
#내 풀이
#이 문제는 bisect를 이용해서 풀 수 있다.
#A의 원소마다 bisect_left를 이용해서 인덱스를 얻어오면 그 인덱스 만큼 작은 값이 있는 것

from bisect import bisect_left

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  b.sort()
  sum = 0
  for num in a:
    sum += bisect_left(b, num)
  print(sum)