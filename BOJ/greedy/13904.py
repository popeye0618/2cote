#과제 (골드 3)
#내 풀이
#거꾸로 가면서 풀면 풀 수 있을 것 같다.(한번에 성공!)

n = int(input())
arr = []
max_day = 0
for _ in range(n):
  day, score = map(int, input().split())
  max_day = max(max_day, day)
  arr.append((day, score))

sorted_arr = sorted(arr, key=lambda x: (-x[0], -x[1]))
visited = [False for _ in range(n)]
result = 0

idx = -1
for day in range(max_day, 0, -1):
  max_value = 0
  for j in range(n):
    if day <= sorted_arr[j][0] and not visited[j] and max_value < sorted_arr[j][1]:
      max_value = sorted_arr[j][1]
      idx = j
  if max_value > 0:
    visited[idx] = True
    result += max_value
print(result)
