#사이버 개강총회
#내 풀이
#입력 받고 같은 사람 있을 수 있으니까 set 사용해서 시간복잡도 줄임

import sys

s, e, q = input().split()
s = int(s.replace(":", ""))
e = int(e.replace(":", ""))
q = int(q.replace(":", ""))

enter = set()
answer = 0

for line in sys.stdin:
  time, name = line.split()
  time = int(time.replace(":", ""))

  if time <= s:
    enter.add(name)

  if e <= time <= q and name in enter:
    answer += 1
    enter.remove(name)

print(answer)