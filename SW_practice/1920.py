#수 찾기
#이분탐색으로 수가 있는지 판별

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
tmp = list(map(int, input().split()))

arr.sort()
for d in tmp:
  left = 0
  right = n - 1

  flag = False
  while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == d:
      print(1)
      flag = True
      break

    if arr[mid] > d:
      right = mid - 1
    else:
      left = mid + 1
  if not flag:
    print(0)