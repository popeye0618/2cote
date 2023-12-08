#강의실 배정(골드 5)
#내 풀이
#같은 강의실에서 들을 수 있는 수업을 다 제거하고 1을 더한다. 남은 강의도 마찬가지로 같은 강의실에서 들을 수 있는 수업을 다 제거하고 1을 더한다. 리스트가 빈 리스트가 될 때까지 반복한다.
#시작시간이 같고 종료시간이 다른경우 뒤에 연결될 수 있는 것이 우선으로 소모된다.

n = int(input())
c = []
for _ in range(n):
  row = list(map(int, input().split()))
  c.append(row)
c = sorted(c, key = lambda x:x[0])
result = 0
ptr = 0
now_time = c[0][1]
del c[0]
while len(c) > 0:
  if 
  if c[ptr][0] == now_time:
    now_time = c[ptr][1]
    ptr += 1