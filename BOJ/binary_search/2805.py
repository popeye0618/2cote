#나무 자르기(실버 2)
#내 풀이
#1부터 제일 긴 나무까지를 범위로 잡고 이분 탐색 진행
#진행 할 때마다 자르고 난 나머지 값들 더해서 m보다 크면 ans에 mid 저장
#크면 right를 줄이고, 작으면 left를 키우는 방식으로 진행

n, m = map(int, input().split())
tree = list(map(int, input().split()))

def binary_search(tree, target):
  left = 1
  right = max(tree)
  ans = 0
  while left <= right:
    mid = (left + right) // 2
    sum = 0
    for leng in tree:
      if leng > mid:
        sum += leng - mid
    if sum >= target:
      ans = mid
      left = mid + 1
    else:
      right = mid - 1
  return ans
print(binary_search(tree, m))