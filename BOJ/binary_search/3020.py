#개똥벌레(골드 5)
#내 풀이
#이 문제는 누적합과 이분탐색으로 풀 수 있다.
#우선 이분탐색은 석순과 종유석을 정렬시켜놓고, 개똥벌레가 특정 값 이상부터는 모두 부딪히므로
#이분탐색을 통해 그 특정값을 찾으면 된다.
#누적합으로 푸는 방법은 정렬시켜놓고 처음으로 부딪히는 구간 이후는 반드시 부딪힌다는 것이므로
#누적된 값을 더해주면 된다.

#이분 탐색
n, h = map(int, input().split())
over = []
under = []
for i in range(n):
  if i % 2 != 0:
    under.append(int(input()))
  else:
    over.append(int(input()))
over.sort()
under.sort()

def binary_search(arr, left, right, target):
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid -1
  return left

min_cnt = n
ans = [n, 0]
for i in range(1, h + 1):
  down = len(under) - binary_search(under, 0, len(under) - 1, i - 0.5)
  up = len(over) - binary_search(over, 0, len(over) - 1, h - i + 0.5)

  if min_cnt == down + up:
    ans[1] += 1
  elif min_cnt > down + up:
    min_cnt = down + up
    ans = [min_cnt, 1]

print(ans[0], ans[1])

#누적 합
n, h = map(int, input().split())
over = [0] * (h + 1)
under = [0] * (h + 1)
for i in range(n):
  if i % 2 != 0:
    under[int(input())] += 1
  else:
    over[int(input())] += 1

for i in range(h - 1, 0, -1):
  under[i] += under[i + 1]
  over[i] += over[i + 1]

min_cnt = n
ans = [n, 0]
for i in range(1, h + 1):
  if min_cnt == under[i] + over[h - i + 1]:
    ans[1] += 1
  elif min_cnt > under[i] + over[h - i + 1]:
    min_cnt = under[i] + over[h - i + 1]
    ans = [min_cnt, 1]

print(ans[0], ans[1])