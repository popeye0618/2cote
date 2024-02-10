#이중 우선순위 큐
#삭제할때도 우선순위를 적용
#아마 heapq를 써야겠지?
#중요한 아이디어는 삭제할 때, max와 min 힙의 동기화
#값에 식별자를 달아서 둘 중 어디에서라도 지워지면 집합에서 제거
#값이 수정되고 나서 다른 힙도 동기화해줌

import heapq

t = int(input())
for _ in range(t):
  k = int(input())
  min_heap = []
  max_heap = []
  tmp = set()
  id = 0
  for _ in range(k): 
    command, value = input().split()
    value = int(value)

    if command == 'I':
      heapq.heappush(min_heap, (value, id))
      heapq.heappush(max_heap, (-value, id))
      tmp.add(id)
      id += 1
    else:
      if not min_heap or not max_heap:
        continue
      
      if value == -1:
        while min_heap:
          v, i = heapq.heappop(min_heap)
          if i in tmp:
            tmp.remove(i)
            break
          
      elif value == 1:
        while max_heap:
          v, i = heapq.heappop(max_heap)
          if i in tmp:
            tmp.remove(i)
            break
  
  max_value = None
  while max_heap:
    max_value, i = heapq.heappop(max_heap)
    if i in tmp:
      break
    else:
      max_value = None
  if max_value is not None:
    tmp.remove(i)

  min_value = None
  while min_heap:
    min_value, i = heapq.heappop(min_heap)
    if i in tmp:
      break
    else:
      min_value = None
  if min_value is not None:
    tmp.remove(i)

  if max_value is None:
    print('EMPTY')
  else:
    max_value = -max_value
    if  min_value is None:
      min_value = max_value
    print(max_value, min_value)