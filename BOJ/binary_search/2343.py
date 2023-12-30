#기타 레슨(실버 1)
#내 풀이
#이진 탐색을 하면서 왼쪽, 오른쪽으로 분할될 때 더 분할된 애들의 합이 큰 값을 기록하고, 큰 쪽으로 시작점을 옮긴다.

#피드백
#이진 탐색문제를 풀 때는 항상 mid가 정답이 나올 수 있도록 해야한다.
#따라서 합을 기준으로 문제를 풀어보자

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr):
  left = max(arr)
  right = sum(arr)
  ans = 0
  while left <= right:
    mid = (left + right) // 2
    count = 1
    total = 0
    for i in arr:
      if total + i > mid:
        count += 1
        total = 0
      total += i
    if count <= m:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1
  
  return ans

print(binary_search(arr))