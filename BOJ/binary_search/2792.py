#보석 상자
#내 풀이
#0부터 최대 보석 개수까지 이분탐색을 한다
#mid를 빼서 나눠진 개수가 학생 수보다 작거나 같으면 정답에 담고 mid를 줄이고
#나눠진 개수가 학생 수보다 많으면 mid를 늘린다.

n, m = map(int, input().split())
j = []
for _ in range(m):
  j.append(int(input()))

def binary_search(j):
  left = 0
  right = max(j)
  ans = 0
  while left <= right:
    mid = (left + right) // 2
    if mid == 0:
      return max(j)
    count = 0
    for x in j:
      if x >= mid:
        if x % mid == 0:
          count += x // mid
        else:
          count += x // mid
          count += 1
      else:
        count += 1
    if count <= n:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1
  return ans
print(binary_search(j))