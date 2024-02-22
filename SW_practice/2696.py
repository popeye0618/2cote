#중앙값구하기 (골드 2)
#내 풀이
#bisect로 정렬 유지하고, 가운데 인덱스 출력
#아이디어는 맞았는데 입력이 많은 경우 여러줄에 걸쳐서 입력받을 수 있다.
#따라서 입력받는 형식을 바꿔야만 성공했다.

from bisect import bisect_left

t = int(input())
for _ in range(t):
  m = int(input())
  arr = []
  while len(arr) < m:
    arr.extend(map(int, input().split()))
    
  temp = []
  answer = []
  for i in range(m):
    n = arr[i]
    idx = bisect_left(temp, n)
    temp.insert(idx, n)
    if i % 2 == 0:
      answer.append(temp[i // 2])

  print(len(answer))
  for i in range(0, len(answer), 10):
    print(' '.join(map(str, answer[i : i + 10])))