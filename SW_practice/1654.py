#랜선 자르기

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

left = 1
right = sum(arr) // m

result = 0
while left <= right:
  mid = (left + right) // 2
  cnt = 0

  for i in arr:
    cnt += i // mid

  if cnt < m:
    right = mid - 1
  else:
    left = mid + 1
    result = mid

print(result)