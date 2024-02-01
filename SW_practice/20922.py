#겹치는건 싫어

from collections import defaultdict, deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
num = defaultdict(int)
queue = deque()

now = 0
start = 0
ans = 0
while now < n:
  if num[arr[now]] < k:
    num[arr[now]] += 1
    queue.append(arr[now])
  else:
    for idx in range(start, now + 1):
      num[arr[idx]] -= 1
      if not queue and now < n:
        start = idx + 1
        queue.append(arr[idx])
        num[arr[idx]] += 1
        break
      if queue and arr[now] == queue.popleft():
        start = idx + 1
        queue.append(arr[idx])
        num[arr[idx]] += 1
        break

  now += 1
  ans = max(len(queue), ans)
  
print(ans)
