#카드2
#큐 사용

from collections import deque

n = int(input())
queue = deque()

for i in range(1, n + 1):
  queue.append(i)

i = 0
while len(queue) > 1:
  if i % 2 == 0:
    queue.popleft()
  else:
    queue.append(queue.popleft())

  i += 1
print(queue.popleft())