#정렬된 배열에서 특정 수의 개수 구하기
#N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
#이 수열에서 x가 등장하는 횟수를 계산하라
#시간복잡도 O(log N)으로 설계하지 않으면 시간초과

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

left = bisect_left(array, x)
right = bisect_right(array, x)
cnt = right - left

if cnt == 0:
  print(-1)
else:
  print(cnt)